# coding: utf-8

"""
Electroweak datasets for the 2024 data-taking campaign
"""
from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_customnano_v15 import campaign_run3_2024_customnano_v15 as cpn
# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3371660,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/Wto2Q-2Jets_Bin-PTQQ-100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v3-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=6372,
#     n_events=377842325,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3371631,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/Wto2Q-2Jets_Bin-PTQQ-200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=2535,
#     n_events=154307921,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3371544,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/Wto2Q-2Jets_Bin-PTQQ-400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v3-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=916,
#     n_events=47423661,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3371653,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/Wto2Q-2Jets_Bin-PTQQ-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1070,
#     n_events=51483908,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=3371540,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/Wto2Q-3Jets_Bin-HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=4651,
#     n_events=384703157,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=3371576,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/Wto2Q-3Jets_Bin-HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=6761,
#     n_events=401294004,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=3371506,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/Wto2Q-3Jets_Bin-HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1081,
#     n_events=53389988,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=3371551,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/Wto2Q-3Jets_Bin-HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v3-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1020,
#     n_events=46694923,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=3371545,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/Wto2Q-3Jets_Bin-HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1224,
#     n_events=52106542,
# )
#

cpn.add_dataset(
    name="w_lnu_j1_pt40to100_amcatnlo",
    id=3371622,
    processes=[procs.w_lnu_j1_pt40to100],
    keys=[
        "/WtoLNu-2Jets_Bin-1J-PTLNu-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v3-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=6250,
    n_events=446357793,
)

cpn.add_dataset(
    name="w_lnu_j1_pt100to200_amcatnlo",
    id=3371647,
    processes=[procs.w_lnu_j1_pt100to200],
    keys=[
        "/WtoLNu-2Jets_Bin-1J-PTLNu-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v3-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=7059,
    n_events=493719086,
)

cpn.add_dataset(
    name="w_lnu_j1_pt200to400_amcatnlo",
    id=3371761,
    processes=[procs.w_lnu_j1_pt200to400],
    keys=[
        "/WtoLNu-2Jets_Bin-1J-PTLNu-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=526,
    n_events=44967803,
)

cpn.add_dataset(
    name="w_lnu_j1_pt400to600_amcatnlo",
    id=3371556,
    processes=[procs.w_lnu_j1_pt400to600],
    keys=[
        "/WtoLNu-2Jets_Bin-1J-PTLNu-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=174,
    n_events=14159808,
)

cpn.add_dataset(
    name="w_lnu_j1_pt600_amcatnlo",
    id=3371649,
    processes=[procs.w_lnu_j1_pt600],
    keys=[
        "/WtoLNu-2Jets_Bin-1J-PTLNu-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=177,
    n_events=15305397,
)

cpn.add_dataset(
    name="w_lnu_j2_pt40to100_amcatnlo",
    id=3371606,
    processes=[procs.w_lnu_j2_pt40to100],
    keys=[
        "/WtoLNu-2Jets_Bin-2J-PTLNu-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v3-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=7098,
    n_events=483113802,
)

cpn.add_dataset(
    name="w_lnu_j2_pt100to200_amcatnlo",
    id=3371662,
    processes=[procs.w_lnu_j2_pt100to200],
    keys=[
        "/WtoLNu-2Jets_Bin-2J-PTLNu-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v3-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=7440,
    n_events=469917942,
)

cpn.add_dataset(
    name="w_lnu_j2_pt200to400_amcatnlo",
    id=3372219,
    processes=[procs.w_lnu_j2_pt200to400],
    keys=[
        "/WtoLNu-2Jets_Bin-2J-PTLNu-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=871,
    n_events=75124628,
)

cpn.add_dataset(
    name="w_lnu_j2_pt400to600_amcatnlo",
    id=3371553,
    processes=[procs.w_lnu_j2_pt400to600],
    keys=[
        "/WtoLNu-2Jets_Bin-2J-PTLNu-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=176,
    n_events=14222725,
)

cpn.add_dataset(
    name="w_lnu_j2_pt600_amcatnlo",
    id=3371953,
    processes=[procs.w_lnu_j2_pt600],
    keys=[
        "/WtoLNu-2Jets_Bin-2J-PTLNu-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=194,
    n_events=14991109,
)

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=3371584,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/Zto2Q-4Jets_Bin-HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=5410,
#     n_events=454296062,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=3371519,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/Zto2Q-4Jets_Bin-HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=2740,
#     n_events=181252308,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=3371621,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/Zto2Q-4Jets_Bin-HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1143,
#     n_events=51519410,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=3371560,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/Zto2Q-4Jets_Bin-HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1529,
#     n_events=67209394,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=3371496,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/Zto2Q-4Jets_Bin-HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v3-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1172,
#     n_events=42051768,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3371740,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/DYto2E-2Jets_Bin-MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1608,
#     n_events=139246435,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3371498,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/DYto2Mu-2Jets_Bin-MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1966,
#     n_events=144880610,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3371625,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/DYto2Tau-2Jets_Bin-MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1570,
#     n_events=133319951,
# )
#

cpn.add_dataset(
    name="dy_ee_m50toinf_amcatnlo",
    id=3370654,
    processes=[procs.dy_ee_m50toinf],
    keys=[
        "/DYto2E-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v4-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=6585,
    n_events=483753919,
)

cpn.add_dataset(
    name="dy_mumu_m50toinf_amcatnlo",
    id=3370632,
    processes=[procs.dy_mumu_m50toinf],
    keys=[
        "/DYto2Mu-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v6-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=6731,
    n_events=488612255,
)

cpn.add_dataset(
    name="dy_tautau_m50toinf_amcatnlo",
    id=3370758,
    processes=[procs.dy_tautau_m50toinf],
    keys=[
        "/DYto2Tau-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v7-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=4178,
    n_events=349058559,
)

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=3371659,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/DYto2E-4Jets_Bin-MLL-10to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=5195,
#     n_events=391568488,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=3371734,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/DYto2Mu-4Jets_Bin-MLL-10to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=5926,
#     n_events=416553031,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=3371972,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/DYto2Tau-4Jets_Bin-MLL-10to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=6328,
#     n_events=487541879,
# )
#

cpn.add_dataset(
    name="ww_sl_powheg",
    id=3374712,
    processes=[procs.ww_sl],
    keys=[
        "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=923,
    n_events=79730963,
)

cpn.add_dataset(
    name="ww_wlnu_wlnu_powheg",
    id=3374654,
    processes=[procs.ww_dl],
    keys=[
        "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2778,
    n_events=240983710,
)

cpn.add_dataset(
    name="wz_wlnu_zqq_powheg",
    id=3374836,
    processes=[procs.wz_wlnu_zqq],
    keys=[
        "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1633,
    n_events=143699249,
)

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374849,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WZToLNu2B-1Jets-4FS_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=149,
#     n_events=9501204,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374822,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WZtoL3Nu-1Jets-4FS_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=184,
#     n_events=14455252,
# )
#

cpn.add_dataset(
    name="wz_wqq_zll_powheg",
    id=3374648,
    processes=[procs.wz_wqq_zll],
    keys=[
        "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2734,
    n_events=236049432,
)

cpn.add_dataset(
    name="wz_wlnu_zll_powheg",
    id=3374701,
    processes=[procs.wz_wlnu_zll],
    keys=[
        "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2834,
    n_events=248149069,
)

cpn.add_dataset(
    name="zz_zll_znunu_powheg",
    id=3374703,
    processes=[procs.zz_zll_znunu],
    keys=[
        "/ZZto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2190,
    n_events=188715312,
)

cpn.add_dataset(
    name="zz_zqq_zll_powheg",
    id=3374868,
    processes=[procs.zz_zqq_zll],
    keys=[
        "/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=446,
    n_events=39122580,
)

cpn.add_dataset(
    name="zz_zll_zll_powheg",
    id=3374704,
    processes=[procs.zz_zll_zll],
    keys=[
        "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2741,
    n_events=236843699,
)

cpn.add_dataset(
    name="www_amcatnlo",
    id=3371810,
    processes=[procs.www],
    keys=[
        "/WWW-4F_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=86,
    n_events=4299284,
)

cpn.add_dataset(
    name="wwz_amcatnlo",
    id=3371793,
    processes=[procs.wwz],
    keys=[
        "/WWZ-4F_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=346,
    n_events=16197159,
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=3371881,
    processes=[procs.wzz],
    keys=[
        "/WZZ-5F_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=295,
    n_events=16199286,
)

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=3371792,
    processes=[procs.zzz],
    keys=[
        "/ZZZ-5F_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=320,
    n_events=16192091,
)

cpn.add_dataset(
    name="ww_fh_powheg",
    id=3370663,
    processes=[procs.ww_fh],
    keys=[
        "/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1775,
    n_events=152242717,
)

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3370583,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WZto4Q-1Jets-4FS_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=99,
#     n_events=6132868,
# )
#

cpn.add_dataset(
    name="zz_znunu_zqq_powheg",
    id=3370707,
    processes=[procs.zz_znunu_zqq],
    keys=[
        "/ZZto2Nu2Q_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=476,
    n_events=46047410,
)

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3370591,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/ZZto4Q-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=111,
#     n_events=4971870,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374218,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WtoENu-2Jets_Bin-0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=3752,
#     n_events=478505838,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374217,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WtoENu-2Jets_Bin-1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=5463,
#     n_events=385149736,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374265,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WtoENu-2Jets_Bin-2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=4812,
#     n_events=274136429,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374154,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WtoMuNu-2Jets_Bin-0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=3615,
#     n_events=462467985,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374243,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WtoMuNu-2Jets_Bin-1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=4683,
#     n_events=335599201,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374246,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WtoMuNu-2Jets_Bin-2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=4861,
#     n_events=299879589,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374156,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WtoTauNu-2Jets_Bin-0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1942,
#     n_events=242740915,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374280,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WtoTauNu-2Jets_Bin-1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=4898,
#     n_events=374344313,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374230,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WtoTauNu-2Jets_Bin-2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=4493,
#     n_events=327817735,
# )
#
