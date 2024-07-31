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

# semileptonic decay
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&nanoaod_version=v11&dataset=TTtoLNu2Q%28_Hdamp-*%7C_MT-17%281%7C3%29p5%29%3F_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="tt_sl_powheg",
    id=14784316,
    is_data=False,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=1786,
            n_events=275339453,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=90,
            n_events=107949071,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=92,
            n_events=109342509,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=89,
            n_events=107779545,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=88,
            n_events=105437846,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=95,
            n_events=115411674,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=89,
            n_events=108182255,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
        ),
    ),
)

# 14.05.2024: updated to NanoAODv12-130X (hdamp samples not updated)
# dileptonic decay
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&nanoaod_version=v11&dataset=TTto2L2Nu%28_Hdamp-*%7C_MT-17%281%7C3%29p5%29%3F_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="tt_dl_powheg",
    id=14790873,
    is_data=False,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=137,
            n_events=84809345,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=86,
            n_events=34267798,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=192,
            n_events=33116945,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=34310080,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=34068776,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=33610745,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=31,
            n_events=33847420,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
        ),
    ),
)


# fully hadronic decay
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&nanoaod_version=v11&dataset=TTto4Q%28_Hdamp-*%7C_MT-17%281%7C3%29p5%29%3F_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="tt_fh_powheg",
    id=14694881,
    is_data=False,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=146,
            n_events=180771725,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=62,
            n_events=73737184,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=67,
            n_events=76996336,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=63,
            n_events=75616556,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=67,
            n_events=80077495,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=65,
            n_events=78138120,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=68,
            n_events=77216300,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
        ),
    ),
)

#
# single top (t-channel)
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&nanoaod_version=v11&dataset=%28TBbar%7CTbarB%29Q_t-channel&chained_request=Premix  # noqa

# t-channel (top)
cpn.add_dataset(
    name="st_tchannel_t_powheg",
    id=14636179,
    is_data=False,
    processes=[procs.st_tchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=10403540,
        ),
    ),
)

# t-channel (anti-top)
cpn.add_dataset(
    name="st_tchannel_tbar_powheg",
    id=14625205,
    is_data=False,
    processes=[procs.st_tchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=5210840,
        ),
    ),
)

#
# single-top (tW-channel)
#

# semileptonic decay (top)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&nanoaod_version=v11&dataset=TWminustoLNu2Q*_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="st_twchannel_t_sl_powheg",
    id=14691146,
    is_data=False,
    processes=[procs.st_twchannel_t_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=15,
            n_events=17032110,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=15,
            n_events=17519371,
        ),
        # missing as of 2023-07-01
        # tune_down=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=None,
        #     n_events=None,
        # ),
        # missing as of 2023-07-01
        # cr_1=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=None,
        #     n_events=None,
        # ),
        # missing as of 2023-07-01
        # cr_2=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=None,
        #     n_events=None,
        # ),
    ),
)

# semileptonic decay (anti-top)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&nanoaod_version=v11&dataset=TbarWplustoLNu2Q*_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="st_twchannel_tbar_sl_powheg",
    id=14691192,
    is_data=False,
    processes=[procs.st_twchannel_tbar_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=15,
            n_events=16804298,
        ),
        # missing as of 2023-07-01
        # tune_up=DatasetInfo(
        #     keys=[
        #         "/TbarWplustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=None,
        #     n_events=None,
        # ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=15,
            n_events=17361554,
        ),
        # missing as of 2023-07-01
        # cr_1=DatasetInfo(
        #     keys=[
        #         "/TbarWplustoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=None,
        #     n_events=None,
        # ),
        # missing as of 2023-07-01
        # cr_2=DatasetInfo(
        #     keys=[
        #         "/TbarWplustoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=None,
        #     n_events=None,
        # ),
    ),
)

# dileptonic decay (top)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&nanoaod_version=v11&dataset=TWminusto2L2Nu*_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="st_twchannel_t_dl_powheg",
    id=14784144,
    is_data=False,
    processes=[procs.st_twchannel_t_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=233,
            n_events=8466410,
        ),

        # missing as of 2023-07-01
        # tune_up=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=None,
        #     n_events=None,
        # ),
        # missing as of 2023-07-01
        # tune_down=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=None,
        #     n_events=None,
        # ),
        # missing as of 2023-07-01
        # cr_1=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=None,
        #     n_events=None,
        # ),
        # missing as of 2023-07-01
        # cr_2=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=None,
        #     n_events=None,
        # ),
    ),
)

# dileptonic decay (anti-top)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&nanoaod_version=v11&dataset=TbarWplusto2L2Nu*_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="st_twchannel_tbar_dl_powheg",
    id=14784283,
    is_data=False,
    processes=[procs.st_twchannel_tbar_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=196,
            n_events=8555460,
        ),
        # missing as of 2023-07-01
        # tune_up=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=None,
        #     n_events=None,
        # ),
        # missing as of 2023-07-01
        # tune_down=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=None,
        #     n_events=None,
        # ),
        # missing as of 2023-07-01
        # cr_1=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=None,
        #     n_events=None,
        # ),
        cr_2=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=7,
            n_events=8274400,
        ),
    ),
)


# fully hadronic decay (top)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&nanoaod_version=v11&dataset=TWminusto4Q*_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="st_twchannel_t_fh_powheg",
    id=14691441,
    is_data=False,
    processes=[procs.st_twchannel_t_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=13480012,
        ),
        # missing as of 2023-07-01
        # tune_up=DatasetInfo(
        #     keys=[
        #         "/TWminusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=None,
        #     n_events=None,
        # ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=12,
            n_events=13372624,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=13348008,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=12,
            n_events=13977131,
        ),
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
    name="ttll_mll_4to50_amcatnlo",
    id=14792774,
    processes=[procs.ttll_mll_m4to50],
    keys=[
            "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        ],
    n_files=25,
    n_events=1049999,
)

cpn.add_dataset(
    name="ttll_mll_50_amcatnlo",
    id=14793375,
    processes=[procs.ttll_mll_m50],
    keys=[
            "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        ],
    n_files=23,
    n_events=1343867,
)


cpn.add_dataset(
    name="tthjettononbb_m125_amcatnlo",
    id=14852415,
    processes=[procs.tthjetstononbb],
    keys=[
            "/TTHtoNon2B-1Jets_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        ],
    n_files=320,
    n_events=22107915,
)

# cpn.add_dataset(
#    name="ttgamma_dilept",
#    id=14260351,
#    processes=[procs.ttgamma_dilept],
#    keys=[
#            "/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM ",  # noqa
#        ],
#    n_files=15,
#    n_events=14694000,
# )

cpn.add_dataset(
    name="ttlnu_amcatnlo",
    id=14232323,
    processes=[procs.ttlnu],
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
    name="ttwh_madgraph",
    id=14855650,
    processes=[procs.ttwh],
    keys=[
            "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        ],
    n_files=79,
    n_events=2800000,
)

# TODO update to NanoAODv12 once available
cpn.add_dataset(
    name="tttt_amcatnlo",
    id=14811100,
    processes=[procs.tttt],
    keys=[
            "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
        ],
    n_files=34,
    n_events=8571152,
)

cpn.add_dataset(
   name="ttzh_madgraph",
   id=14861698,
   processes=[procs.ttzh],
   keys=[
           "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
       ],
   n_files=104,
   n_events=2785771,
)

# TODO not found in CMSDAS
# cpn.add_dataset(
#    name="tthh_madgraph",
#    id=14286140,
#    processes=[procs.tthh],
#    keys=[
#            "/TTHH_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
#        ],
#    n_files=13,
#    n_events=500000,
# )
#
# cpn.add_dataset(
#    name="ttwz_madgraph",
#    id=14234781,
#    processes=[procs.ttwz],
#    keys=[
#            "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
#        ],
#    n_files=2,
#    n_events=498000,
# )


#
# Single Top + X
#

cpn.add_dataset(
    name="twztoll_thad_wlept_dr1_amcatnlo",
    id=14868500,
    processes=[procs.twztoll_thad_wlept_dr1],
    keys=[
            "/TWZ_Tto2Q_WtoLNu_Zto2L_DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
        ],
    n_files=35,
    n_events=159111,
)

cpn.add_dataset(
    name="twztoll_thad_wlept_dr2_amcatnlo",
    id=14870420,
    processes=[procs.twztoll_thad_wlept_dr2],
    keys=[
            "/TWZ_Tto2Q_WtoLNu_Zto2L_DR2_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
        ],
    n_files=60,
    n_events=1979526,
)

cpn.add_dataset(
    name="twztoll_tlept_whad_dr1_amcatnlo",
    id=14885317,
    processes=[procs.twztoll_tlept_whad_dr1],
    keys=[
            "/TWZ_TtoLNu_Wto2Q_Zto2L_DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM",  # noqa
        ],
    n_files=11,
    n_events=45954,
)


cpn.add_dataset(
    name="twztoll_tlept_whad_dr2_amcatnlo",
    id=14854709,
    processes=[procs.twztoll_tlept_whad_dr2],
    keys=[
            "/TWZ_TtoLNu_Wto2Q_Zto2L_DR2_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
        ],
    n_files=12,
    n_events=2000000,
)

cpn.add_dataset(
    name="twztoll_tlept_wlept_dr1_amcatnlo",
    id=14885324,
    processes=[procs.twztoll_tlept_wlept_dr1],
    keys=[
            "/TWZ_TtoLNu_WtoLNu_Zto2L_DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
        ],
    n_files=23,
    n_events=414414,
)

cpn.add_dataset(
    name="twztoll_tlept_wlept_dr2_amcatnlo",
    id=14870596,
    processes=[procs.twztoll_tlept_wlept_dr2],
    keys=[
            "/TWZ_TtoLNu_WtoLNu_Zto2L_DR2_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
        ],
    n_files=30,
    n_events=808552,
)

cpn.add_dataset(
   name="tzq_ll_4f_ckm_amcatnlo",
   id=14916913,
   processes=[procs.tzq],
   keys=[
           "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
       ],
   n_files=40,
   n_events=3047512,
)
