# coding: utf-8

"""
CMS datasets from the 2018 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_v9 import campaign_run2_2018_nano_v9 as cpn


cpn.add_dataset(
        name="data_mumu_a_PNET",
        id=143542070,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/2018/DoubleMuon/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_Run2018A-UL2018_MiniAODv2_GT36-v1", #noqa
        ],
        n_files=704,
        n_events=70931950,
        aux={
        "era": "A",
    },
    )

cpn.add_dataset(
        name="data_mumu_b_PNET",
        id=143477080,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/2018/DoubleMuon/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_Run2018B-UL2018_MiniAODv2_GT36-v1", #noqa
        ],
        n_files=319,
        n_events=32173507,
        aux={
        "era": "B",
    },
    )

cpn.add_dataset(
        name="data_mumu_c_PNET",
        id=143469260,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/2018/DoubleMuon/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_Run2018C-UL2018_MiniAODv2_GT36-v1", #noqa
        ],
        n_files=335,
        n_events=33794567,
        aux={
        "era": "C",
    },
    )

cpn.add_dataset(
        name="data_mumu_d_PNET",
        id=143726730,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/2018/DoubleMuon/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_Run2018D-UL2018_MiniAODv2_GT36-v1", #noqa
        ],
        n_files=1619,
        n_events=163374914,
        aux={
        "era": "D",
    },
    )

cpn.add_dataset(
        name="data_egamma_a_PNET",
        id=143786170,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/2018/EGamma/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_Run2018A-UL2018_MiniAODv2_GT36-v1", #noqa
        ],
        n_files=3286,
        n_events=319383937,
        aux={
        "era": "A",
    },
    )

cpn.add_dataset(
        name="data_egamma_b_PNET",
        id=144276950,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/2018/EGamma/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_Run2018B-UL2018_MiniAODv2_GT36-v1", #noqa
        ],
        n_files=1431,
        n_events=139144140,
        aux={
        "era": "B",
    },
    )

cpn.add_dataset(
        name="data_egamma_c_PNET",
        id=144066400,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/2018/EGamma/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_Run2018C-UL2018_MiniAODv2_GT36-v1", #noqa
        ],
        n_files=1477,
        n_events=143781609,
        aux={
        "era": "C",
    },
    )

cpn.add_dataset(
        name="data_egamma_d_PNET",
        id=142534100,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/2018/EGamma/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_Run2018D-UL2018_MiniAODv2_GT36-v2", #noqa
        ],
        n_files=7482,
        n_events=726731338,
        aux={
        "era": "D",
    },
    )

cpn.add_dataset(
        name="data_muoneg_a_PNET",
        id=143747010,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/2018/MuonEG/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_Run2018A-UL2018_MiniAODv2_GT36-v1", #noqa
        ],
        n_files=309,
        n_events=31248811,
        aux={
        "era": "A",
    },
    )

cpn.add_dataset(
        name="data_muoneg_b_PNET",
        id=143604930,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/2018/MuonEG/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_Run2018B-UL2018_MiniAODv2_GT36-v1", #noqa
        ],
        n_files=140,
        n_events=14447228,
        aux={
        "era": "B",
    },
    )

cpn.add_dataset(
        name="data_muoneg_c_PNET",
        id=143710680,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/2018/MuonEG/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_Run2018C-UL2018_MiniAODv2_GT36-v1", #noqa
        ],
        n_files=150,
        n_events=15363987,
        aux={
        "era": "C",
    },
    )

cpn.add_dataset(
        name="data_muoneg_d_PNET",
        id=143806030,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/2018/MuonEG/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_Run2018D-UL2018_MiniAODv2_GT36-v1", #noqa
        ],
        n_files=686,
        n_events=70190218,
        aux={
        "era": "D",
    },
    )

cpn.add_dataset(
        name="data_mu_a_PNET",
        id=143808070,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/2018/SingleMuon/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_Run2018A-UL2018_MiniAODv2_GT36-v2", #noqa
        ],
        n_files=2296,
        n_events=227474647,
        aux={
        "era": "A",
    },
    )

cpn.add_dataset(
        name="data_mu_b_PNET",
        id=143547070,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/2018/SingleMuon/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_Run2018B-UL2018_MiniAODv2_GT36-v2", #noqa
        ],
        n_files=1121,
        n_events=110446445,
        aux={
        "era": "B",
    },
    )

cpn.add_dataset(
        name="data_mu_c_PNET",
        id=143469950,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/2018/SingleMuon/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_Run2018C-UL2018_MiniAODv2_GT36-v3", #noqa
        ],
        n_files=1093,
        n_events=107972995,
        aux={
        "era": "C",
    },
    )

cpn.add_dataset(
        name="data_mu_d_PNET",
        id=143753270,
        is_data=True,
        processes=[procs.data],
        keys=[
            "/2018/SingleMuon/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_Run2018D-UL2018_MiniAODv2_GT36-v2", #noqa
        ],
        n_files=5067,
        n_events=500853680,
        aux={
        "era": "D",
    },
    )
