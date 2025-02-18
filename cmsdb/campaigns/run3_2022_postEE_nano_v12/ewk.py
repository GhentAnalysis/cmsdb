# coding: utf-8

"""
Electroweak datasets for the 2022 post-EE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_v12 import campaign_run3_2022_postEE_nano_v12 as cpn

####################################################################################################
#
# Drell-Yan
#
####################################################################################################

# inclusive, LO, forPog
cpn.add_dataset(
    name="dy_m50toinf_for_pog_madgraph",
    id=14791423,
    processes=[procs.dy_m50toinf],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22EENanoAODv12-forPOG_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=127,
    n_events=94947242,
)

# inclusive, LO
cpn.add_dataset(
    name="dy_m10to50_madgraph",
    id=14873228,
    processes=[procs.dy_m10to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-10to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
            ],
            n_files=2274,
            n_events=500642946,
        ),
    ),
)

# until not extended dataset is on t2b only use extended one
"""
cpn.add_dataset(
    name="dy_m50toinf_madgraph",
    id=14810676,
    processes=[procs.dy_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=236,
            n_events=240872023,
        ),
        extension=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=1587,
            n_events=254295366,
        ),
    ),
)
"""
cpn.add_dataset(
    name="dy_m50toinf_madgraph",
    id=14810676,
    processes=[procs.dy_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=1587,
            n_events=254295366,
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
# cpn.add_dataset(
#     name="dy_m50to120_ht400to800_madgraph",
#     id=14878614,
#     processes=[procs.dy_m50to120_ht400to800],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-50to120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=52,
#             n_events=3935310,
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
# # jet-binned, ptll-binned, NLO
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
    id=14796394,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=381,
    n_events=281543551,
)


#
# Diboson
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEGS&nanoaod_version=v11&short_name=VV  # noqa

# missing as of 2023-07-01
# cpn.add_dataset(
#     name="zz_pythia",
#     id=None,
#     is_data=False,
#     processes=[procs.zz],
#     keys=[
#         "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=None,
#     n_events=None,
# )

cpn.add_dataset(
    name="wz_pythia",
    id=14799680,
    is_data=False,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=90,
    n_events=26840468,
)

cpn.add_dataset(
    name="wz_wlnu_zll_powheg",
    id=14790992,
    is_data=False,
    processes=[procs.wz_wlnu_zll],
    keys=[
        "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM ",  # noqa
        "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM"  # noqa
    ],
    n_files=63 + 199,
    n_events=9779090 + 31432387,
)


cpn.add_dataset(
    name="wz_wlnu_zll_1jets_amcatnlo",
    id=14784506,
    is_data=False,
    processes=[procs.wz_wlnu_zll_1jets],  # TODO change processes to 1 jet specific
    keys=[
        "/WZto3LNu-1Jets-4FS_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=131,
    n_events=19099028,
)


cpn.add_dataset(
    name="ww_powheg",
    id=14801288,
    is_data=False,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=117,
    n_events=53190560,
)

cpn.add_dataset(
    name="ww_wlnu_wlnu_powheg",
    id=14791590,
    is_data=False,
    processes=[procs.ww_dl],
    keys=[
        "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=57,
    n_events=22428584,
)

# ZZ
#

cpn.add_dataset(
    name="zz_zll_zll_powheg",
    id=14790743,
    processes=[procs.zz_zll_zll],
    keys=[
        "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=208,
    n_events=61372656,
)

#
# GluGlueToContinToZZ
#

cpn.add_dataset(
    name="ggtozzto2e2mu_mcfm",
    id=14826608,
    processes=[procs.ggtozzto2e2mu],
    keys=[
        "/GluGluToContinto2Zto2E2Mu_TuneCP5_13p6TeV_mcfm701-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=523444,
)

cpn.add_dataset(
    name="ggtozzto2e2tau_mcfm",
    id=14889511,
    processes=[procs.ggtozzto2e2tau],
    keys=[
        "/GluGluToContinto2Zto2E2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=517620,
)

cpn.add_dataset(
    name="ggtozzto2mu2tau_mcfm",
    id=14889510,
    processes=[procs.ggtozzto2mu2tau],
    keys=[
        "/GluGluToContinto2Zto2Mu2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=525000,
)

cpn.add_dataset(
    name="ggtozzto4e_mcfm",
    id=14889461,
    processes=[procs.ggtozzto4e],
    keys=[
        "/GluGlutoContinto2Zto4E_TuneCP5_13p6TeV_mcfm-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=1035740,
)

cpn.add_dataset(
    name="ggtozzto4mu_mcfm",
    id=14889477,
    processes=[procs.ggtozzto4mu],
    keys=[
        "/GluGlutoContinto2Zto4Mu_TuneCP5_13p6TeV_mcfm-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=1032472,
)

cpn.add_dataset(
    name="ggtozzto4tau_mcfm",
    id=14889468,
    processes=[procs.ggtozzto4tau],
    keys=[
        "/GluGlutoContinto2Zto4Tau_TuneCP5_13p6TeV_mcfm-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=36,
    n_events=1044896,
)

# VH

cpn.add_dataset(
    name="vh_htononbb_m125_amcatnlo",
    id=14850117,
    processes=[procs.vh],
    keys=[
        "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=502646,
)

#
# Triple Boson
#

cpn.add_dataset(
    name="www_amcatnlo",
    id=14793787,
    processes=[procs.www],
    keys=[
        "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=1482480,
)

cpn.add_dataset(
    name="wwz_amcatnlo",
    id=14793788,
    processes=[procs.wwz],
    keys=[
        "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=5601076,
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=14798602,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=40,
    n_events=5290014,
)

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=14805133,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=5803440,
)

#
# Boson + Gamma
#

# WG

cpn.add_dataset(
    name="wg_wlnu_ptg10to100_amcatnlo",
    id=14787167,
    processes=[procs.wg_wlnu_ptg10to100],
    keys=[
        "/WGtoLNuG-1Jets_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1014,
    n_events=5803440,
)

cpn.add_dataset(
    name="wg_wlnu_ptg100to200_amcatnlo",
    id=14787642,
    processes=[procs.wg_wlnu_ptg100to200],
    keys=[
        "/WGtoLNuG-1Jets_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=123,
    n_events=3517478,
)

cpn.add_dataset(
    name="wg_wlnu_ptg200to400_amcatnlo",
    id=14850186,
    processes=[procs.wg_wlnu_ptg200to400],
    keys=[
        "/WGtoLNuG-1Jets_PTG-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=89,
    n_events=1657844,
)

cpn.add_dataset(
    name="wg_wlnu_ptg400to600_amcatnlo",
    id=14850183,
    processes=[procs.wg_wlnu_ptg400to600],
    keys=[
        "/WGtoLNuG-1Jets_PTG-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=72,
    n_events=1604621,
)

cpn.add_dataset(
    name="wg_wlnu_ptg600toinf_amcatnlo",
    id=14852427,
    processes=[procs.wg_wlnu_ptg600toinf],
    keys=[
        "/WGtoLNuG-1Jets_PTG-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=76,
    n_events=1794885,
)

# WZG

cpn.add_dataset(
    name="wzg_wlnu_amcatnlo",
    id=14797986,
    processes=[procs.wzg_wlnu],
    keys=[
        "/WZGtoLNuZG_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=750000,
)

# DYG to  2LG

cpn.add_dataset(
    name="dyg_zll_mll4to50_ptg10to100_amcatnlo",
    id=14809616,
    processes=[procs.dyg_zll_mll4to50_ptg10to100],
    keys=[
        "/DYGto2LG-1Jets_MLL-4to50_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=576,
    n_events=85739885,
)

cpn.add_dataset(
    name="dyg_zll_mll4to50_ptg100to200_amcatnlo",
    id=14809461,
    processes=[procs.dyg_zll_mll4to50_ptg100to200],
    keys=[
        "/DYGto2LG-1Jets_MLL-4to50_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=75,
    n_events=1448629,
)

cpn.add_dataset(
    name="dyg_zll_mll4to50_ptg200toinf_amcatnlo",
    id=14811651,
    processes=[procs.dyg_zll_mll4to50_ptg200toinf],
    keys=[
        "/DYGto2LG-1Jets_MLL-4to50_PTG-200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=30,
    n_events=746202,
)

cpn.add_dataset(
    name="dyg_zll_mll50toinf_ptg10to50_amcatnlo",
    id=14790854,
    processes=[procs.dyg_zll_mll50toinf_ptg10to50],
    keys=[
        "/DYGto2LG-1Jets_MLL-50_PTG-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=191,
    n_events=104473209,
)

cpn.add_dataset(
    name="dyg_zll_mll50toinf_ptg50to100_amcatnlo",
    id=14808376,
    processes=[procs.dyg_zll_mll50toinf_ptg50to100],
    keys=[
        "/DYGto2LG-1Jets_MLL-50_PTG-50to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=90,
    n_events=48791625,
)

cpn.add_dataset(
    name="dyg_zll_mll50toinf_ptg100to200_amcatnlo",
    id=14793597,
    processes=[procs.dyg_zll_mll50toinf_ptg100to200],
    keys=[
        "/DYGto2LG-1Jets_MLL-50_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=696610,
)

cpn.add_dataset(
    name="dyg_zll_mll50toinf_ptg200to400_amcatnlo",
    id=14886082,
    processes=[procs.dyg_zll_mll50toinf_ptg200to400],
    keys=[
        "/DYGto2LG-1Jets_MLL-50_PTG-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=29,
    n_events=1785572,
)

cpn.add_dataset(
    name="dyg_zll_mll50toinf_ptg400to600_amcatnlo",
    id=14887668,
    processes=[procs.dyg_zll_mll50toinf_ptg400to600],
    keys=[
        "/DYGto2LG-1Jets_MLL-50_PTG-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=1776157,
)

cpn.add_dataset(
    name="dyg_zll_mll50toinf_ptg600toinf_amcatnlo",
    id=14886958,
    processes=[procs.dyg_zll_mll50toinf_ptg600toinf],
    keys=[
        "/DYGto2LG-1Jets_MLL-50_PTG-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=62,
    n_events=1797374,
)
