#!/usr/bin/env python3
import argparse
import csv
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from functools import lru_cache
from pathlib import Path


SPREADSHEET_URLS = {
    "2025": (
        "http://docs.google.com/spreadsheets/d/"
        "1LrKEphbzf0Ndt72WLrTjCrIh3_tuOEcQuTPHvCjlpQE/"
        "export?format=csv&gid=645761148"
    ),
    "2024": (
        "http://docs.google.com/spreadsheets/d/"
        "1LrKEphbzf0Ndt72WLrTjCrIh3_tuOEcQuTPHvCjlpQE/"
        "export?format=csv&gid=891834841"
    ),
    "2023": (
        "http://docs.google.com/spreadsheets/d/"
        "1LrKEphbzf0Ndt72WLrTjCrIh3_tuOEcQuTPHvCjlpQE/"
        "export?format=csv&gid=723442297"
    ),
    "2022": (
        "http://docs.google.com/spreadsheets/d/"
        "1LrKEphbzf0Ndt72WLrTjCrIh3_tuOEcQuTPHvCjlpQE/"
        "export?format=csv&gid=837854228"
    ),
}


CUSTOM_NANO_TAG = "CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15"

# optional override of the sample -> dataset/process mapping file (set via --mapping)
PROCESS_FILE = None


def normalize(text):
    return (text or "").strip()


@lru_cache(maxsize=1)
def load_process_mappings():
    base_dir = Path(__file__).resolve().parent / "customnano_v15"
    candidate_files = (
        base_dir / "utils" / "process.txt",
        base_dir / "utils" / "processes.txt",
        base_dir / "processes.txt",
    )

    if PROCESS_FILE:
        process_file = Path(PROCESS_FILE)
    else:
        process_file = next((path for path in candidate_files if path.exists()), None)
    if not process_file or not process_file.exists():
        return []

    mappings = []
    for line in process_file.read_text(encoding="utf-8").splitlines():
        text = normalize(line)
        if not text or text.startswith("#"):
            continue

        columns = text.split()
        if len(columns) < 3:
            continue

        sample_path, dataset_name, process_name = columns[:3]
        # optional fourth column: output group (top, ewk, qcd, higgs, data)
        group = columns[3].lower() if len(columns) > 3 else ""
        sample_token = extract_sample_token(sample_path)
        mappings.append(
            {
                "sample": sample_path.lower(),
                "sample_token": sample_token,
                "dataset_name": dataset_name.lower(),
                "process_name": process_name.lower(),
                "group": group,
            }
        )

    return mappings


def extract_sample_token(dataset_path):
    parts = normalize(dataset_path).split("/")
    if len(parts) > 1 and parts[1]:
        return parts[1].lower()
    return ""


def strip_generator_tokens(text):
    cleaned = normalize(text).lower().replace("-", "_")
    for token in ("powheg", "amcatnlo", "madgraph", "pythia", "pythia8"):
        cleaned = cleaned.replace(f"_{token}", "_")
        cleaned = cleaned.replace(token, "")
    cleaned = re.sub(r"__+", "_", cleaned)
    return cleaned.strip("_")

def find_mapping_by_sample_token(sample, miniaod=""):
    sample_token_candidates = [
        extract_sample_token(miniaod),
        extract_sample_token(sample),
    ]
    sample_token_candidates = [token for token in sample_token_candidates if token]

    mappings = load_process_mappings()
    for token in sample_token_candidates:
        for mapping in mappings:
            if token == mapping["sample_token"]:
                return mapping

    return None


def extract_data_era(campaign_name):
    campaign_text = normalize(campaign_name)
    match = re.search(r"Run\d{4}([A-Za-z]+)(?:.*?(_v\d+))?", campaign_text)
    if not match:
        return ""

    era = match.group(1).lower()
    version_suffix = (match.group(2) or "").lower()
    return f"{era}{version_suffix}"


def infer_process_name(sample, miniaod="", sample_type=""):
    mapping = find_mapping_by_sample_token(sample, miniaod=miniaod)
    if mapping:
        return mapping["process_name"] or ""

    return ""


def find_header_and_indices(rows):
    needed = {"miniaod", "nanoaod", "assignment", "sample"}
    optional = {"type", "status", "events"}
    for i, row in enumerate(rows):
        lowered = [normalize(c).lower() for c in row]
        if not needed.issubset(set(lowered)):
            continue
        indices = {
            "miniaod": lowered.index("miniaod"),
            "nanoaod": lowered.index("nanoaod"),
            "assignment": lowered.index("assignment"),
            "sample": lowered.index("sample"),
        }
        for column_name in optional:
            indices[column_name] = lowered.index(column_name) if column_name in lowered else None
        # header reads "Analysis (put ttHcc, Vcb, ...)"
        indices["analysis"] = next(
            (j for j, name in enumerate(lowered) if name.startswith("analysis")),
            None,
        )
        return i, indices
    raise ValueError(
        "Could not find CSV header with MiniAOD, NanoAOD, Assignment, and Sample columns"
    )


def parse_int_value(value):
    text = normalize(value).replace(",", "")
    if not text:
        return None
    try:
        return int(text)
    except ValueError:
        return None


def parse_spreadsheet(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    header_idx, col = find_header_and_indices(rows)
    entries = []

    for row in rows[header_idx + 1:]:
        if not row:
            continue
        max_idx = max(index for index in col.values() if index is not None)
        if len(row) <= max_idx:
            continue

        miniaod = normalize(row[col["miniaod"]])
        nanoaod = normalize(row[col["nanoaod"]])
        assignment = normalize(row[col["assignment"]])
        sample = normalize(row[col["sample"]])
        sample_type = normalize(row[col["type"]]) if col.get("type") is not None and len(row) > col["type"] else ""
        status = normalize(row[col["status"]]) if col.get("status") is not None and len(row) > col["status"] else ""
        events = parse_int_value(row[col["events"]]) if col.get("events") is not None and len(row) > col["events"] else None
        analysis = normalize(row[col["analysis"]]) if col.get("analysis") is not None and len(row) > col["analysis"] else ""

        if not nanoaod and not miniaod:
            continue

        entries.append(
            {
                "miniaod": miniaod,
                "nanoaod": nanoaod,
                "assignment": assignment,
                "sample": sample,
                "status": status,
                "type": sample_type,
                "events": events,
                "analysis": analysis,
            }
        )

    return entries


def extract_dataset_name(miniaod):
    parts = normalize(miniaod).split("/")
    if len(parts) > 2 and parts[1]:
        return parts[1]
    return ""


def extract_campaign_name(miniaod):
    parts = normalize(miniaod).split("/")
    if len(parts) > 2 and parts[2]:
        return parts[2]
    return ""


def build_new_sample_names(miniaod, sample_type):
    cmd = ["dasgoclient", "--query",
           f"child dataset={miniaod} instance=prod/phys03"]
    completed = subprocess.run(cmd, capture_output=True, text=True)

    if completed.returncode != 0:
        return None

    children = [line.strip() for line in completed.stdout.splitlines()
                if line.strip()]
    if not children:
        return None

    for child in children:
        if "NanoTuples-uParTv3-parTlepID-NanoAODv15" in child:
            return child

    return None


def find_published_by_name(miniaod):
    """
    Fallback for productions published without DAS parentage (e.g. 2018): look the dataset up
    by name and pick the entry whose processed-dataset suffix matches the MiniAOD version.
    """
    dataset_name = extract_dataset_name(miniaod)
    campaign_name = extract_campaign_name(miniaod)
    if not dataset_name or not campaign_name:
        return None

    # e.g. RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2
    campaign_prefix = campaign_name.split("-", 1)[0]
    query = (
        f"dataset=/{dataset_name}/{CUSTOM_NANO_TAG}_{campaign_prefix}*/USER "
        "instance=prod/phys03"
    )
    _, candidates, _ = run_dasgoclient_query(query)
    if not candidates:
        return None

    # extensions are published with a truncated tag ("...-106X-000..."), regular samples
    # keep the global tag and version ("...-106X_v16-v2-000...")
    match = re.search(r"(_ext\d+)?-(v\d+)$", campaign_name)
    is_ext = bool(match and match.group(1))
    version = match.group(2) if match else ""
    for candidate in candidates:
        processed = candidate.split("/")[2]
        if is_ext and re.search(r"-\d+X-0+$", processed):
            return candidate
        if not is_ext and version and re.search(rf"_v\d+-{version}-0+$", processed):
            return candidate

    return None


def build_new_dataset_name(miniaod, sample_type, sample=""):
    dataset_name = extract_dataset_name(miniaod)
    campaign_name = extract_campaign_name(miniaod)

    if not dataset_name or not campaign_name:
        return ""

    if normalize(sample_type).lower() == "data":
        era = extract_data_era(campaign_name)
        if not era:
            return ""
        return f"data_{dataset_name.lower()}_{era}"

    mapping = find_mapping_by_sample_token(sample, miniaod=miniaod)
    if mapping and mapping["dataset_name"]:

        process_name = mapping["dataset_name"]

        if process_name.endswith("_powheg"):
            process_name = process_name.replace("_powheg", "")
        if process_name.endswith("_amcatnlo"):
            process_name = process_name.replace("_amcatnlo", "")
        if process_name.endswith("_madgraph"):
            process_name = process_name.replace("_madgraph", "")
        if process_name.endswith("_pythia8"):
            process_name = process_name.replace("_pythia8", "")
        if process_name.endswith("_mcfm"):
            process_name = process_name.replace("_mcfm", "")
        return process_name

    return ""


def print_progress_bar(current, total, width=30):
    if total <= 0:
        return

    fraction = current / total
    filled = int(width * fraction)
    bar = "#" * filled + "-" * (width - filled)
    percent = fraction * 100.0
    sys.stdout.write(f"\r[{bar}] {current}/{total} ({percent:5.1f}%)")
    sys.stdout.flush()


def format_progress_line(user, dataset_name, miniaod, new_dataset_name,
                         expected_events, found_events):
    return (
        f"{user} {dataset_name} {miniaod} {new_dataset_name} "
        f"{expected_events} {found_events}"
    )


def parse_assignment_list(value):
    if not value:
        return []
    return [part.strip().lower() for part in value.split(",") if part.strip()]


def assignment_matches(entry_assignment, requested_user):
    if not requested_user:
        return True
    requested = requested_user.strip().lower()
    tokens = parse_assignment_list(entry_assignment)
    return requested in tokens


PROCESS_GROUP_ORDER = ("top", "ewk", "qcd", "higgs", "data")

PROCESS_GROUP_KEYWORDS = {
    "top": (
        "tt",
        "tt+bb",
        "tt+bb DPS",
        "ttW",
        "Single Top",
        "ttZ",
        "tt(Wcb)",
        "tttt",
        "Rare top",
        "tt+bb syst",
        "tt(Wcb) syst",
    ),
    "ewk": (
        "W+jets",
        "Z+jets",
        "Diboson",
        "Triboson",
    ),
    "qcd": (
        "QCD",
        "multijet",
    ),
    "higgs": (
        "ttH(cc)",
        "ttH(bb)",
        "ttHNonbb",
        "VBFHToXX",
        "ggHToXX",
        "ZHToXX",
        "WplusHToXX",
        "WminusHToXX",
        "WH",
        "ZH",
        "VBFH",
        "ggH",
        "cHgg",
    ),
}


def classify_process_group(sample, sample_type="", miniaod=""):
    sample_text = normalize(sample).lower()
    sample_type_text = normalize(sample_type).lower()


    if sample_type_text == "data" or sample_text == "data":
        return "data"

    if sample_text in PROCESS_GROUP_ORDER:
        return sample_text

    mapping = find_mapping_by_sample_token(sample, miniaod=miniaod)
    if mapping and mapping["group"] in PROCESS_GROUP_ORDER:
        return mapping["group"]

    for group in ("higgs", "top", "ewk", "qcd"):
        for keyword in PROCESS_GROUP_KEYWORDS[group]:
            if keyword in sample:
                print(miniaod, sample, group)
                return group

    if sample_type_text in PROCESS_GROUP_ORDER:
        return sample_type_text

    return ""


def get_das_info_script_path():
    return Path(__file__).resolve().parent / "get_das_info.py"


def run_get_das_info(new_sample_name):
    cmd = ["python3", str(get_das_info_script_path()), "-d", new_sample_name]
    return subprocess.run(cmd, capture_output=True, text=True)


def comment_output_block(text):
    lines = text.splitlines()
    return "\n".join(f"# {line}" if line.strip() else "#" for line in lines)


def write_grouped_das_reports(entries, year, output_root=Path("customnano_v15"), min_fraction=0.0):
    output_root = Path(output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    output_paths = {group: output_root / f"{group}.txt" for group in PROCESS_GROUP_ORDER}
    for path in output_paths.values():
        path.write_text("", encoding="utf-8")

    grouped_counts = {group: 0 for group in PROCESS_GROUP_ORDER}
    skipped = []

    for entry in entries:
        miniaod = entry.get("miniaod", "")
        if not miniaod:
            continue

        if miniaod.endswith("/USER"):
            continue

        sample = entry.get("sample", "")
        mapping = find_mapping_by_sample_token(sample, miniaod=miniaod)
        sample_group = classify_process_group(
            sample,
            entry.get("type", ""),
            miniaod=miniaod,
        )
        if not sample_group:
            skipped.append(sample)
            continue

        new_sample_name = build_new_sample_names(
            miniaod,
            entry.get("type") or sample_group,
        )
        if not new_sample_name:
            new_sample_name = find_published_by_name(miniaod)

        if not new_sample_name:
            skipped.append(sample or miniaod)
            with open(output_paths[sample_group], "a", encoding="utf-8") as report:
                report.write(f"# not published: {miniaod}\n\n")
            continue

        completed = run_get_das_info(new_sample_name)

        new_dataset_name = build_new_dataset_name(
            miniaod,
            entry.get("type") or sample_group,
            sample=sample,
        )
        if not new_dataset_name:
            new_dataset_name = "PLACEHOLDER"

        process_name = infer_process_name(
            sample,
            miniaod=miniaod,
            sample_type=entry.get("type") or sample_group,
        )
        if not process_name or process_name == "placeholder":
            process_name = "PLACEHOLDER"

        # comment out unmapped samples, samples without a cmsdb process, and incomplete ones
        comment_block = mapping is None or process_name == "PLACEHOLDER"
        notes = []
        found_events = re.search(r"n_events=(\d+)", completed.stdout or "")
        expected_events = entry.get("events")
        if found_events and expected_events:
            found_events = int(found_events.group(1))
            if found_events < min_fraction * expected_events:
                comment_block = True
                notes.append(
                    f"# INCOMPLETE: {found_events} / {expected_events} events "
                    f"({100.0 * found_events / expected_events:.2f}%)",
                )
        if mapping is not None and process_name == "PLACEHOLDER":
            notes.append("# missing process in cmsdb")

        print(f"write in {output_paths[sample_group]}")
        with open(output_paths[sample_group], "a", encoding="utf-8") as report:
            for note in notes:
                report.write(note + "\n")
            if completed.stdout:
                output = completed.stdout
                output = output.replace(
                    'name="PLACEHOLDER',
                    f'name="{new_dataset_name}',
                )
                output = output.replace(
                    'processes=[procs.PLACEHOLDER]',
                    f'processes=[procs.{process_name}]',
                )
                if comment_block:
                    output = comment_output_block(output)
                report.write(output.rstrip() + "\n")
            else:
                report.write(f"# missing {miniaod}")
            report.write("\n")

        grouped_counts[sample_group] += 1

    return output_paths, grouped_counts, skipped

def download_spreadsheet(year, csv_path):
    url = SPREADSHEET_URLS.get(str(year))
    if not url:
        supported = ", ".join(sorted(SPREADSHEET_URLS.keys()))
        raise ValueError(
            f"No spreadsheet configured for year '{year}'. "
            f"Supported years: {supported}"
        )

    cmd = ["curl", "-L", "-sS", url, "-o", str(csv_path)]
    completed = subprocess.run(cmd, capture_output=True, text=True)
    if completed.returncode != 0:
        raise RuntimeError(
            "Failed to download spreadsheet.csv: "
            f"{completed.stderr.strip() or 'curl returned non-zero exit code'}"
        )


def run_dasgoclient_query(query):
    cmd = ["dasgoclient", "--query", query]
    completed = subprocess.run(cmd, capture_output=True, text=True)
    stdout_lines = [line.strip()
                    for line in completed.stdout.splitlines() if line.strip()]
    stderr = completed.stderr.strip()
    return completed.returncode, stdout_lines, stderr


def suggest_from_nano(nano_dataset):
    if not nano_dataset:
        return ""
    guess = nano_dataset.replace("/NANOAODSIM", "/MINIAODSIM")
    guess = guess.replace("/NANOAOD", "/MINIAOD")
    guess = guess.replace("NanoAOD", "MiniAOD")
    return guess

def print_report(total_checked, issues):
    print("\n=== Validation Summary ===")
    print(f"Checked NanoAOD datasets: {total_checked}")
    print(f"Issues found: {len(issues)}")

    if not issues:
        print("No missing or mismatched entries found.")
        return

    for idx, issue in enumerate(issues, start=1):
        print(f"\n[{idx}] {issue['type']}")
        print(f"  NanoAOD: {issue.get('nanoaod', '')}")
        if issue.get("expected_miniaod"):
            print(f"  MiniAOD in spreadsheet: {issue['expected_miniaod']}")
        if issue.get("found_parents"):
            print("  Parents found in DAS:")
            for parent in issue["found_parents"]:
                print(f"    - {parent}")
        if issue.get("suggested_miniaod"):
            print(
                "  Suggested MiniAOD to add/use: "
                f"{issue['suggested_miniaod']}"
            )
        if issue.get("details"):
            print(f"  Details: {issue['details']}")


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Download the spreadsheet for a year, build new CustomNanoAODv15 "
            "sample names, and write grouped DAS info into text files"
        )
    )
    parser.add_argument(
        "year",
        help=(
            "Year used to pick the spreadsheet and output filenames (e.g. 2024)"
        ),
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help=(
            "Directory that will contain the grouped text files. Defaults to customnano_v15"
        ),
    )
    parser.add_argument(
        "--csv",
        default=None,
        help="Use this local spreadsheet CSV instead of downloading the one for the year",
    )
    parser.add_argument(
        "--mapping",
        default=None,
        help=(
            "Sample -> dataset/process mapping file (columns: nano key, dataset name, "
            "process, optional group). Defaults to customnano_v15/utils/processes.txt"
        ),
    )
    parser.add_argument(
        "--types",
        nargs="+",
        default=None,
        help="Only consider spreadsheet rows of these types (e.g. MC Data)",
    )
    parser.add_argument(
        "--analysis",
        default=None,
        help="Only consider spreadsheet rows whose Analysis column contains this tag (e.g. tttt)",
    )
    parser.add_argument(
        "--min-fraction",
        type=float,
        default=0.0,
        help=(
            "Comment out datasets whose published n_events is below this fraction of the "
            "spreadsheet Events column (e.g. 1.0 to keep only fully processed samples)"
        ),
    )
    return parser.parse_args()


def main():
    global PROCESS_FILE
    args = parse_args()
    PROCESS_FILE = args.mapping

    if args.csv:
        csv_path = Path(args.csv)
    else:
        csv_path = Path("spreadsheet.csv")
        try:
            download_spreadsheet(args.year, csv_path)
        except (ValueError, RuntimeError) as err:
            print(f"ERROR: {err}", file=sys.stderr)
            sys.exit(1)

    if not csv_path.exists():
        print(f"ERROR: CSV file not found: {csv_path}", file=sys.stderr)
        sys.exit(1)

    entries = parse_spreadsheet(csv_path)
    if args.types:
        types = {t.lower() for t in args.types}
        entries = [e for e in entries if e["type"].lower() in types]
    if args.analysis:
        entries = [e for e in entries if assignment_matches(e["analysis"], args.analysis)]

    if os.system("which dasgoclient > /dev/null 2>&1") != 0:
        print(
            "ERROR: dasgoclient is not available in PATH. "
            "Install/setup DAS client first."
        )
        sys.exit(2)

    output_dir = Path(args.output_dir) if args.output_dir else Path("customnano_v15")
    output_paths, grouped_counts, skipped = write_grouped_das_reports(
        entries,
        year=args.year,
        output_root=output_dir,
        min_fraction=args.min_fraction,
    )

    print("Wrote grouped DAS reports:")
    for group in PROCESS_GROUP_ORDER:
        print(f"  {group}: {grouped_counts[group]} entries -> {output_paths[group]}")

    if skipped:
        print(f"Skipped {len(skipped)} entries without a recognized group or output name.")


if __name__ == "__main__":
    main()
