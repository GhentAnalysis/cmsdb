# coding: utf-8

"""
ParticleNet tagger top quark datasets for the 2018 data-taking campaign
Credit to Juhee Song for providing the datasets
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_v9 import campaign_run2_2018_nano_v9 as cpn


#
# st
#

cpn.add_dataset(
    name="st_tchannel_t_powheg_PNET",
    id=142939030,  # 0
    processes=[procs.st_tchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/2018UL/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
            ],
            n_files=149,
            n_events=178336000,
        ),
    ),
)

cpn.add_dataset(
    name="st_tchannel_tbar_powheg_PNET",
    id=142967560,  # 0
    processes=[procs.st_tchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/2018UL/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
            ],
            n_files=130,
            n_events=95627000,
        ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_t_PNET",
    id=142488300,  # 0
    processes=[procs.st_twchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/2018UL/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
            ],
            n_files=52,
            n_events=7956000,
        ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_tbar_PNET",
    id=142537780,  # 0
    processes=[procs.st_twchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/2018UL/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
            ],
            n_files=23,
            n_events=7749000,
        ),
    ),
)

#
# ttbar
#

cpn.add_dataset(
    name="tt_sl_powheg_PNET",
    id=142354370,  # 0
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/2018UL/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
            ],
            n_files=391,
            n_events=476408000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_dl_powheg_PNET",
    id=142344740,  # NOTE adding a last 0 to the id to avoid conflicts with the original tt_dl_powheg
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/2018UL/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
            ],
            n_files=3061,
            n_events=145020000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_powheg_PNET",
    id=142320680,  # 0
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/2018UL/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
            ],
            n_files=339,
            n_events=334206000,
        ),
    ),
)

#
# TT + X
#

cpn.add_dataset(
    name="ttztollnunu_m10_amcatnlo_PNET",
    id=142531370,  # 0
    processes=[procs.ttz_zlep_m10toinf],
    keys=[
            "/2018UL/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
        ],
    n_files=21,
    n_events=19608000,
)

cpn.add_dataset(
    name="ttztoll_m1to10_amcatnlo_PNET",
    id=143388130,  # 0
    processes=[procs.ttz_zlep_m1to10],
    keys=[
            "/2018UL/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
        ],
    n_files=7,
    n_events=994000,
)

cpn.add_dataset(
    name="tthjettononbb_m125_amcatnlo_PNET",
    id=142308710,  # 0
    processes=[procs.tth_hnonbb_1j],
    keys=[
            "/2018UL/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
        ],
    n_files=51,
    n_events=9852567,
)

cpn.add_dataset(
    name="ttgamma_dilept_PNET",
    id=142603510,  # 0
    processes=[procs.ttgamma_dilept],
    keys=[
            "/2018UL/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
        ],
    n_files=15,
    n_events=14694000,
)

cpn.add_dataset(
    name="ttwjetstoln_amcatnlo_PNET",
    id=142323230,  # 0
    processes=[procs.ttw_wlnu],
    keys=[
            "/2018UL/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
        ],
    n_files=13,
    n_events=10450000,
)
#
# TT + XX
#

cpn.add_dataset(
    name="ttww_madgraph_PNET",
    id=142354410,  # 0
    processes=[procs.ttww],
    keys=[
            "/2018UL/TTWW_TuneCP5_13TeV-madgraph-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
        ],
    n_files=3,
    n_events=944000,
)

cpn.add_dataset(
    name="ttwz_madgraph_PNET",
    id=142347810,  # 0
    processes=[procs.ttwz],
    keys=[
            "/2018UL/TTWZ_TuneCP5_13TeV-madgraph-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
        ],
    n_files=2,
    n_events=498000,
)

cpn.add_dataset(
    name="ttzz_madgraph_PNET",
    id=142423070,  # 0
    processes=[procs.ttzz],
    keys=[
            "/2018UL/TTZZ_TuneCP5_13TeV-madgraph-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
        ],
    n_files=8,
    n_events=498000,
)

cpn.add_dataset(
    name="tthh_madgraph_PNET",
    id=142861400,  # 0
    processes=[procs.tthh],
    keys=[
            "/2018UL/TTHH_TuneCP5_13TeV-madgraph-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
        ],
    n_files=13,
    n_events=500000,
)

cpn.add_dataset(
    name="ttwh_madgraph_PNET",
    id=142853920,  # 0
    processes=[procs.ttwh],
    keys=[
            "/2018UL/TTWH_TuneCP5_13TeV-madgraph-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
        ],
    n_files=4,
    n_events=497000,
)

cpn.add_dataset(
    name="ttzh_madgraph_PNET",
    id=142861900,  # 0
    processes=[procs.ttzh],
    keys=[
            "/2018UL/TTZH_TuneCP5_13TeV-madgraph-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
        ],
    n_files=17,
    n_events=500000,
)

cpn.add_dataset(
    name="tttt_amcatnlo_PNET",
    id=142848320,  # 0
    processes=[procs.tttt],
    keys=[
            "/2018UL/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
        ],
    n_files=49,
    n_events=13058000,
)

#
# Single Top + X
#

cpn.add_dataset(
    name="twz_tqq_wlnu_zll_dr1_amcatnlo_PNET",
    id=142313840,  # 0
    processes=[procs.twz_tqq_wlnu_zll_dr1],
    keys=[
            "/2018UL/TWZToLL_thad_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
        ],
    n_files=32,
    n_events=2976000,
)

cpn.add_dataset(
    name="twz_tlnu_wqq_zll_dr1_amcatnlo_PNET",
    id=147281510,  # 0
    processes=[procs.twz_tlnu_wqq_zll_dr1],
    keys=[
            "/2018UL/TWZToLL_tlept_Whad_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
        ],
    n_files=12,
    n_events=9806000,
)

cpn.add_dataset(
    name="twz_tlnu_wlnu_zll_dr1_amcatnlo_PNET",
    id=142313680,  # 0
    processes=[procs.twz_tlnu_wlnu_zll_dr1],
    keys=[
            "/2018UL/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
        ],
    n_files=10,
    n_events=1000000,
)

cpn.add_dataset(
    name="tzq_ll_4f_ckm_amcatnlo_PNET",
    id=143003610,  # 0
    processes=[procs.tzq],
    keys=[
            "/2018UL/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
        ],
    n_files=14,
    n_events=11916000,
)
