# coding: utf-8

"""
Higgs datasets for the 2024 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_customnano_v15 import campaign_run3_2024_customnano_v15 as cpn

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370683,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/TTH-Hto2C_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=27,
#     n_events=996455,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370637,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/TTH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=55,
#     n_events=2443910,
# )
#

cpn.add_dataset(
    name="tth_hnonbb_powheg",
    id=3370614,
    processes=[procs.tth_hnonbb],
    keys=[
        "/TTH-HtoNon2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1218,
    n_events=53980865,
)

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370740,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/TTH-Hto2B-TTto2L2Nu_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=779,
#     n_events=29527000,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370724,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/TTH-Hto2B-TTto4Q_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=758,
#     n_events=29658000,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370742,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/TTH-Hto2B-TTtoLNu2Q_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=721,
#     n_events=29048000,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3372076,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/GluGluH-Hto2G_Par-M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=160,
#     n_events=7839611,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3372168,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/TTH-Hto2G_Par-M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1004,
#     n_events=34851285,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3372073,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/BBH-Hto2G_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=21,
#     n_events=1499300,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3372123,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/VBFH-Hto2G_Par-M-125_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=91,
#     n_events=4483026,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3372107,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WplusH-Hto2G-Wto2Q_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=59,
#     n_events=913855,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3372059,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WplusH-Hto2G-WtoLNu_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=60,
#     n_events=898894,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3372125,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/HPlusB-Hto2G-5FS-MuRFScaleDynX0p50_Par-M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=610,
#     n_events=30955136,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3372115,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/HPlusB-Hto2G-4FS-MuRFScaleDynX0p50_Par-M-125_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=286,
#     n_events=15000000,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3372104,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/HPlusC-Hto2G-3FS-MuRFScaleDynX0p50_Par-M-125_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=327,
#     n_events=15000000,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3372217,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/HPlusC-Hto2G-4FS-MuRFScaleDynX0p50_Par-M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=495,
#     n_events=28387959,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370689,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/ZH-Zto2Q-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=40,
#     n_events=2877591,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370638,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/GluGluZH-Zto2Q-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=11,
#     n_events=500000,
# )
#

cpn.add_dataset(
    name="wmh_wqq_hbb_powheg",
    id=3370688,
    processes=[procs.wmh_wqq_hbb],
    keys=[
        "/WminusH-Wto2Q-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=47,
    n_events=3966909,
)

cpn.add_dataset(
    name="wmh_wlnu_hbb_powheg",
    id=3370776,
    processes=[procs.wmh_wlnu_hbb],
    keys=[
        "/WminusH-WtoLNu-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=28,
    n_events=1976960,
)

cpn.add_dataset(
    name="wph_wqq_hbb_powheg",
    id=3370682,
    processes=[procs.wph_wqq_hbb],
    keys=[
        "/WplusH-Wto2Q-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=78,
    n_events=6261825,
)

cpn.add_dataset(
    name="wph_wlnu_hbb_powheg",
    id=3370704,
    processes=[procs.wph_wlnu_hbb],
    keys=[
        "/WplusH-WtoLNu-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=45,
    n_events=3068881,
)

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370710,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/ZH-Zto2Q-Hto2C_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=24,
#     n_events=1468890,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370677,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/GluGluZH-Zto2Q-Hto2C_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=8,
#     n_events=400000,
# )
#

cpn.add_dataset(
    name="wmh_wqq_hcc_powheg",
    id=3370691,
    processes=[procs.wmh_wqq_hcc],
    keys=[
        "/WminusH-Wto2Q-Hto2C_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=29,
    n_events=1980289,
)

cpn.add_dataset(
    name="wmh_wlnu_hcc_powheg",
    id=3370606,
    processes=[procs.wmh_wlnu_hcc],
    keys=[
        "/WminusH-WtoLNu-Hto2C_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=17,
    n_events=991419,
)

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370640,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WplusH-Wto2Q-Hto2C_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=40,
#     n_events=3149704,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370659,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WplusH-WtoLNu-Hto2C_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=23,
#     n_events=1575988,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370725,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/VBFH-Hto2C_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=51,
#     n_events=3969341,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370702,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/VBFH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=121,
#     n_events=9989440,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=3370743,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/VBFZto2Q_TuneCP5_13p6TeV_madgraph-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=174,
#     n_events=13834407,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370731,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/VBFH-Hto2C_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-ext1-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=335,
#     n_events=19989500,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370650,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/VBFH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-ext1-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=349,
#     n_events=19990298,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370698,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/GluGluH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=115,
#     n_events=9874198,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370661,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/GluGluH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-ext1-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=307,
#     n_events=19932930,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370717,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/GluGluH-Hto2C_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=50,
#     n_events=3956380,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370757,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/GluGluH-Hto2C_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-ext1-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=323,
#     n_events=19919744,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370675,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/GluGluZH-Zto2L-Hto2S_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=12,
#     n_events=193475,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370667,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/GluGluZH-Zto2Nu-Hto2S_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=5,
#     n_events=96375,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370642,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/GluGluZH-Zto2Q-Hto2S_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=8,
#     n_events=100000,
# )
#

cpn.add_dataset(
    name="wmh_wqq_hss_powheg",
    id=3370673,
    processes=[procs.wmh_wqq_hss],
    keys=[
        "/WminusH-Wto2Q-Hto2S_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=17,
    n_events=989238,
)

cpn.add_dataset(
    name="wmh_wlnu_hss_powheg",
    id=3370635,
    processes=[procs.wmh_wlnu_hss],
    keys=[
        "/WminusH-WtoLNu-Hto2S_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=11,
    n_events=497475,
)

cpn.add_dataset(
    name="wph_wqq_hss_powheg",
    id=3370680,
    processes=[procs.wph_wqq_hss],
    keys=[
        "/WplusH-Wto2Q-Hto2S_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=25,
    n_events=1595072,
)

cpn.add_dataset(
    name="wph_wlnu_hss_powheg",
    id=3370696,
    processes=[procs.wph_wlnu_hss],
    keys=[
        "/WplusH-WtoLNu-Hto2S_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=20,
    n_events=793160,
)

cpn.add_dataset(
    name="zh_zll_hss_powheg",
    id=3370721,
    processes=[procs.zh_zll_hss],
    keys=[
        "/ZH-Zto2L-Hto2S_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=8,
    n_events=249376,
)

cpn.add_dataset(
    name="zh_znunu_hss_powheg",
    id=3370657,
    processes=[procs.zh_znunu_hss],
    keys=[
        "/ZH-Zto2Nu-Hto2S_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=8,
    n_events=250000,
)

cpn.add_dataset(
    name="zh_zqq_hss_powheg",
    id=3370753,
    processes=[procs.zh_zqq_hss],
    keys=[
        "/ZH-Zto2Q-Hto2S_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=12,
    n_events=495716,
)

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3372670,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/ZH-Hto2G-Zto2L_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=37,
#     n_events=920000,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3372879,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/ZH-Hto2G-Zto2Nu_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=40,
#     n_events=919031,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3372761,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/ZH-Hto2G-Zto2Q_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=39,
#     n_events=920000,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3372773,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WminusH-Hto2G-Wto2Q_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=55,
#     n_events=918868,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3372834,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/WminusH-Hto2G-WtoLNu_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/cmst3-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=58,
#     n_events=918020,
# )
#
