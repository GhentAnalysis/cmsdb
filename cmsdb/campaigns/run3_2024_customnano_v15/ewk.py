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
#     n_files=2472,
#     n_events=149113003,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3371631,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/Wto2Q-2Jets_Bin-PTQQ-200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=17,
#     n_events=682095,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3371544,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/Wto2Q-2Jets_Bin-PTQQ-400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v3-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=911,
#     n_events=47112701,
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
#     n_files=2312,
#     n_events=147224645,
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
    n_files=2994,
    n_events=217652728,
)

cpn.add_dataset(
    name="w_lnu_j1_pt100to200_amcatnlo",
    id=3371647,
    processes=[procs.w_lnu_j1_pt100to200],
    keys=[
        "/WtoLNu-2Jets_Bin-1J-PTLNu-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v3-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=3969,
    n_events=274918001,
)

cpn.add_dataset(
    name="w_lnu_j1_pt200to400_amcatnlo",
    id=3371761,
    processes=[procs.w_lnu_j1_pt200to400],
    keys=[
        "/WtoLNu-2Jets_Bin-1J-PTLNu-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=435,
    n_events=37040113,
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
    n_files=174,
    n_events=15044100,
)

cpn.add_dataset(
    name="w_lnu_j2_pt40to100_amcatnlo",
    id=3371606,
    processes=[procs.w_lnu_j2_pt40to100],
    keys=[
        "/WtoLNu-2Jets_Bin-2J-PTLNu-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v3-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=5854,
    n_events=388406653,
)

cpn.add_dataset(
    name="w_lnu_j2_pt100to200_amcatnlo",
    id=3371662,
    processes=[procs.w_lnu_j2_pt100to200],
    keys=[
        "/WtoLNu-2Jets_Bin-2J-PTLNu-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v3-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=5352,
    n_events=342840702,
)

cpn.add_dataset(
    name="w_lnu_j2_pt200to400_amcatnlo",
    id=3372219,
    processes=[procs.w_lnu_j2_pt200to400],
    keys=[
        "/WtoLNu-2Jets_Bin-2J-PTLNu-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=221,
    n_events=19017336,
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
    n_files=190,
    n_events=14708268,
)

# missing /WtoLNu-4Jets_Bin-1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM
# missing /WtoLNu-4Jets_Bin-2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM
# missing /WtoLNu-4Jets_Bin-3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM
# missing /WtoLNu-4Jets_Bin-4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM
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
#     n_files=1113,
#     n_events=50224006,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=3371560,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/Zto2Q-4Jets_Bin-HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1526,
#     n_events=67063660,
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
    n_files=931,
    n_events=68606814,
)

cpn.add_dataset(
    name="dy_mumu_m50toinf_amcatnlo",
    id=3370632,
    processes=[procs.dy_mumu_m50toinf],
    keys=[
        "/DYto2Mu-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v6-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=3225,
    n_events=245692231,
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
#     n_files=3566,
#     n_events=273359932,
# )
#

# missing /WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM
# missing /WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM
# missing /WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM
# missing /WZToLNu2B-1Jets-4FS_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM
# missing /WZtoL3Nu-1Jets-4FS_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM
# missing /WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM
# missing /WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM
# missing /ZZto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM
# missing /ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM
# missing /ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM
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
    n_files=294,
    n_events=16162158,
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

# missing /DYGto2LG-1Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM
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
#     n_files=380,
#     n_events=47073829,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374217,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WtoENu-2Jets_Bin-1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1798,
#     n_events=138401918,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374265,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WtoENu-2Jets_Bin-2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1600,
#     n_events=87928101,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374154,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WtoMuNu-2Jets_Bin-0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1791,
#     n_events=230504399,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374243,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WtoMuNu-2Jets_Bin-1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1336,
#     n_events=102959013,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374246,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WtoMuNu-2Jets_Bin-2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1557,
#     n_events=90728354,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374156,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WtoTauNu-2Jets_Bin-0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=537,
#     n_events=67650643,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374280,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WtoTauNu-2Jets_Bin-1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=3579,
#     n_events=272738846,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3374230,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WtoTauNu-2Jets_Bin-2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=831,
#     n_events=50440762,
# )
#
