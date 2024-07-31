# coding: utf-8

"""
CMS datasets from the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v11 import campaign_run3_2022_preEE_nano_v11 as cpn


#
# Muon
#

cpn.add_dataset(
    name="data_mu_c",
    id=14784127,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022C-22Sep2023-v1/NANOAOD",
    ],
    n_files=124,
    n_events=138427345,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_d",
    id=14783357,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022D-22Sep2023-v1/NANOAOD",
    ],
    n_files=82,
    n_events=75468381,
    aux={
        "era": "D",
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
        "/EGamma/Run2022C-22Sep2023-v1/NANOAOD",
    ],
    n_files=313,
    n_events=263689151,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_egamma_d",
    id=14783299,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022D-22Sep2023-v1/NANOAOD",
    ],
    n_files=109,
    n_events=89134996,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_muoneg_c",
    id=14784125,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/Run2022C-22Sep2023-v1/NANOAOD",
    ],
    n_files=28,
    n_events=15768439,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_muoneg_d",
    id=14784209,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/Run2022D-22Sep2023-v1/NANOAOD",
    ],
    n_files=16,
    n_events=8007031,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_mumu_c",
    id=14784138,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/DoubleMuon/Run2022C-22Sep2023-v1/NANOAOD",
    ],
    n_files=12,
    n_events=4646904,
    aux={
        "era": "C",
    },
)
