# coding: utf-8

"""
CMS datasets from the 2022 pre-EE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn


#
# Muon
#

cpn.add_dataset(
    name="data_mu_c",
    id=14784127,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022C-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=124,
    n_events=138427345,
    aux={
        "era": "C",
        "jec_era": "RunCD",
    },
)

cpn.add_dataset(
    name="data_singlemu_c",
    id=14784104,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022C-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=35,
    n_events=20162441,
    aux={
        "era": "C",
        "jec_era": "RunCD",
    },
)

cpn.add_dataset(
    name="data_doublemu_c",
    id=14784138,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/DoubleMuon/Run2022C-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=12,
    n_events=4646904,
    aux={
        "era": "C",
        "jec_era": "RunCD",
    },
)

cpn.add_dataset(
    name="data_mu_d",
    id=14783357,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022D-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=82,
    n_events=75468381,
    aux={
        "era": "D",
        "jec_era": "RunCD",
    },
)


#
# E/Gamma
#

cpn.add_dataset(
    name="data_egamma_c",
    id=14784140,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022C-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=313,
    n_events=263689151,
    aux={
        "era": "C",
        "jec_era": "RunCD",
    },
)

cpn.add_dataset(
    name="data_egamma_d",
    id=14783299,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022D-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=109,
    n_events=89134996,
    aux={
        "era": "D",
        "jec_era": "RunCD",
    },
)


#
# MuonEG
#


cpn.add_dataset(
    name="data_muoneg_a",
    id=14783289,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022A-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=5,
    n_events=12,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_muoneg_b",
    id=14784076,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022B-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=7,
    n_events=254803,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_muoneg_c",
    id=14784125,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022C-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=28,
    n_events=15768439,
    aux={
        "era": "C",
        "jec_era": "RunCD",
    },
)

cpn.add_dataset(
    name="data_muoneg_d",
    id=14784209,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022D-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=16,
    n_events=8007031,
    aux={
        "era": "D",
        "jec_era": "RunCD",
    },
)

cpn.add_dataset(
    name="data_jetmet_c",
    id=14784135,
    is_data=True,
    processes=[procs.data_jetmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET/Run2022C-22Sep2023-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=206,
            n_events=169187457,
        ),
    ),
    aux={
        "era": "C",
        "jec_era": "RunCD",
    },
)

cpn.add_dataset(
    name="data_jetmet_d",
    id=14809508,
    is_data=True,
    processes=[procs.data_jetmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET/Run2022D-22Sep2023-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=100,
            n_events=100853361,
        ),
    ),
    aux={
        "era": "D",
    },
)
