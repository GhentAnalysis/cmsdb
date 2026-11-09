# coding: utf-8

"""
data datasets for the 2018 data-taking campaign (custom NanoAODv15)
"""

import cmsdb.processes as procs

from cmsdb.campaigns.run2_2018_customnano_v15 import campaign_run2_2018_customnano_v15 as cpn

#
# DoubleMuon
#

cpn.add_dataset(
    name="data_doublemu_a",
    id=3395894,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/DoubleMuon/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018A-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=761,
    n_events=75499908,
)

cpn.add_dataset(
    name="data_doublemu_b",
    id=3395003,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/DoubleMuon/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018B-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=353,
    n_events=35057758,
)

cpn.add_dataset(
    name="data_doublemu_c",
    id=3395885,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/DoubleMuon/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018C-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=348,
    n_events=34565869,
)

# NOTE: complete; equals the valid MiniAOD parent. The sheet value (168620231) includes 1 MiniAOD file
# invalidated in DBS (100178 events, runs 322179, 322252, 323976)
cpn.add_dataset(
    name="data_doublemu_d",
    id=3395876,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/DoubleMuon/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018D-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1698,
    n_events=168520053,
)

#
# SingleMuon
#

# NOTE: all 61131 lumis of the valid MiniAOD parent, identical to the central NanoAODv15 (241600265 events);
# 5292 below the DBS event count of the MiniAOD parent (241605557), cause not identified. The sheet value
# (241596817) is from the NanoAODv9_GT36-v1 dataset, made from a different MiniAOD version (GT36-v1)
cpn.add_dataset(
    name="data_singlemu_a",
    id=3396354,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleMuon/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018A-UL2018_MiniAODv2_GT36-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2472,
    n_events=241600265,
)

cpn.add_dataset(
    name="data_singlemu_b",
    id=3396185,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleMuon/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018B-UL2018_MiniAODv2_GT36-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1228,
    n_events=119918017,
)

cpn.add_dataset(
    name="data_singlemu_c",
    id=3396194,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleMuon/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018C-UL2018_MiniAODv2_GT36-v3-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1126,
    n_events=110032072,
)

cpn.add_dataset(
    name="data_singlemu_d",
    id=3396193,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleMuon/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018D-UL2018_MiniAODv2_GT36-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=5255,
    n_events=513884680,
)

#
# EGamma
#

cpn.add_dataset(
    name="data_egamma_a",
    id=3395844,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018A-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=3507,
    n_events=339013231,
)

cpn.add_dataset(
    name="data_egamma_b",
    id=3396351,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018B-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1588,
    n_events=153822427,
)

cpn.add_dataset(
    name="data_egamma_c",
    id=3396036,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018C-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1524,
    n_events=147827904,
)

# NOTE: 181745 events (273 LS) short of the valid MiniAOD parent (751108801): runs 320500 (all 80 LS) and 320569
# (193 LS), none of them golden; documented in /user/tmohr/public_html/unprocessed_customV15_EGamma2018D/
# (the sheet value 752061412 also counts invalidated MiniAOD files)
cpn.add_dataset(
    name="data_egamma_d",
    id=3396040,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018D-UL2018_MiniAODv2_GT36-v3-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=7758,
    n_events=750927056,
)

#
# MuonEG
#

cpn.add_dataset(
    name="data_muoneg_a",
    id=3396059,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018A-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=331,
    n_events=32958503,
)

cpn.add_dataset(
    name="data_muoneg_b",
    id=3395976,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018B-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=163,
    n_events=16204062,
)

cpn.add_dataset(
    name="data_muoneg_c",
    id=3395950,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018C-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=158,
    n_events=15652198,
)

cpn.add_dataset(
    name="data_muoneg_d",
    id=3397005,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018D-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=722,
    n_events=71947999,
)

#
# JetHT and MET: not completely processed yet, commented out
#
# JetHT
#

# NOTE: 171402440 / 171492206 events in the production sheet (99.95%)
# cpn.add_dataset(
#     name="data_jetht_a",
#     id=3395902,
#     is_data=True,
#     processes=[procs.data],
#     keys=[
#         "/JetHT/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018A-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1744,
#     n_events=171402440,
# )

# cpn.add_dataset(
#     name="data_jetht_b",
#     id=3395907,
#     is_data=True,
#     processes=[procs.data],
#     keys=[
#         "/JetHT/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018B-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=794,
#     n_events=78253065,
# )

# cpn.add_dataset(
#     name="data_jetht_c",
#     id=3395881,
#     is_data=True,
#     processes=[procs.data],
#     keys=[
#         "/JetHT/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018C-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=714,
#     n_events=70027804,
# )

# NOTE: 352934804 / 355774350 events in the production sheet (99.20%)
# cpn.add_dataset(
#     name="data_jetht_d",
#     id=3395905,
#     is_data=True,
#     processes=[procs.data],
#     keys=[
#         "/JetHT/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018D-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=3584,
#     n_events=352934804,
# )

#
# MET
#

# cpn.add_dataset(
#     name="data_met_a",
#     id=3395889,
#     is_data=True,
#     processes=[procs.data],
#     keys=[
#         "/MET/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018A-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=531,
#     n_events=52759851,
# )

# cpn.add_dataset(
#     name="data_met_b",
#     id=3395887,
#     is_data=True,
#     processes=[procs.data],
#     keys=[
#         "/MET/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018B-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=299,
#     n_events=29714277,
# )

# cpn.add_dataset(
#     name="data_met_c",
#     id=3395850,
#     is_data=True,
#     processes=[procs.data],
#     keys=[
#         "/MET/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018C-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=317,
#     n_events=31144738,
# )

# NOTE: 159344383 / 160411782 events in the production sheet (99.33%)
# cpn.add_dataset(
#     name="data_met_d",
#     id=3395895,
#     is_data=True,
#     processes=[procs.data],
#     keys=[
#         "/MET/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2018D-UL2018_MiniAODv2_GT36-v1-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1607,
#     n_events=159344383,
# )
