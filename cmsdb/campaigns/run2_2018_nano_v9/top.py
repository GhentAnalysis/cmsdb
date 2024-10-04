# coding: utf-8

"""
top quark datasets for the 2018 data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_v9 import campaign_run2_2018_nano_v9 as cpn


#
# ttbar
#

cpn.add_dataset(
    name="st_tchannel_t_powheg",
    id=14293903,
    processes=[procs.st_tchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=149,
            n_events=178336000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5up_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=90,
            n_events=75582000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5down_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=57,
            n_events=74992000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_hdampup_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=62,
            n_events=59030000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_hdampdown_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=104,
            n_events=73014000,
        ),
    ),
)

cpn.add_dataset(
    name="st_tchannel_tbar_powheg",
    id=14296756,
    processes=[procs.st_tchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=130,
            n_events=95627000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5up_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=44,
            n_events=36424000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5down_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=55,
            n_events=36144000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_hdampup_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=37268000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_hdampdown_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=37919000,
        ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_t",
    id=14248830,
    processes=[procs.st_twchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=52,
            n_events=7956000,
        ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_tbar",
    id=14253778,
    processes=[procs.st_twchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=7749000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_sl_powheg",
    id=14235437,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=391,
            n_events=476408000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=165,
            n_events=199394000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=156,
            n_events=189888000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=168,
            n_events=197814000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=171,
            n_events=193212000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_dl_powheg",
    id=14234474,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=155,
            n_events=145020000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=57064000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=59853000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=44,
            n_events=54048000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=58,
            n_events=59958000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_powheg",
    id=14232068,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=339,
            n_events=334206000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=114,
            n_events=136785999,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=131,
            n_events=139688000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=126,
            n_events=138026000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=113,
            n_events=139490000,
        ),
    ),
)

#
# TT + X
#

cpn.add_dataset(
    name="ttztollnunu_m10_amcatnlo",
    id=14253137,
    processes=[procs.ttz_zlep_m10toinf],
    keys=[
            "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
        ],
    n_files=21,
    n_events=19608000,
)

cpn.add_dataset(
    name="ttztoll_m1to10_amcatnlo",
    id=14338813,
    processes=[procs.ttz_zlep_m1to10],
    keys=[
            "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
        ],
    n_files=7,
    n_events=994000,
)

cpn.add_dataset(
    name="tthjettononbb_m125_amcatnlo",
    id=14230871,
    processes=[procs.tthjetstononbb],
    keys=[
            "/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
        ],
    n_files=51,
    n_events=9852567,
)

cpn.add_dataset(
    name="ttgamma_dilept",
    id=14260351,
    processes=[procs.ttgamma_dilept],
    keys=[
            "/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM ",  # noqa
        ],
    n_files=15,
    n_events=14694000,
)

cpn.add_dataset(
    name="ttwjetstolnu_amcatnlo",
    id=14232323,
    processes=[procs.ttw_lnu],
    keys=[
            "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
        ],
    n_files=13,
    n_events=10450000,
)
#
# TT + XX
#

cpn.add_dataset(
    name="ttww_madgraph",
    id=14235441,
    processes=[procs.ttww],
    keys=[
            "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
        ],
    n_files=3,
    n_events=944000,
)

cpn.add_dataset(
    name="ttwz_madgraph",
    id=14234781,
    processes=[procs.ttwz],
    keys=[
            "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
        ],
    n_files=2,
    n_events=498000,
)

cpn.add_dataset(
    name="ttzz_madgraph",
    id=14242307,
    processes=[procs.ttzz],
    keys=[
            "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
        ],
    n_files=8,
    n_events=498000,
)

cpn.add_dataset(
    name="tthh_madgraph",
    id=14286140,
    processes=[procs.tthh],
    keys=[
            "/TTHH_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
        ],
    n_files=13,
    n_events=500000,
)

cpn.add_dataset(
    name="ttwh_madgraph",
    id=14285392,
    processes=[procs.ttwh],
    keys=[
            "/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
        ],
    n_files=4,
    n_events=497000,
)

cpn.add_dataset(
    name="ttzh_madgraph",
    id=14286190,
    processes=[procs.ttzh],
    keys=[
            "/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
        ],
    n_files=17,
    n_events=500000,
)

cpn.add_dataset(
    name="tttt_amcatnlo",
    id=14284832,
    processes=[procs.tttt],
    keys=[
            "/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
        ],
    n_files=49,
    n_events=13058000,
)

#
# Single Top + X
#

cpn.add_dataset(
    name="twztoll_thad_wlept_dr1_amcatnlo",
    id=14231384,
    processes=[procs.twztoll_thad_wlept_dr1],
    keys=[
            "/TWZToLL_thad_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
        ],
    n_files=32,
    n_events=2976000,
)

cpn.add_dataset(
    name="twztoll_tlept_whad_dr1_amcatnlo",
    id=14728151,
    processes=[procs.twztoll_tlept_whad_dr1],
    keys=[
            "/TWZToLL_tlept_Whad_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
        ],
    n_files=12,
    n_events=9806000,
)

cpn.add_dataset(
    name="twztoll_tlept_wlept_dr1_amcatnlo",
    id=14231368,
    processes=[procs.twztoll_tlept_wlept_dr1],
    keys=[
            "/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
        ],
    n_files=10,
    n_events=1000000,
)

cpn.add_dataset(
    name="tzq_ll_4f_ckm_amcatnlo",
    id=14300361,
    processes=[procs.tzq],
    keys=[
            "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
        ],
    n_files=14,
    n_events=11916000,
)
