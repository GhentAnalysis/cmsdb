# coding: utf-8

"""
CMS datasets from the 2023 post-BPix data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_v12 import campaign_run3_2023_postBPix_nano_v12 as cpn

#
# Muon
#

cpn.add_dataset(
    name="data_mu0_d_v1",
    id=14787767,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023D-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=125,
    n_events=100291308,
    aux={
        "era": "D",
        "jec_era": "RunD",
    },
)

cpn.add_dataset(
    name="data_mu1_d_v1",
    id=14787545,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon1/Run2023D-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=100,
    n_events=100281976,
    aux={
        "era": "D",
        "jec_era": "RunD",
    },
)

cpn.add_dataset(
    name="data_mu0_d_v2",
    id=14787686,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=32,
    n_events=21462916,
    aux={
        "era": "D",
        "jec_era": "RunD",
    },
)

cpn.add_dataset(
    name="data_mu1_d_v2",
    id=14786997,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon1/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=30,
    n_events=21463645,
    aux={
        "era": "D",
        "jec_era": "RunD",
    },
)

#
# MuonEG
#

cpn.add_dataset(
    name="data_muoneg_d_v1",
    id=14787219,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2023D-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=32,
    n_events=17530531,
    aux={
        "era": "D",
        "jec_era": "RunD",
    },
)

cpn.add_dataset(
    name="data_muoneg_d_v2",
    id=14787200,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=11,
    n_events=3751587,
    aux={
        "era": "D",
        "jec_era": "RunD",
    },
)

#
# E/Gamma
#

cpn.add_dataset(
    name="data_egamma0_d_v1",
    id=14786984,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023D-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=124,
    n_events=105892646,
    aux={
        "era": "D",
        "jec_era": "RunD",
    },
)

cpn.add_dataset(
    name="data_egamma1_d_v1",
    id=14786912,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma1/Run2023C-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=71,
    n_events=67582665,
    aux={
        "era": "D",
        "jec_era": "RunD",
    },
)

cpn.add_dataset(
    name="data_egamma0_d_v2",
    id=14787876,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=33,
    n_events=22657211,
    aux={
        "era": "D",
        "jec_era": "RunD",
    },
)

cpn.add_dataset(
    name="data_egamma1_d_v2",
    id=14785166,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma1/Run2023C-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=30,
    n_events=22653287,
    aux={
        "era": "D",
        "jec_era": "RunD",
    },
)
