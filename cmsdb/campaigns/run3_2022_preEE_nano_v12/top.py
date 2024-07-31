# coding: utf-8

"""
top quark datasets for the 2022 pre-EE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn

#
# ttbar
#

# semileptonic decay
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=TTtoLNu2Q%28_Hdamp-*%7C_MT-17%281%7C3%29p5%29%3F_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="tt_sl_powheg",
    id=14707480,
    is_data=False,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=67,
            n_events=80484415,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=32259560,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=32703000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=28,
            n_events=31147944,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=31624817,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=28,
            n_events=32268860,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=31853547,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
        ),
    ),
)

# 15.07.2024: updated to NanoAODv12-130X (hdamp samples not updated)
# dileptonic decay
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=TTto2L2Nu%28_Hdamp-*%7C_MT-17%281%7C3%29p5%29%3F_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="tt_dl_powheg",
    id=14707644,
    is_data=False,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=23765566,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=9621248,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=9943000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=12,
            n_events=9824455,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=9943673,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=12,
            n_events=9831244,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=9730000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
        ),
    ),
)


# fully hadronic decay
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=TTto4Q%28_Hdamp-*%7C_MT-17%281%7C3%29p5%29%3F_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="tt_fh_powheg",
    id=14708054,
    is_data=False,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=46,
            n_events=53419472,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=22548206,
        ),
        # missing as of 2023-07-01
        # tune_down=DatasetInfo(
        #     keys=[
        #         "/TTto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=None,
        #     n_events=None,
        # ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=21658498,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=23430687,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=21873176,
        ),
        # missing as of 2023-07-01
        # cr_2=DatasetInfo(
        #     keys=[
        #         "/TTto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=None,
        #     n_events=None,
        # ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
        ),
    ),
)

#
# single top (t-channel)
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=%28TBbar%7CTbarB%29Q_t-channel&chained_request=Premix  # noqa

# t-channel (top)
cpn.add_dataset(
    name="st_tchannel_t_powheg",
    id=14635077,
    is_data=False,
    processes=[procs.st_tchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=2,
            n_events=2973675,
        ),
    ),
)

# t-channel (anti-top)
cpn.add_dataset(
    name="st_tchannel_tbar_powheg",
    id=14619151,
    is_data=False,
    processes=[procs.st_tchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=2,
            n_events=1488752,
        ),
    ),
)

#
# single-top (tW-channel)
#

# semileptonic decay (top)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=TWminustoLNu2Q*_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
# nominal missing as of 2023-07-01
# cpn.add_dataset(
#     name="st_twchannel_t_sl_powheg",
#     id=None,
#     is_data=False,
#     processes=[procs.st_twchannel_t_sl],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=None,
#             n_events=None,
#         ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "/TWminustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=5,
#             n_events=4943120,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "/TWminustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=4,
#             n_events=4587700,
#         ),
#         cr_1=DatasetInfo(
#             keys=[
#                 "/TWminustoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=5,
#             n_events=4593174,
#         ),
#         cr_2=DatasetInfo(
#             keys=[
#                 "/TWminustoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=4,
#             n_events=4676221,
#         ),
#     ),
# )

# semileptonic decay (anti-top)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=TbarWplustoLNu2Q*_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
# nominal missing as of 2023-07-01
# cpn.add_dataset(
#     name="st_twchannel_tbar_sl_powheg",
#     id=None,
#     is_data=False,
#     processes=[procs.st_twchannel_tbar_sl],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=None,
#             n_events=None,
#         ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "/TbarWplustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=None,
#             n_events=None,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "/TbarWplustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=None,
#             n_events=None,
#         ),
#         cr_1=DatasetInfo(
#             keys=[
#                 "/TbarWplustoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=4,
#             n_events=4728679,
#         ),
#         cr_2=DatasetInfo(
#             keys=[
#                 "/TbarWplustoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=4,
#             n_events=4633416,
#         ),
#     ),
# )

# dileptonic decay (top)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=TWminusto2L2Nu*_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="st_twchannel_t_dl_powheg",
    id=14678180,
    is_data=False,
    processes=[procs.st_twchannel_t_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=2435564,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=2375416,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=2385737,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=2492355,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=3,
            n_events=2497224,
        ),
    ),
)

# dileptonic decay (anti-top)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=TbarWplusto2L2Nu*_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="st_twchannel_tbar_dl_powheg",
    id=14690995,
    is_data=False,
    processes=[procs.st_twchannel_tbar_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=3,
            n_events=2401536,
        ),
        # missing as of 2023-07-01
        # tune_up=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=None,
        #     n_events=None,
        # ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=2,
            n_events=2422160,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=2425480,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=2496520,
        ),
    ),
)


# fully hadronic decay (top)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=TWminusto4Q*_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="st_twchannel_t_fh_powheg",
    id=14691168,
    is_data=False,
    processes=[procs.st_twchannel_t_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=3924210,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=3853959,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=3822520,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=3800301,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=3862996,
        ),
    ),
)


# fully hadronic decay (anti-top)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=TbarWplusto4Q*_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="st_twchannel_tbar_fh_powheg",
    id=14691156,
    is_data=False,
    processes=[procs.st_twchannel_t_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=3957160,
        ),
        # tune_up=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=None,
        #     n_events=None,
        # ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=3971608,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=3823795,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=3862163,
        ),
    ),
)

#
# TT + X
#

cpn.add_dataset(
    name="ttll_mll_4to50_amcatnlo",
    id=14793589,
    processes=[procs.ttll_mll_m4to50],
    keys=[
            "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        ],
    n_files=25,
    n_events=300000,
)

cpn.add_dataset(
    name="ttll_mll_50_amcatnlo",
    id=14793929,
    processes=[procs.ttll_mll_m50],
    keys=[
            "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        ],
    n_files=28,
    n_events=400000,
)


cpn.add_dataset(
    name="tthjettononbb_m125_amcatnlo",
    id=14852673,
    processes=[procs.tthjetstononbb],
    keys=[
            "/TTHtoNon2B-1Jets_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        ],
    n_files=165,
    n_events=6303497,
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
    id=14836097,
    processes=[procs.ttlnu],
    keys=[
            "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
        ],
    n_files=1,
    n_events=111308,
)

#
# TT + XX
# TODO process xsecs unknown!!
#

cpn.add_dataset(
    name="ttww_madgraph",
    id=14797430,
    processes=[procs.ttww],
    keys=[
            "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        ],
    n_files=23,
    n_events=448443,
)

cpn.add_dataset(
    name="ttzz_madgraph",
    id=14800072,
    processes=[procs.ttzz],
    keys=[
            "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        ],
    n_files=22,
    n_events=443238,
)

cpn.add_dataset(
    name="ttwh_madgraph",
    id=14860507,
    processes=[procs.ttwh],
    keys=[
            "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        ],
    n_files=25,
    n_events=790196,
)

# TODO update to NanoAODv12 once available
cpn.add_dataset(
    name="tttt_amcatnlo",
    id=14795232,
    processes=[procs.tttt],
    keys=[
            "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        ],
    n_files=47,
    n_events=2396925,
)

cpn.add_dataset(
   name="ttzh_madgraph",
   id=14861662,
   processes=[procs.ttzh],
   keys=[
           "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
       ],
   n_files=43,
   n_events=798996,
)

#
# Single Top + X(X/q)
#

cpn.add_dataset(
    name="twztoll_thad_wlept_dr1_amcatnlo",
    id=14885205,
    processes=[procs.twztoll_thad_wlept_dr1],
    keys=[
            "/TWZ_Tto2Q_WtoLNu_Zto2L_DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM",  # noqa
        ],
    n_files=11,
    n_events=57035,
)

cpn.add_dataset(
    name="twztoll_thad_wlept_dr2_amcatnlo",
    id=14868457,
    processes=[procs.twztoll_thad_wlept_dr2],
    keys=[
            "/TWZ_Tto2Q_WtoLNu_Zto2L_DR2_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
        ],
    n_files=24,
    n_events=533582,
)

cpn.add_dataset(
    name="twztoll_tlept_whad_dr1_amcatnlo",
    id=14882755,
    processes=[procs.twztoll_tlept_whad_dr1],
    keys=[
            "/TWZ_TtoLNu_Wto2Q_Zto2L_DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM",  # noqa
        ],
    n_files=13,
    n_events=137368,
)


cpn.add_dataset(
    name="twztoll_tlept_whad_dr2_amcatnlo",
    id=14868174,
    processes=[procs.twztoll_tlept_whad_dr2],
    keys=[
            "/TWZ_TtoLNu_Wto2Q_Zto2L_DR2_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
        ],
    n_files=24,
    n_events=557276,
)

cpn.add_dataset(
    name="twztoll_tlept_wlept_dr1_amcatnlo",
    id=14885080,
    processes=[procs.twztoll_tlept_wlept_dr1],
    keys=[
            "/TWZ_TtoLNu_WtoLNu_Zto2L_DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM",  # noqa
        ],
    n_files=22,
    n_events=95807,
)

cpn.add_dataset(
    name="twztoll_tlept_wlept_dr2_amcatnlo",
    id=14870857,
    processes=[procs.twztoll_tlept_wlept_dr2],
    keys=[
            "/TWZ_TtoLNu_WtoLNu_Zto2L_DR2_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
        ],
    n_files=21,
    n_events=223130,
)

cpn.add_dataset(
   name="tzq_ll_4f_ckm_amcatnlo",
   id=14916923,
   processes=[procs.tzq],
   keys=[
           "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
       ],
   n_files=32,
   n_events=889780,
)
