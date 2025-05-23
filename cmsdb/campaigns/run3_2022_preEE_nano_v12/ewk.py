# coding: utf-8

"""
Electroweak datasets for the 2022 pre-EE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn

####################################################################################################
#
# Drell-Yan
#
####################################################################################################

# inclusive, LO, forPog
cpn.add_dataset(
    name="dy_m50toinf_for_pog_madgraph",
    id=14802794,
    processes=[procs.dy_m50toinf],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22NanoAODv12-forPOG_130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=51,
    n_events=27096229,
)

# inclusive, LO
cpn.add_dataset(
    name="dy_m10to50_madgraph",
    id=14817818,
    processes=[procs.dy_m10to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-10to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=349,
            n_events=154413937,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_madgraph",
    id=14791369,
    processes=[procs.dy_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=157,
            n_events=74397637,
        ),
        extension=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=497,
            n_events=71486192,
        ),
    ),
)

# jet-binned, LO
cpn.add_dataset(
    name="dy_m50toinf_1j_madgraph",
    id=14790810,
    processes=[procs.dy_m50toinf_1j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=187,
            n_events=57771603,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_madgraph",
    id=14794042,
    processes=[procs.dy_m50toinf_2j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=147,
            n_events=50007544,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_3j_madgraph",
    id=14791238,
    processes=[procs.dy_m50toinf_3j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=109,
            n_events=28997825,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_4j_madgraph",
    id=14794840,
    processes=[procs.dy_m50toinf_4j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=140,
            n_events=9490226,
        ),
    ),
)

# TODO: implement corresponding processes + xsecs
# # ptll-binned, LO
# cpn.add_dataset(
#     name="dy_m50toinf_ptll100to200_madgraph",
#     id=14948737,
#     processes=[procs.dy_m50toinf_ptll100to200],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-50_PTLL-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=497,
#             n_events=69961256,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_ptll200to400_madgraph",
#     id=14949443,
#     processes=[procs.dy_m50toinf_ptll200to400],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-50_PTLL-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=155,
#             n_events=6931476,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_ptll400to600_madgraph",
#     id=14949288,
#     processes=[procs.dy_m50toinf_ptll400to600],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-50_PTLL-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=81,
#             n_events=3355496,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_ptll600toinf_madgraph",
#     id=14948747,
#     processes=[procs.dy_m50toinf_ptll600toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-50_PTLL-600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=117,
#             n_events=3470735,
#         ),
#     ),
# )

# # ht-binned, LO
# cpn.add_dataset(
#     name="dy_m4to50_ht40to70_madgraph",
#     id=14950532,
#     processes=[procs.dy_m4to50_ht40to70],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-4to50_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=1706,
#             n_events=332696345,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m4to50_ht70to100_madgraph",
#     id=14949534,
#     processes=[procs.dy_m4to50_ht70to100],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-4to50_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=1099,
#             n_events=201751012,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m4to50_ht400to800_madgraph",
#     id=14949799,
#     processes=[procs.dy_m4to50_ht400to800],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-4to50_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=77,
#             n_events=4520981,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m4to50_ht800to1500_madgraph",
#     id=14948706,
#     processes=[procs.dy_m4to50_ht800to1500],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-4to50_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=189,
#             n_events=3901947,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m4to50_ht1500to2500_madgraph",
#     id=14951014,
#     processes=[procs.dy_m4to50_ht1500to2500],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-4to50_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=54,
#             n_events=3203979,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m4to50_ht2500toinf_madgraph",
#     id=14952243,
#     processes=[procs.dy_m4to50_ht2500toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-4to50_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=147,
#             n_events=3660177,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50to120_ht40to70_madgraph",
#     id=14817089,
#     processes=[procs.dy_m50to120_ht40to70],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-50to120_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=422,
#             n_events=133980512,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50to120_ht70to100_madgraph",
#     id=14847021,
#     processes=[procs.dy_m50to120_ht70to100],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-50to120_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=648,
#             n_events=98847366,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50to120_ht100to400_madgraph",
#     id=14813464,
#     processes=[procs.dy_m50to120_ht100to400],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-50to120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=307,
#             n_events=142936007,
#         ),
#     ),
# )

# inclusive, NLO
cpn.add_dataset(
    name="dy_m4to10_amcatnlo",
    id=14940403,
    processes=[procs.dy_m4to10],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-4to10_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=1037,
            n_events=197465370,
        ),
        extension=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-4to10_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=838,
            n_events=147147055,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m10to50_amcatnlo",
    id=14803206,
    processes=[procs.dy_m10to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=322,
            n_events=215532589,
        ),
        extension=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v3/NANOAODSIM",  # noqa
            ],
            n_files=1123,
            n_events=171220296,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_amcatnlo",
    id=14791972,
    processes=[procs.dy_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=286,
            n_events=213436879,
        ),
        extension=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v1/NANOAODSIM",  # noqa
            ],
            n_files=407,
            n_events=319825084,
        ),
    ),
)

# jet-binned, NLO
cpn.add_dataset(
    name="dy_m50toinf_0j_amcatnlo",
    id=14791116,
    processes=[procs.dy_m50toinf_0j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=452,
            n_events=346950546,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_amcatnlo",
    id=14790681,
    processes=[procs.dy_m50toinf_1j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=454,
            n_events=322623183,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_amcatnlo",
    id=14801013,
    processes=[procs.dy_m50toinf_2j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=386,
            n_events=277437970,
        ),
    ),
)

# TODO: implement corresponding processes + xsecs
# # ptll and jet-binned, NLO
# cpn.add_dataset(
#     name="dy_m50toinf_1j_ptll40to100_amcatnlo",
#     id=14825993,
#     processes=[procs.dy_m50toinf_1j_ptll40to100],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=287,
#             n_events=163904854,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_1j_ptll100to200_amcatnlo",
#     id=14826169,
#     processes=[procs.dy_m50toinf_1j_ptll100to200],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=183,
#             n_events=64510280,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_1j_ptll200to400_amcatnlo",
#     id=14824736,
#     processes=[procs.dy_m50toinf_1j_ptll200to400],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=61,
#             n_events=6583092,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_1j_ptll400to600_amcatnlo",
#     id=14826052,
#     processes=[procs.dy_m50toinf_1j_ptll400to600],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=38,
#             n_events=1722633,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_1j_ptll600toinf_amcatnlo",
#     id=14870369,
#     processes=[procs.dy_m50toinf_1j_ptll600toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=33,
#             n_events=1862921,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_2j_ptll40to100_amcatnlo",
#     id=14868304,
#     processes=[procs.dy_m50toinf_2j_ptll40to100],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=406,
#             n_events=66554879,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_2j_ptll100to200_amcatnlo",
#     id=14870830,
#     processes=[procs.dy_m50toinf_2j_ptll100to200],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=356,
#             n_events=70249250,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_2j_ptll200to400_amcatnlo",
#     id=14853119,
#     processes=[procs.dy_m50toinf_2j_ptll200to400],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=93,
#             n_events=12661552,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_2j_ptll400to600_amcatnlo",
#     id=14827368,
#     processes=[procs.dy_m50toinf_2j_ptll400to600],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=48,
#             n_events=1739647,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_2j_ptll600toinf_amcatnlo",
#     id=14824689,
#     processes=[procs.dy_m50toinf_2j_ptll600toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=25,
#             n_events=1682240,
#         ),
#     ),
# )


####################################################################################################
#
# W boson production
#
####################################################################################################

cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14803995,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=148,
    n_events=84739011,
)

####################################################################################################
#
# Diboson
#
####################################################################################################


# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22GS&nanoaod_version=v11&short_name=VV  # noqa

# TODO update to NanoAODv12
cpn.add_dataset(
    name="zz_pythia",
    id=14587173,
    is_data=False,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=1186860,
)

cpn.add_dataset(
    name="zz_zll_zll",
    id=14791221,
    processes=[procs.zz_zll_zll],
    keys=[
        "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=82,
    n_events=14629101,
)

#
# WZ
#

cpn.add_dataset(
    name="wz",
    id=14803901,
    is_data=False,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=7527043,
)

cpn.add_dataset(
    name="wz_wlnu_zll",
    id=14791591,
    is_data=False,
    processes=[procs.wz_wlnu_zll],
    keys=[
        "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=2776339,
)

cpn.add_dataset(
    name="wz_wlnu_zll_1jets",
    id=14784506,
    is_data=False,
    processes=[procs.wz_wlnu_zll_1jets],  # TODO change processes to 1 jet specific
    keys=[
        "/WZto3LNu-1Jets-4FS_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=108,
    n_events=10095542,
)

#
# WW
#

cpn.add_dataset(
    name="ww_pythia",
    id=14800098,
    is_data=False,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=63,
    n_events=15357390,
)

cpn.add_dataset(
    name="ww_wlnu_wlnu_powheg",
    id=14793091,
    is_data=False,
    processes=[procs.ww_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=40,
            n_events=6135192,
        ),
        extension=DatasetInfo(
            keys=[
                "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=77,
            n_events=6599291,
        ),
    ),
)

#
# GluGlueToContinToZZ
#

# cpn.add_dataset(
#    name="gluglutocontintozzto2e2mu_mcfm",
#    id=14826608,
#    processes=[procs.ggtozzto2e2mu],
#    keys=[
#        "/GluGluToContinto2Zto2E2Mu_TuneCP5_13p6TeV_mcfm701-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#    ],
#    n_files=1,
#    n_events=523444,
# )

cpn.add_dataset(
    name="gluglutocontintozzto2e2tau_mcfm",
    id=14889015,
    processes=[procs.ggtozzto2e2tau],
    keys=[
        "/GluGluToContinto2Zto2E2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=144855,
)

cpn.add_dataset(
    name="gluglutocontintozzto2mu2tau_mcfm",
    id=14889049,
    processes=[procs.ggtozzto2mu2tau],
    keys=[
        "/GluGluToContinto2Zto2Mu2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=146285,
)

# TODO Not found in CMSDAS
# cpn.add_dataset(
#    name="gluglutocontintozzto4e_mcfm",
#    id=14242982,
#    processes=[procs.ggtozzto4e],
#    keys=[
#        "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
#    ],
#    n_files=25,
#    n_events=974000,
# )
#
# cpn.add_dataset(
#    name="gluglutocontintozzto4mu_mcfm",
#    id=14266651,
#    processes=[procs.ggtozzto4mu],
#    keys=[
#        "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
#    ],
#    n_files=34,
#    n_events=845232,
# )
#
# cpn.add_dataset(
#    name="gluglutocontintozzto4tau_mcfm",
#    id=14253997,
#    processes=[procs.ggtozzto4tau],
#    keys=[
#        "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
#    ],
#    n_files=10,
#    n_events=493998,
# )

#
# Triple Boson
#

cpn.add_dataset(
    name="www",
    id=14800679,
    processes=[procs.www],
    keys=[
        "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=450000,
)

cpn.add_dataset(
    name="wwz",
    id=14797985,
    processes=[procs.wwz],
    keys=[
        "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=40,
    n_events=1950044,
)

cpn.add_dataset(
    name="wzz",
    id=14796198,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=1987058,
)

cpn.add_dataset(
    name="zzz",
    id=14801345,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=1970234,
)
