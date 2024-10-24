# coding: utf-8

"""
ParticleNet Electroweak datasets for the 2018 data-taking campaign
Credit to Juhee for providing the datasets:
/pnfs/iihe/cms/store/user/jusong/topNanoAOD
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_v9 import campaign_run2_2018_nano_v9 as cpn


#
# Drell-Yan
#
cpn.add_dataset(
    name="dy_lept_m10to50_madgraph_PNET",
    id=1423518500,  # 00 because the next one has the same id
    processes=[procs.dy_m10to50],
    keys=[
        "/2018UL/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/TopNanoAODv9-1-1_2018UL",
    ],
    n_files=30,
    n_events=26202328,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-100to200_madgraph_PNET",
    id=142351850,  # 0
    processes=[procs.dy_m50toinf_ht100to200],
    keys=[
        "/2018UL/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/TopNanoAODv9-1-1_2018UL",
    ],
    n_files=30,
    n_events=26202328,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-200to400_madgraph_PNET",
    id=142348900,  # 0
    processes=[procs.dy_m50toinf_ht200to400],
    keys=[
        "/2018UL/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/TopNanoAODv9-1-1_2018UL",
    ],
    n_files=21,
    n_events=18455718,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-400to600_madgraph_PNET",
    id=142313830,  # 0
    processes=[procs.dy_m50toinf_ht400to600],
    keys=[
        "/2018UL/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/TopNanoAODv9-1-1_2018UL",
    ],
    n_files=28,
    n_events=8682257,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-600to800_madgraph_PNET",
    id=142355740,  # 0
    processes=[procs.dy_m50toinf_ht600to800],
    keys=[
        "/2018UL/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/TopNanoAODv9-1-1_2018UL",
    ],
    n_files=11,
    n_events=7035971,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-800to1200_madgraph_PNET",
    id=142363170,  # 0
    processes=[procs.dy_m50toinf_ht800to1200],
    keys=[
        "/2018UL/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/TopNanoAODv9-1-1_2018UL",
    ],
    n_files=24,
    n_events=6554679,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-1200to2500_madgraph_PNET",
    id=142353780,  # 0
    processes=[procs.dy_m50toinf_ht1200to2500],
    keys=[
        "/2018UL/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/TopNanoAODv9-1-1_2018UL",
    ],
    n_files=13,
    n_events=5966661,
)

#
# W + jets
#

# TODO

#
# WZ
#


# TODO

#
# ZZ
#

# TODO


#
# WW
#

cpn.add_dataset(
    name="ww_pythia8_PNET",
    id=142299860,  # 0
    processes=[procs.ww],
    keys=[
        "/2018UL/WW_TuneCP5_13TeV-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
    ],
    n_files=31,
    n_events=15679000,
)


#
# triboson
#

cpn.add_dataset(
    name="www_4f_amcatnlo_PNET",
    id=142296710,  # 0
    processes=[procs.www],
    keys=[
        "/2018UL/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
    ],
    n_files=5,
    n_events=240000,
)

cpn.add_dataset(
    name="wwz_4f_amcatnlo_PNET",
    id=142303610,  # 0
    processes=[procs.wwz],
    keys=[
        "/2018UL/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
    ],
    n_files=5,
    n_events=248000,
)

cpn.add_dataset(
    name="wzz_amcatnlo_PNET",
    id=142411040,  # 0
    processes=[procs.wzz],
    keys=[
        "/2018UL/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
    ],
    n_files=20,
    n_events=9994000,
)

cpn.add_dataset(
    name="zzz_amcatnlo_PNET",
    id=142419400,  # 0
    processes=[procs.zzz],
    keys=[
        "/2018UL/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
    ],
    n_files=60,
    n_events=9889000,
)
