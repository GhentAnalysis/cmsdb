# coding: utf-8

"""
data datasets for the 2024 data-taking campaign
"""

import cmsdb.processes as procs

from cmsdb.campaigns.run3_2024_customnano_v15 import campaign_run3_2024_customnano_v15 as cpn

cpn.add_dataset(
    name="data_muon0_c",
    id=3372666,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024C-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=997,
    n_events=97505587,
)

cpn.add_dataset(
    name="data_muon0_d",
    id=3372653,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024D-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1243,
    n_events=120787065,
)

cpn.add_dataset(
    name="data_muon0_e",
    id=3372681,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024E-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1748,
    n_events=169640946,
)

cpn.add_dataset(
    name="data_muon0_f",
    id=3372658,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024F-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=4558,
    n_events=442432787,
)

cpn.add_dataset(
    name="data_muon0_g",
    id=3371521,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024G-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=6622,
    n_events=642028803,
)

cpn.add_dataset(
    name="data_muon0_h",
    id=3371539,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024H-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=969,
    n_events=93983627,
)

cpn.add_dataset(
    name="data_muon0_i",
    id=3371614,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024I-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1014,
    n_events=97634104,
)

cpn.add_dataset(
    name="data_muon1_c",
    id=3370523,
    is_data=True,
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
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024D-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1238,
    n_events=120415086,
)

cpn.add_dataset(
    name="data_muon1_e",
    id=3370570,
    is_data=True,
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
    is_data=True,
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
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024G-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=6608,
    n_events=641891857,
)

cpn.add_dataset(
    name="data_muon1_h",
    id=3370551,
    is_data=True,
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
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024I-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1015,
    n_events=97630010,
)

cpn.add_dataset(
    name="data_muoneg_c",
    id=3372079,
    is_data=True,
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
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024D-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=190,
    n_events=18827708,
)

cpn.add_dataset(
    name="data_muoneg_e",
    id=3372098,
    is_data=True,
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
    is_data=True,
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
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024G-MINIv6NANOv15-v3-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=986,
    n_events=97985222,
)

cpn.add_dataset(
    name="data_muoneg_h",
    id=3372005,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024H-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=144,
    n_events=14323522,
)

cpn.add_dataset(
    name="data_muoneg_i",
    id=3372024,
    is_data=True,
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
    is_data=True,
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
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024D-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1623,
    n_events=156558757,
)

cpn.add_dataset(
    name="data_egamma0_e",
    id=3371546,
    is_data=True,
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
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024F-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=6694,
    n_events=638973884,
)

cpn.add_dataset(
    name="data_egamma0_g",
    id=3371567,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024G-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=9473,
    n_events=903260423,
)

cpn.add_dataset(
    name="data_egamma0_h",
    id=3371583,
    is_data=True,
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
    is_data=True,
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
    is_data=True,
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
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024D-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1620,
    n_events=156275778,
)

cpn.add_dataset(
    name="data_egamma1_e",
    id=3372057,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024E-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2603,
    n_events=249377273,
)

cpn.add_dataset(
    name="data_egamma1_f",
    id=3372077,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024F-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=6597,
    n_events=631018208,
)

cpn.add_dataset(
    name="data_egamma1_g",
    id=3372070,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024G-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=9469,
    n_events=903246278,
)

cpn.add_dataset(
    name="data_egamma1_h",
    id=3372060,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024H-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1416,
    n_events=134835799,
)

cpn.add_dataset(
    name="data_egamma1_i",
    id=3372064,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024I-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1388,
    n_events=132903874,
)

cpn.add_dataset(
    name="data_jetmet0_c",
    id=3371589,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024C-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=705,
    n_events=69348871,
)


cpn.add_dataset(
    name="data_jetmet0_d",
    id=3388623,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024D-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=773,
    n_events=75911377,
)


cpn.add_dataset(
    name="data_jetmet0_e",
    id=3371616,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024E-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1264,
    n_events=123673375,
)


cpn.add_dataset(
    name="data_jetmet0_f",
    id=3371517,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET0/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024F-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=3167,
    n_events=309079689,
)


cpn.add_dataset(
    name="data_jetmet0_g",
    id=3371610,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024G-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=4102,
    n_events=400931856,
)


cpn.add_dataset(
    name="data_jetmet0_h",
    id=3371559,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024H-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=570,
    n_events=55794457,
)


cpn.add_dataset(
    name="data_jetmet0_i",
    id=3371617,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024I-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=606,
    n_events=59259348,
)


cpn.add_dataset(
    name="data_jetmet1_c",
    id=3371623,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024C-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=708,
    n_events=69648563,
)


cpn.add_dataset(
    name="data_jetmet1_d",
    id=3371575,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024D-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=772,
    n_events=75810110,
)


cpn.add_dataset(
    name="data_jetmet1_e",
    id=3371558,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024E-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1274,
    n_events=123347987,
)


cpn.add_dataset(
    name="data_jetmet1_f",
    id=3371578,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024F-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=3170,
    n_events=309469683,
)


cpn.add_dataset(
    name="data_jetmet1_g",
    id=3371570,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024G-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=4033,
    n_events=394355975,
)


cpn.add_dataset(
    name="data_jetmet1_h",
    id=3371954,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024H-MINIv6NANOv15-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=525,
    n_events=51368685,
)


cpn.add_dataset(
    name="data_jetmet1_i",
    id=3371564,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024I-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=607,
    n_events=59255632,
)


cpn.add_dataset(
    name="data_parkinghh_c",
    id=3371985,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024C-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1077,
    n_events=105158321,
)


cpn.add_dataset(
    name="data_parkinghh_d",
    id=3371966,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024D-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1299,
    n_events=125986310,
)


cpn.add_dataset(
    name="data_parkinghh_e",
    id=3371910,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024E-MINIv6NANOv15-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1835,
    n_events=177935339,
)


cpn.add_dataset(
    name="data_parkinghh_f",
    id=3371874,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024F-MINIv6NANOv15-v4-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=5065,
    n_events=486729639,
)


cpn.add_dataset(
    name="data_parkinghh_g",
    id=3371936,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024G-MINIv6NANOv15-v3-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=7383,
    n_events=709609093,
)


cpn.add_dataset(
    name="data_parkinghh_h",
    id=3371951,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024H-MINIv6NANOv15-v3-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1033,
    n_events=99559443,
)


cpn.add_dataset(
    name="data_parkinghh_i",
    id=3371927,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2024I-MINIv6NANOv15-v3-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1075,
    n_events=103577087,
)
