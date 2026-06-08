# coding: utf-8

"""
data datasets for the 2024 data-taking campaign
"""

from order import DatasetInfo
import cmsdb.processes as procs

from cmsdb.campaigns.run3_2024_customnano_v15 import campaign_run3_2024_customnano_v15 as cpn

cpn.add_dataset(
    name="data_muon0_c",
    id=3372666,
    processes=[procs.data],
    keys=[
        "/Muon0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024C-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=695,
    n_events=68069710,
)

cpn.add_dataset(
    name="data_muon0_d",
    id=3372653,
    processes=[procs.data],
    keys=[
        "/Muon0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024D-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=581,
    n_events=56446727,
)

cpn.add_dataset(
    name="data_muon0_e",
    id=3372681,
    processes=[procs.data],
    keys=[
        "/Muon0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024E-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=688,
    n_events=66879609,
)

cpn.add_dataset(
    name="data_muon0_f",
    id=3372658,
    processes=[procs.data],
    keys=[
        "/Muon0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024F-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1268,
    n_events=123058960,
)

cpn.add_dataset(
    name="data_muon0_g",
    id=3371521,
    processes=[procs.data],
    keys=[
        "/Muon0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024G-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=9964,
    n_events=965903658,
)

cpn.add_dataset(
    name="data_muon0_h",
    id=3371539,
    processes=[procs.data],
    keys=[
        "/Muon0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024H-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=243,
    n_events=23584916,
)

cpn.add_dataset(
    name="data_muon0_i",
    id=3371614,
    processes=[procs.data],
    keys=[
        "/Muon0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024I-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=188,
    n_events=18253507,
)

cpn.add_dataset(
    name="data_muon1_c",
    id=3370523,
    processes=[procs.data],
    keys=[
        "/Muon1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024C-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1005,
    n_events=97481556,
)

cpn.add_dataset(
    name="data_muon1_d",
    id=3370575,
    processes=[procs.data],
    keys=[
        "/Muon1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024D-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=963,
    n_events=93653103,
)

cpn.add_dataset(
    name="data_muon1_e",
    id=3370570,
    processes=[procs.data],
    keys=[
        "/Muon1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024E-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1781,
    n_events=172848674,
)

cpn.add_dataset(
    name="data_muon1_f",
    id=3370557,
    processes=[procs.data],
    keys=[
        "/Muon1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024F-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=4556,
    n_events=442287452,
)

cpn.add_dataset(
    name="data_muon1_g",
    id=3370568,
    processes=[procs.data],
    keys=[
        "/Muon1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024G-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=6606,
    n_events=641695857,
)

cpn.add_dataset(
    name="data_muon1_h",
    id=3370551,
    processes=[procs.data],
    keys=[
        "/Muon1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024H-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=965,
    n_events=93981102,
)

cpn.add_dataset(
    name="data_muon1_i",
    id=3370561,
    processes=[procs.data],
    keys=[
        "/Muon1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024I-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1013,
    n_events=97435749,
)

cpn.add_dataset(
    name="data_muoneg_c",
    id=3372079,
    processes=[procs.data],
    keys=[
        "/MuonEG/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024C-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=184,
    n_events=18312408,
)

cpn.add_dataset(
    name="data_muoneg_d",
    id=3372048,
    processes=[procs.data],
    keys=[
        "/MuonEG/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024D-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=182,
    n_events=18031311,
)

cpn.add_dataset(
    name="data_muoneg_e",
    id=3372098,
    processes=[procs.data],
    keys=[
        "/MuonEG/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024E-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=265,
    n_events=26319233,
)

cpn.add_dataset(
    name="data_muoneg_f",
    id=3372083,
    processes=[procs.data],
    keys=[
        "/MuonEG/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024F-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=677,
    n_events=67341687,
)

cpn.add_dataset(
    name="data_muoneg_g",
    id=3372061,
    processes=[procs.data],
    keys=[
        "/MuonEG/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024G-MINIv6NANOv15-v3-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=966,
    n_events=95992626,
)

cpn.add_dataset(
    name="data_muoneg_h",
    id=3372005,
    processes=[procs.data],
    keys=[
        "/MuonEG/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024H-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=141,
    n_events=14027028,
)

cpn.add_dataset(
    name="data_muoneg_i",
    id=3372024,
    processes=[procs.data],
    keys=[
        "/MuonEG/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024I-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=147,
    n_events=14579063,
)

cpn.add_dataset(
    name="data_egamma0_c",
    id=3371572,
    processes=[procs.data],
    keys=[
        "/EGamma0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024C-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1631,
    n_events=157378917,
)

cpn.add_dataset(
    name="data_egamma0_d",
    id=3371573,
    processes=[procs.data],
    keys=[
        "/EGamma0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024D-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1622,
    n_events=156460481,
)

cpn.add_dataset(
    name="data_egamma0_e",
    id=3371546,
    processes=[procs.data],
    keys=[
        "/EGamma0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024E-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2606,
    n_events=249348576,
)

cpn.add_dataset(
    name="data_egamma0_f",
    id=3371547,
    processes=[procs.data],
    keys=[
        "/EGamma0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024F-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=6612,
    n_events=632256445,
)

cpn.add_dataset(
    name="data_egamma0_g",
    id=3371567,
    processes=[procs.data],
    keys=[
        "/EGamma0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024G-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=9471,
    n_events=903112709,
)

cpn.add_dataset(
    name="data_egamma0_h",
    id=3371583,
    processes=[procs.data],
    keys=[
        "/EGamma0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024H-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1414,
    n_events=134680448,
)

cpn.add_dataset(
    name="data_egamma0_i",
    id=3371586,
    processes=[procs.data],
    keys=[
        "/EGamma0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024I-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1392,
    n_events=132904290,
)

cpn.add_dataset(
    name="data_egamma1_c",
    id=3372058,
    processes=[procs.data],
    keys=[
        "/EGamma1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024C-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1635,
    n_events=157841358,
)

cpn.add_dataset(
    name="data_egamma1_d",
    id=3372069,
    processes=[procs.data],
    keys=[
        "/EGamma1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024D-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1604,
    n_events=154737779,
)

cpn.add_dataset(
    name="data_egamma1_e",
    id=3372057,
    processes=[procs.data],
    keys=[
        "/EGamma1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024E-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1912,
    n_events=183250048,
)

cpn.add_dataset(
    name="data_egamma1_f",
    id=3372077,
    processes=[procs.data],
    keys=[
        "/EGamma1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024F-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=6385,
    n_events=610697584,
)

cpn.add_dataset(
    name="data_egamma1_g",
    id=3372070,
    processes=[procs.data],
    keys=[
        "/EGamma1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024G-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=8117,
    n_events=773417123,
)

cpn.add_dataset(
    name="data_egamma1_h",
    id=3372060,
    processes=[procs.data],
    keys=[
        "/EGamma1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024H-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1385,
    n_events=131849721,
)

cpn.add_dataset(
    name="data_egamma1_i",
    id=3372064,
    processes=[procs.data],
    keys=[
        "/EGamma1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024I-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1374,
    n_events=131561563,
)

# cpn.add_dataset(
#     name="data_jetmet0_c",
#     id=3371589,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/JetMET0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024C-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=705,
#     n_events=69348871,
# )
#

# cpn.add_dataset(
#     name="data_jetmet0_d",
#     id=3371565,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/JetMET0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024D-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=773,
#     n_events=75911377,
# )
#

# cpn.add_dataset(
#     name="data_jetmet0_e",
#     id=3371616,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/JetMET0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024E-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1264,
#     n_events=123673375,
# )
#

# cpn.add_dataset(
#     name="data_jetmet0_f",
#     id=3371517,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/JetMET0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024F-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=3167,
#     n_events=309079689,
# )
#

# cpn.add_dataset(
#     name="data_jetmet0_g",
#     id=3371610,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/JetMET0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024G-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=2254,
#     n_events=220340093,
# )
#

# cpn.add_dataset(
#     name="data_jetmet0_h",
#     id=3371559,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/JetMET0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024H-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=548,
#     n_events=53636159,
# )
#

# cpn.add_dataset(
#     name="data_jetmet0_i",
#     id=3371617,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/JetMET0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024I-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=578,
#     n_events=56541702,
# )
#

# cpn.add_dataset(
#     name="data_jetmet1_c",
#     id=3371623,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/JetMET1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024C-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=689,
#     n_events=67782994,
# )
#

# cpn.add_dataset(
#     name="data_jetmet1_d",
#     id=3371575,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/JetMET1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024D-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=753,
#     n_events=73956332,
# )
#

# cpn.add_dataset(
#     name="data_jetmet1_e",
#     id=3371558,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/JetMET1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024E-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=378,
#     n_events=37008371,
# )
#

# cpn.add_dataset(
#     name="data_jetmet1_f",
#     id=3371578,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/JetMET1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024F-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=2936,
#     n_events=286691411,
# )
#

# cpn.add_dataset(
#     name="data_jetmet1_g",
#     id=3371570,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/JetMET1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024G-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=3821,
#     n_events=373637674,
# )
#

# cpn.add_dataset(
#     name="data_jetmet1_h",
#     id=3371954,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/JetMET1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024H-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=117,
#     n_events=11491798,
# )
#

# cpn.add_dataset(
#     name="data_jetmet1_i",
#     id=3371564,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/JetMET1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024I-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1089,
#     n_events=106317879,
# )
#

# cpn.add_dataset(
#     name="data_parkinghh_c",
#     id=3371985,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/ParkingHH/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024C-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=988,
#     n_events=96434885,
# )
#

# cpn.add_dataset(
#     name="data_parkinghh_d",
#     id=3371966,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/ParkingHH/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024D-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=722,
#     n_events=69842034,
# )
#

# cpn.add_dataset(
#     name="data_parkinghh_e",
#     id=3371910,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/ParkingHH/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024E-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=195,
#     n_events=18903311,
# )
#

# cpn.add_dataset(
#     name="data_parkinghh_f",
#     id=3371874,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/ParkingHH/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024F-MINIv6NANOv15-v4-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=4988,
#     n_events=479362077,
# )
#

# cpn.add_dataset(
#     name="data_parkinghh_g",
#     id=3371936,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/ParkingHH/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024G-MINIv6NANOv15-v3-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1337,
#     n_events=128771337,
# )
#

# cpn.add_dataset(
#     name="data_parkinghh_h",
#     id=3371951,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/ParkingHH/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024H-MINIv6NANOv15-v3-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1007,
#     n_events=97064942,
# )
#

# cpn.add_dataset(
#     name="data_parkinghh_i",
#     id=3371927,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/ParkingHH/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024I-MINIv6NANOv15-v3-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1075,
#     n_events=103577087,
# )
#
