# coding: utf-8

"""
CMS datasets from the 2018 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_v9 import campaign_run2_2018_nano_v9 as cpn


cpn.add_dataset(
        name="data_mumu_a",
        id=14354207,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/DoubleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD", # TODO: GT36 to t2b, currently only at DESY or ipnl
        ],
        n_files=49,
        n_events=75499908,
        aux={
        "era": "A",
    },
    )

cpn.add_dataset(
        name="data_mumu_b",
        id=14347708,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/DoubleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD", # TODO: GT36 to t2b, currently only at DESY or ipnl
        ],
        n_files=18,
        n_events=35057758,
        aux={
        "era": "B",
    },
    )

cpn.add_dataset(
        name="data_mumu_c",
        id=14346926,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/DoubleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD",  # TODO: GT36 to t2b, currently only at DESY or ipnl
        ],
        n_files=31,
        n_events=34565869,
        aux={
        "era": "C",
    },
    )

cpn.add_dataset(
        name="data_mumu_d",
        id=14372673,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/DoubleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD", # TODO: GT36 to t2b, currently only at DESY or ipnl
        ],
        n_files=88,
        n_events=168620231,
        aux={
        "era": "D",
    },
    )

cpn.add_dataset(
        name="data_egamma_a",
        id=14378617,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/EGamma/Run2018A-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD",
        ],
        n_files=142,
        n_events=339013231,
        aux={
        "era": "A",
    },
    )

cpn.add_dataset(
        name="data_egamma_b",
        id=14427695,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/EGamma/Run2018B-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD",
        ],
        n_files=62,
        n_events=153822427,
        aux={
        "era": "B",
    },
    )

cpn.add_dataset(
        name="data_egamma_c",
        id=14406640,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/EGamma/Run2018C-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD",
        ],
        n_files=79,
        n_events=147827904,
        aux={
        "era": "C",
    },
    )

cpn.add_dataset(
        name="data_egamma_d",
        id=14253410,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/EGamma/Run2018D-UL2018_MiniAODv2_NanoAODv9-v3/NANOAOD",
        ],
        n_files=355,
        n_events=752524583,
        aux={
        "era": "D",
    },
    )

cpn.add_dataset(
        name="data_muoneg_a",
        id=14374701,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/MuonEG/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD", # TODO: GT36 to t2b
        ],
        n_files=32,
        n_events=32958503,
        aux={
        "era": "A",
    },
    )

cpn.add_dataset(
        name="data_muoneg_b",
        id=14360493,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/MuonEG/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD", # TODO: GT36 to t2b
        ],
        n_files=12,
        n_events=16204062,
        aux={
        "era": "B",
    },
    )

cpn.add_dataset(
        name="data_muoneg_c",
        id=14371068,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/MuonEG/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD", # TODO: GT36 to t2b
        ],
        n_files=14,
        n_events=15652198,
        aux={
        "era": "C",
    },
    )

cpn.add_dataset(
        name="data_muoneg_d",
        id=14380603,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/MuonEG/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD", # TODO: GT36 to t2b
        ],
        n_files=60,
        n_events=71947999,
        aux={
        "era": "D",
    },
    )

cpn.add_dataset(
        name="data_mu_a",
        id=14380807,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/SingleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD",
        ],
        n_files=94,
        n_events=241596817,
        aux={
        "era": "A",
    },
    )

cpn.add_dataset(
        name="data_mu_b",
        id=14354707,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/SingleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD",
        ],
        n_files=52,
        n_events=119918017,
        aux={
        "era": "B",
    },
    )

cpn.add_dataset(
        name="data_mu_c",
        id=14346995,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/SingleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD",
        ],
        n_files=67,
        n_events=110032072,
        aux={
        "era": "C",
    },
    )

cpn.add_dataset(
        name="data_mu_d",
        id=14375327,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/SingleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD",
        ],
        n_files=208,
        n_events=513884680,
        aux={
        "era": "D",
    },
    )
