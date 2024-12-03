# coding: utf-8

"""
top quark datasets for the 2023 post-BPix data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_v12 import campaign_run3_2023_postBPix_nano_v12 as cpn


####################################################################################################
#
# ttbar (only datasets needed for ttZ)
#
####################################################################################################

#
# ttbar (powheg)
#

cpn.add_dataset(
    name="tt_sl_powheg",
    id=14808334,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=492,
            n_events=82058000,
        )
    ),
)


cpn.add_dataset(
    name="tt_dl_powheg",
    id=14835967,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=150,
            n_events=24649000,
        )
    ),
)

####################################################################################################
#
# single top (s-channel)
#
####################################################################################################

# TODO: not yet found in DAS

####################################################################################################
#
# single top (t-channel)
#
####################################################################################################

# TODO: not yet found in DAS

####################################################################################################
#
# single top (tW-channel)
#
####################################################################################################

cpn.add_dataset(
    name="st_twchannel_t_dl_powheg",
    id=14836358,
    processes=[procs.st_twchannel_t_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=2479000,
        )
    ),
)

cpn.add_dataset(
    name="st_twchannel_tbar_dl_powheg",
    id=14930339,
    processes=[procs.st_twchannel_tbar_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=50,
            n_events=2488000,
        )
    ),
)

####################################################################################################
#
# ttV, ttVV
#
####################################################################################################


#
# TT + X
#

cpn.add_dataset(
    name="ttz_zll_m4to50",
    id=14982175,
    processes=[procs.ttz_zll_m4to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            aux={
                "broken_files": [
                    "/store/mc/Run3Summer23BPixNanoAODv12/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/NANOAODSIM/130X_mcRun3_2023_realistic_postBPix_v6-v2/80000/3370d4e8-e2f9-4901-b8af-e3225e39a1c2.root",
                ],
            },
            n_files=16,  # 17-1 broken file because not available on t2b
            n_events=294000,
        ),
    ),
)

cpn.add_dataset(
    name="ttz_zll_m50toinf",
    id=14989610,
    processes=[procs.ttz_zll_m50toinf],
    keys=[
            "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
        ],
    n_files=23,
    n_events=400000,
)

cpn.add_dataset(
    name="ttw_wlnu_1jets",
    id=15137890,
    processes=[procs.ttw_wlnu],
    keys=[
        "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",
    ],
    n_files=1,
    n_events=256078,
)

#
# TT + XX

cpn.add_dataset(
    name="tttt",
    id=14987188,
    processes=[procs.tttt],
    keys=[
            "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
        ],
    n_files=43,
    n_events=2477775,
)


cpn.add_dataset(
    name="ttww_madgraph",
    id=14931988,
    processes=[procs.ttww],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=74,
            n_events=7288000,
        ),
    ),
)
cpn.add_dataset(
    name="ttwz_madgraph",
    id=14969073,
    processes=[procs.ttw],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=3,
            n_events=497000,
        ),
    ),
)

cpn.add_dataset(
    name="ttzz_madgraph",
    id=14937861,
    processes=[procs.ttzz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=992000,
        ),
    ),
)


#
# Single Top + X(X/q)
#

cpn.add_dataset(
    name="twz_tqq_wlnu_zll_dr1",
    id=15140022,
    processes=[procs.twz_tqq_wlnu_zll_dr1],
    keys=[
            "/TWZ_Tto2Q_WtoLNu_Zto2L_DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
        ],
    n_files=32,
    n_events=2184000,
)

cpn.add_dataset(
    name="twz_tqq_wlnu_zll_dr2",
    id=15053489,
    processes=[procs.twz_tqq_wlnu_zll_dr2],
    keys=[
            "/TWZ_Tto2Q_WtoLNu_Zto2L_DR2_SM_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
        ],
    n_files=13,
    n_events=557000,
)

cpn.add_dataset(
    name="twz_tlnu_wqq_zll_dr1",
    id=15139307,
    processes=[procs.twz_tlnu_wqq_zll_dr1],
    keys=[
            "/TWZ_TtoLNu_Wto2Q_Zto2L_DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
        ],
    n_files=35,
    n_events=4272000,
)

cpn.add_dataset(
    name="twz_tlnu_wqq_zll_dr2",
    id=15058265,
    processes=[procs.twz_tlnu_wqq_zll_dr2],
    keys=[
            "/TWZ_TtoLNu_Wto2Q_Zto2L_DR2_SM_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
        ],
    n_files=17,
    n_events=557000,
)

cpn.add_dataset(
    name="twz_tlnu_wlnu_zll_dr1",
    id=15139306,
    processes=[procs.twz_tlnu_wlnu_zll_dr1],
    keys=[
            "/TWZ_TtoLNu_WtoLNu_Zto2L_DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
        ],
    n_files=36,
    n_events=1097000,
)

cpn.add_dataset(
    name="twz_tlnu_wlnu_zll_dr2",
    id=15054138,
    processes=[procs.twz_tlnu_wlnu_zll_dr2],
    keys=[
            "/TWZ_TtoLNu_WtoLNu_Zto2L_DR2_SM_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
        ],
    n_files=3,
    n_events=226000,
)

# tZq not available in 2023 postBPIX
# cpn.add_dataset(
#   name="tzq_zll_4f_m30toinf",
#   id=14916923,
#   processes=[procs.tzq],
#   keys=[
#           "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#       ],
#   n_files=32,
#   n_events=889780,
# )
