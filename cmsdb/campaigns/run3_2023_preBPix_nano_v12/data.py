# coding: utf-8

"""
CMS datasets from the 2023 pre-BPix data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn

#
# Muon
#

cpn.add_dataset(
    name="data_mu0_c_v1",
    id=14787055,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=90,
    n_events=54715896,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_mu1_c_v1",
    id=14786107,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon1/Run2023C-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=73,
    n_events=54698315,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_mu0_c_v2",
    id=14787019,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=31,
    n_events=17063451,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_mu1_c_v2",
    id=14787021,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon1/Run2023C-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=33,
    n_events=17059895,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_mu0_c_v3",
    id=14787140,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v3-v1/NANOAOD",  # noqa
    ],
    n_files=42,
    n_events=20015377,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_mu1_c_v3",
    id=14787090,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon1/Run2023C-22Sep2023_v3-v1/NANOAOD",  # noqa
    ],
    n_files=30,
    n_events=20010429,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_mu0_c_v4",
    id=14786982,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=165,
    n_events=138943783,
    aux={
        "era": "C",
        "jec_era": "RunCv4",
    },
)

cpn.add_dataset(
    name="data_mu1_c_v4",
    id=14787027,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon1/Run2023C-22Sep2023_v4-v2/NANOAOD",  # noqa
    ],
    n_files=108,
    n_events=101615754,
    aux={
        "era": "C",
        "jec_era": "RunCv4",
    },
)

#
# MuonEG
#

cpn.add_dataset(
    name="data_muoneg_c_v1",
    id=14784846,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2023C-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=25,
    n_events=9772655,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_muoneg_c_v2",
    id=14787041,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2023C-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=8,
    n_events=2735170,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_muoneg_c_v3",
    id=14784883,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2023C-22Sep2023_v3-v1/NANOAOD",  # noqa
    ],
    n_files=11,
    n_events=3502967,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_muoneg_c_v4",
    id=14784848,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=41,
    n_events=24205121,
    aux={
        "era": "C",
        "jec_era": "RunCv4",
    },
)

#
# E/Gamma
#

cpn.add_dataset(
    name="data_egamma0_c_v1",
    id=14786980,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=90,
    n_events=67598081,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_egamma1_c_v1",
    id=14786912,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma1/Run2023C-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=71,
    n_events=67582665,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_egamma0_c_v2",
    id=14787633,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=22,
    n_events=17233307,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_egamma1_c_v2",
    id=14787073,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma1/Run2023C-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=24,
    n_events=17230822,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_egamma0_c_v3",
    id=14787548,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v3-v1/NANOAOD",  # noqa
    ],
    n_files=26,
    n_events=21993048,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_egamma1_c_v3",
    id=14786975,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma1/Run2023C-22Sep2023_v3-v1/NANOAOD",  # noqa
    ],
    n_files=25,
    n_events=21987586,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_egamma0_c_v4",
    id=14786977,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=168,
    n_events=160108119,
    aux={
        "era": "C",
        "jec_era": "RunCv4",
    },
)

cpn.add_dataset(
    name="data_egamma1_c_v4",
    id=14786782,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma1/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=177,
    n_events=160049621,
    aux={
        "era": "C",
        "jec_era": "RunCv4",
    },
)
