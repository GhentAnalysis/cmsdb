# coding: utf-8

"""
Refresh the n_files / n_events entries of a custom NanoAOD campaign (default: run3_2024_customnano_v15) from DAS.

USAGE:
    python scripts/update_das_counts.py                       # all files -> /tmp copies
    python scripts/update_das_counts.py data.py               # subset
    python scripts/update_das_counts.py --out-dir /tmp/check
    python scripts/update_das_counts.py --in-place            # overwrite the cmsdb files
    python scripts/update_das_counts.py --campaign run2_2018_customnano_v15 top.py ewk.py higgs.py
"""

from __future__ import annotations

import os
import re
import sys
import json
import subprocess
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor

CAMPAIGNS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "cmsdb", "campaigns",
)
DEFAULT_CAMPAIGN = "run3_2024_customnano_v15"
DEFAULT_FILES = ["data.py", "top.py", "qcd.py", "ewk.py", "higgs.py"]
DAS_INSTANCE = "prod/phys03"

key_re = re.compile(r'^\s*"(/[^"]+/USER)",')
n_files_re = re.compile(r"^(\s*)n_files=(\d+),\s*$")
n_events_re = re.compile(r"^(\s*)n_events=(\d+),\s*$")


class Block(object):
    """
    One active cpn.add_dataset entry: its dataset key and the line indices holding the counts.
    """

    def __init__(self, key: str, key_line: int) -> None:
        self.key = key
        self.key_line = key_line
        self.n_files_line = None
        self.n_files = None
        self.n_events_line = None
        self.n_events = None

    @property
    def complete(self) -> bool:
        return self.n_files_line is not None and self.n_events_line is not None


def parse_blocks(lines: list[str]) -> list[Block]:
    """
    Scan lines for active (non-commented) dataset blocks and return the ones carrying both counts.
    """
    blocks, pending = [], None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("#"):
            continue

        match = key_re.match(line)
        if match:
            pending = Block(match.group(1), i)
            continue

        if pending is None:
            continue

        match = n_files_re.match(line)
        if match:
            pending.n_files_line, pending.n_files = i, int(match.group(2))
            continue

        match = n_events_re.match(line)
        if match:
            pending.n_events_line, pending.n_events = i, int(match.group(2))
            continue

        # a closing paren ends the block; drop it if it never carried both counts
        if stripped == ")":
            if pending.complete:
                blocks.append(pending)
            pending = None

    return blocks


def query_das(key: str, retries: int = 1) -> tuple[int, int] | None:
    """
    Return (n_files, n_events) for a dataset key, or None if DAS has no record of it.
    """
    cmd = ["dasgoclient", "--query", f"summary dataset={key} instance={DAS_INSTANCE}"]
    for attempt in range(retries + 1):
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        except subprocess.TimeoutExpired:
            continue
        if proc.returncode != 0:
            continue
        try:
            summary = json.loads(proc.stdout.strip() or "[]")
        except json.JSONDecodeError:
            continue
        if not summary:
            continue
        n_files = int(summary[0].get("nfiles") or 0)
        n_events = int(summary[0].get("nevents") or 0)
        # a non-existent dataset comes back as an all-zero summary with exit code 0
        if n_files == 0:
            return None
        return n_files, n_events

    return None


def fetch_all(keys: list[str], workers: int) -> dict[str, tuple[int, int] | None]:
    """
    Query all unique keys in parallel, reporting progress on stderr.
    """
    unique = sorted(set(keys))
    results, done = {}, [0]

    def work(key: str) -> None:
        result = query_das(key)
        results[key] = result
        done[0] += 1
        print(f"\r  queried {done[0]}/{len(unique)}", end="", file=sys.stderr, flush=True)

    with ThreadPoolExecutor(max_workers=workers) as pool:
        list(pool.map(work, unique))
    print("", file=sys.stderr)

    return results


def process_file(campaign_dir: str, name: str, out_path: str, workers: int) -> tuple[int, int]:
    """
    Rewrite the counts of one campaign file and return (n_updated, n_failed).
    """
    src = os.path.join(campaign_dir, name)
    with open(src) as f:
        lines = f.read().splitlines(keepends=True)

    blocks = parse_blocks(lines)
    print(f"\n{name}: {len(blocks)} active datasets", file=sys.stderr)
    if not blocks:
        return 0, 0

    das = fetch_all([b.key for b in blocks], workers)

    n_updated = n_failed = 0
    for block in blocks:
        result = das.get(block.key)
        if result is None:
            print(f"  FAILED  {block.key} (no DAS record)")
            n_failed += 1
            continue
        n_files, n_events = result
        if (n_files, n_events) == (block.n_files, block.n_events):
            continue

        indent = n_files_re.match(lines[block.n_files_line]).group(1)
        lines[block.n_files_line] = f"{indent}n_files={n_files},\n"
        indent = n_events_re.match(lines[block.n_events_line]).group(1)
        lines[block.n_events_line] = f"{indent}n_events={n_events},\n"
        print(
            f"  updated {block.key}\n"
            f"          n_files {block.n_files} -> {n_files}, n_events {block.n_events} -> {n_events}",
        )
        n_updated += 1

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w") as f:
        f.write("".join(lines))
    print(f"  {len(blocks) - n_updated - n_failed} unchanged, wrote {out_path}", file=sys.stderr)

    return n_updated, n_failed


def main() -> int:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", default=None, help=f"campaign files (default: {' '.join(DEFAULT_FILES)})")
    parser.add_argument("--out-dir", default="/tmp/das_counts", help="where to write the updated copies")
    parser.add_argument("--in-place", action="store_true", help="overwrite the cmsdb files instead")
    parser.add_argument("--campaign", default=DEFAULT_CAMPAIGN, help="campaign directory below cmsdb/campaigns")
    parser.add_argument("-j", "--workers", type=int, default=8, help="parallel dasgoclient queries")
    args = parser.parse_args()

    campaign_dir = os.path.join(CAMPAIGNS_DIR, args.campaign)
    files = [os.path.basename(f) for f in (args.files or DEFAULT_FILES)]

    total_updated = total_failed = 0
    for name in files:
        out_path = os.path.join(campaign_dir if args.in_place else args.out_dir, name)
        n_updated, n_failed = process_file(campaign_dir, name, out_path, args.workers)
        total_updated += n_updated
        total_failed += n_failed

    print(f"\nsummary: {total_updated} updated, {total_failed} failed", file=sys.stderr)

    return 1 if total_failed else 0


if __name__ == "__main__":
    sys.exit(main())
