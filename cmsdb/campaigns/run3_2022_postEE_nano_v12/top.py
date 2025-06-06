# coding: utf-8

"""
top quark datasets for the 2022 post-EE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_v12 import campaign_run3_2022_postEE_nano_v12 as cpn

#
# ttbar
#

cpn.add_dataset(
    name="tt_sl_powheg",
    id=14797923,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=523,
            n_events=267007920,
        ),
        extension=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=1786,
            n_events=275339453,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=289,
            n_events=105603983,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=285,
            n_events=108814065,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTtoLNu2Q_MT-166p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=201,
        #     n_events=109075751,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTtoLNu2Q_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=233,
        #     n_events=113876301,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=227,
            n_events=106574300,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=266,
            n_events=108997020,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTtoLNu2Q_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=211,
        #     n_events=113420713,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTtoLNu2Q_MT-178p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=191,
        #     n_events=109020936,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=186,
            n_events=110835546,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=299,
            n_events=109684223,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=308,
            n_events=108790299,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=247,
            n_events=107642765,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTtoLNu2Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=276,
        #     n_events=110158847,
        # ),
    ),
)


cpn.add_dataset(
    name="tt_dl_powheg",
    id=14790873,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=137,
            n_events=84809345,
        ),
        extension=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=706,
            n_events=84715417,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=143,
            n_events=33569906,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
            ],
            n_files=69,
            n_events=33381504,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_MT-166p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=75,
        #     n_events=33861870,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=72,
        #     n_events=34502576,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=99,
            n_events=34528287,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=98,
            n_events=34942166,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=85,
        #     n_events=32171539,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_MT-178p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=141,
        #     n_events=33139400,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=175,
            n_events=33436823,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=83,
            n_events=33513515,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=192,
            n_events=33116945,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=86,
            n_events=34267798,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=106,
        #     n_events=36305732,
        # ),
    ),
)


cpn.add_dataset(
    name="tt_fh_powheg",
    id=14802702,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=294,
            n_events=179069201,
        ),
        extension=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=1417,
            n_events=187745623,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
            ],
            n_files=336,
            n_events=79760788,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=195,
            n_events=73588304,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto4Q_MT-166p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=186,
        #     n_events=71372700,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=160,
            n_events=73477028,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=152,
            n_events=76754456,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto4Q_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=146,
        #     n_events=78188810,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto4Q_MT-178p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=143,
        #     n_events=74833906,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=194,
            n_events=77014720,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=202,
            n_events=75167944,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=193,
            n_events=73414336,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto4Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=220,
        #     n_events=78441232,
        # ),
    ),
)


#
# single top (t-channel)
#


cpn.add_dataset(
    name="st_tchannel_t_4f_powheg",
    id=14800033,
    processes=[procs.st_tchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=104,
            n_events=10153433,
        ),
    ),
)
cpn.add_dataset(
    name="st_tchannel_tbar_4f_powheg",
    id=14805343,
    processes=[procs.st_tchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=46,
            n_events=5206568,
        ),
    ),
)

#
# single-top (tW-channel)
#


cpn.add_dataset(
    name="st_twchannel_t_sl_powheg",
    id=14792182,
    processes=[procs.st_twchannel_t_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=63,
            n_events=16666206,
        ),
        extension=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=226,
            n_events=15886044,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q_DS_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=88,
        #     n_events=17742721,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=90,
        #     n_events=17796577,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=87,
            n_events=17360046,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=16373306,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=56,
        #     n_events=17555496,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=124,
            n_events=16912207,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=104,
            n_events=15981441,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=140,
            n_events=16563901,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=101,
            n_events=17276921,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=141,
        #     n_events=15656945,
        # ),
    ),
)


cpn.add_dataset(
    name="st_twchannel_tbar_sl_powheg",
    id=14791275,
    processes=[procs.st_twchannel_tbar_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=65,
            n_events=16485994,
        ),
        extension=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=241,
            n_events=17272926,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplustoLNu2Q_DS_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=73,
        #     n_events=17220057,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=83,
            n_events=16625035,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=80,
            n_events=16788071,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplustoLNu2Q_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=64,
        #     n_events=16399368,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=77,
            n_events=16975875,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=72,
            n_events=17324463,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplustoLNu2Q_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=80,
        #     n_events=15811879,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=84,
            n_events=16500529,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=114,
            n_events=17109494,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=92,
            n_events=17265431,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=100,
            n_events=16958949,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplustoLNu2Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=118,
        #     n_events=17549333,
        # ),
    ),
)


cpn.add_dataset(
    name="st_twchannel_t_dl_powheg",
    id=14791125,
    processes=[procs.st_twchannel_t_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=51,
            n_events=8129084,
        ),
        extension=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=233,
            n_events=8466410,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_DS_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=32,
        #     n_events=8747906,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=91,
            n_events=8682320,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=96,
            n_events=8689026,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=80,
        #     n_events=8706724,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=80,
            n_events=8727065,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=72,
            n_events=8575656,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=45,
        #     n_events=8444552,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_TuneCH3_13p6TeV_powheg-herwig7/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM",  # noqa
        #     ],
        #     n_files=62,
        #     n_events=8730795,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=75,
            n_events=8558405,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=70,
            n_events=8667578,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=101,
            n_events=8666105,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=66,
            n_events=8496890,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=69,
        #     n_events=8194610,
        # ),
    ),
)


cpn.add_dataset(
    name="st_twchannel_tbar_dl_powheg",
    id=14791494,
    processes=[procs.st_twchannel_tbar_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=47,
            n_events=8183339,
        ),
        extension=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=196,
            n_events=8555460,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_DS_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=22,
        #     n_events=8696716,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=39,
            n_events=8604358,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=102,
            n_events=10703567,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=87,
        #     n_events=8707880,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=8343170,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=95,
            n_events=8744312,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=100,
        #     n_events=8384423,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_TuneCH3_13p6TeV_powheg-herwig7/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
        #     ],
        #     n_files=140,
        #     n_events=8710331,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=96,
            n_events=8468544,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=57,
            n_events=8223650,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=133,
            n_events=8609800,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=49,
            n_events=8511858,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=31,
        #     n_events=8040454,
        # ),
    ),
)


cpn.add_dataset(
    name="st_twchannel_t_fh_powheg",
    id=14791385,
    processes=[procs.st_twchannel_t_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=61,
            n_events=13460118,
        ),
        extension=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=125,
            n_events=13999320,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto4Q_DS_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=80,
        #     n_events=13721756,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=88,
            n_events=13414968,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=90,
            n_events=13970516,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto4Q_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=93,
        #     n_events=13893868,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=89,
            n_events=13708786,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=98,
            n_events=13317000,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto4Q_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=93,
        #     n_events=14208940,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=75,
            n_events=13429848,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=90,
            n_events=13778240,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=79,
            n_events=12988148,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=135,
            n_events=13756852,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto4Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=86,
        #     n_events=13259905,
        # ),
    ),
)


# fully hadronic decay (anti-top)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&nanoaod_version=v11&dataset=TbarWplusto4Q*_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
# nominal missing as of 2023-07-01
# cpn.add_dataset(
#     name="st_twchannel_tbar_fh_powheg",
#     id=None,
#     is_data=False,
#     processes=[procs.st_twchannel_tbar_fh],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=None,
#             n_events=None,
#         ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "/TbarWplusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=None,
#             n_events=None,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "/TbarWplusto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=None,
#             n_events=None,
#         ),
#         cr_1=DatasetInfo(
#             keys=[
#                 "/TbarWplusto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=None,
#             n_events=None,
#         ),
#         cr_2=DatasetInfo(
#             keys=[
#                 "/TbarWplusto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=13,
#             n_events=13896218,
#         ),
#     ),
# )


#
# TT + X
#

cpn.add_dataset(
    name="ttz_zll_m4to50",
    id=14792774,
    processes=[procs.ttz_zll_m4to50],
    keys=[
        "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=1049999,
)

cpn.add_dataset(
    name="ttz_zll_m50toinf",
    id=14793375,
    processes=[procs.ttz_zll_m50toinf],
    keys=[
        "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=1343867,
)

cpn.add_dataset(
    name="ttw_wlnu_1jets",
    id=14232323,
    processes=[procs.ttw_wlnu],
    keys=[
        "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=335985,
)
#
# TT + XX
# TODO process xsecs unknown!!
#

cpn.add_dataset(
    name="ttww_madgraph",
    id=14800877,
    processes=[procs.ttww],
    keys=[
        "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=52,
    n_events=1536000,
)

cpn.add_dataset(
    name="ttzz_madgraph",
    id=14826688,
    processes=[procs.ttzz],
    keys=[
        "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=1054000,
)

cpn.add_dataset(
    name="tttt",
    id=14811100,
    processes=[procs.tttt],
    keys=[
        "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=8571152,
)


cpn.add_dataset(
    name="ttwz_madgraph",
    id=15007011,
    processes=[procs.ttwz],
    keys=[
        "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=1132932,
)


#
# Single Top + X
#

cpn.add_dataset(
    name="twz_tqq_wlnu_zll_dr1",
    id=14868500,
    processes=[procs.twz_tqq_wlnu_zll_dr1],
    keys=[
        "/TWZ_Tto2Q_WtoLNu_Zto2L_DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=159111,
)

cpn.add_dataset(
    name="twz_tqq_wlnu_zll_dr2",
    id=14870420,
    processes=[procs.twz_tqq_wlnu_zll_dr2],
    keys=[
        "/TWZ_Tto2Q_WtoLNu_Zto2L_DR2_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=60,
    n_events=1979526,
)

cpn.add_dataset(
    name="twz_tlnu_wqq_zll_dr1",
    id=14885317,
    processes=[procs.twz_tlnu_wqq_zll_dr1],
    keys=[
        "/TWZ_TtoLNu_Wto2Q_Zto2L_DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=45954,
)


cpn.add_dataset(
    name="twz_tlnu_wqq_zll_dr2",
    id=14854709,
    processes=[procs.twz_tlnu_wqq_zll_dr2],
    keys=[
        "/TWZ_TtoLNu_Wto2Q_Zto2L_DR2_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=2000000,
)

cpn.add_dataset(
    name="twz_tlnu_wlnu_zll_dr1",
    id=14885324,
    processes=[procs.twz_tlnu_wlnu_zll_dr1],
    keys=[
        "/TWZ_TtoLNu_WtoLNu_Zto2L_DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=414414,
)

cpn.add_dataset(
    name="twz_tlnu_wlnu_zll_dr2",
    id=14870596,
    processes=[procs.twz_tlnu_wlnu_zll_dr2],
    keys=[
        "/TWZ_TtoLNu_WtoLNu_Zto2L_DR2_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=30,
    n_events=808552,
)

cpn.add_dataset(
    name="tzq_zll_4f_m30toinf",
    id=14916913,
    processes=[procs.tzq],
    keys=[
         "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=40,
    n_events=3047512,
)
