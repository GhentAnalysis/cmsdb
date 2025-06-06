# coding: utf-8

"""
Electroweak datasets for the 2018 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_v9 import campaign_run2_2018_nano_v9 as cpn


#
# Drell-Yan
#

cpn.add_dataset(
    name="dy_lep_m10to50_amcatnlo",
    id=14529612,
    processes=[procs.dy_lep_m10to50],
    keys=[
        "/DYJetsToLL_M-10to50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=99177236,
)

cpn.add_dataset(
    name="dy_lep_m50_amcatnlo",
    id=14260276,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=204,
    n_events=195510810,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-100to200_madgraph",
    id=14235185,
    processes=[procs.dy_lep_m50_ht100to200],
    keys=[
        "/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
    ],
    n_files=30,
    n_events=26202328,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-200to400_madgraph",
    id=14234890,
    processes=[procs.dy_lep_m50_ht200to400],
    keys=[
        "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
    ],
    n_files=21,
    n_events=18455718,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-400to600_madgraph",
    id=14231383,
    processes=[procs.dy_lep_m50_ht400to600],
    keys=[
        "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
    ],
    n_files=28,
    n_events=8682257,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-600to800_madgraph",
    id=14235574,
    processes=[procs.dy_lep_m50_ht600to800],
    keys=[
        "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
    ],
    n_files=11,
    n_events=7035971,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-800to1200_madgraph",
    id=14236317,
    processes=[procs.dy_lep_m50_ht800to1200],
    keys=[
        "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
    ],
    n_files=24,
    n_events=6554679,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-1200to2500_madgraph",
    id=14235378,
    processes=[procs.dy_lep_m50_ht1200to2500],
    keys=[
        "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
    ],
    n_files=13,
    n_events=5966661,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-2500toinf_madgraph",
    id=14244277,
    processes=[procs.dy_lep_m50_ht2500toinf],
    keys=[
        "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=1978203,
)

#
# W + jets (LO)
#

cpn.add_dataset(
    name="w_lnu_madgraph",
    id=14230313,
    processes=[procs.w_lnu],
    keys=[
        "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",
        "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM",
    ],
    n_files=94 + 467,
    n_events=81051269 + 79645994,
)

cpn.add_dataset(
    name="w_lnu_ht70to100_madgraph",
    processes=[procs.w_lnu_ht70to100],
    id=14230395,
    keys=[
        '/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM',
        '/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v3/NANOAODSIM'
    ],
    n_files=97 + 669,
    n_events=66220256 + 72037044,
)

cpn.add_dataset(
    name="w_lnu_ht100to200_madgraph",
    processes=[procs.w_lnu_ht100to200],
    id=14302707,
    keys=[
        '/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM',
        '/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v3/NANOAODSIM'
    ],
    n_files=57 + 523,
    n_events=51408967 + 68556079,
)

cpn.add_dataset(
    name="w_lnu_ht200to400_madgraph",
    processes=[procs.w_lnu_ht200to400],
    id=14231286,
    keys=[
        '/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM',
        '/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v3/NANOAODSIM'
    ],
    n_files=101 + 780,
    n_events=58225632 + 59011717,
)

cpn.add_dataset(
    name="w_lnu_ht400to600_madgraph",
    processes=[procs.w_lnu_ht400to600],
    id=14230704,
    keys=[
        '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM',
        '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM',
        '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext2-v3/NANOAODSIM'
    ],
    n_files=44 + 27 + 177,
    n_events=7444030 + 1971444 + 9997677,
)

cpn.add_dataset(
    name="w_lnu_ht600to800_madgraph",
    processes=[procs.w_lnu_ht600to800],
    id=14230968,
    keys=[
        '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM',
        '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM',
        '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext2-v3/NANOAODSIM'
    ],
    n_files=33 + 35 + 254,
    n_events=7718765 + 5720014 + 15645953,
)

cpn.add_dataset(
    name="w_lnu_ht800to1200_madgraph",
    processes=[procs.w_lnu_ht800to1200],
    id=14228089,
    keys=[
        '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM',
        '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM',
        '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext2-v3/NANOAODSIM'
    ],
    n_files=11 + 32 + 199,
    n_events=7306187 + 5418842 + 14546732,
)

cpn.add_dataset(
    name="w_lnu_ht1200to2500_madgraph",
    processes=[procs.w_lnu_ht1200to2500],
    id=14299228,
    keys=[
        '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM',
        '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM',
        '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext2-v3/NANOAODSIM'
    ],
    n_files=8 + 51 + 172,
    n_events=6481518 + 6486269 + 14170096,
)

cpn.add_dataset(
    name="w_lnu_ht2500toinf_madgraph",
    processes=[procs.w_lnu_ht2500toinf],
    id=14279142,
    keys=[
        '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM',
        '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM',
        '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext2-v3/NANOAODSIM'
    ],
    n_files=51 + 50 + 241,
    n_events=2097648 + 10124647 + 15094137,
)

#
# W + Jets (NLO)
#

cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14294932,
    processes=[procs.w_lnu],
    keys=[
        "/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=54,
    n_events=29117828,
)


cpn.add_dataset(
    name="w_lnu_0j_amcatnlo",
    id=14253116,
    processes=[procs.w_lnu_0j],
    keys=[
        "/WJetsToLNu_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=102,
    n_events=172138190,
)

cpn.add_dataset(
    name="w_lnu_1j_amcatnlo",
    id=14230754,
    processes=[procs.w_lnu_1j],
    keys=[
        "/WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=149,
    n_events=183483106,
)

cpn.add_dataset(
    name="w_lnu_2j_amcatnlo",
    id=14299548,
    processes=[procs.w_lnu_2j],
    keys=[
        "/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=63,
    n_events=94925903,
)


#
# WZ
#

cpn.add_dataset(
    name="wz_lnuqq_amcatnlo",
    id=14375151,
    processes=[procs.wz_qqll_m4],
    keys=[
        "/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=7395487,
)

cpn.add_dataset(
    name="wz_lnununu_amcatnlo",
    id=14401982,
    processes=[procs.wz_lnununu_m4],
    keys=[
        "/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=2497292,
)

cpn.add_dataset(
    name="wz_lllnu_amcatnlo",
    id=14253602,
    processes=[procs.wz_lllnu],
    keys=[
        "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=9821283,
)

#
# ZZ
#

cpn.add_dataset(
    name="zzto4l_powheg",
    id=14241148,
    processes=[procs.zz_llll],
    keys=[
        "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=144,
    n_events=98488000,
)

#
# GluGlueToContinToZZ
#

cpn.add_dataset(
    name="gluglutocontintozzto2e2mu_mcfm",
    id=14241611,
    processes=[procs.ggtozzto2e2mu],
    keys=[
        "/gluglutocontintozzto2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=500000,
)

cpn.add_dataset(
    name="gluglutocontintozzto2e2tau_mcfm",
    id=14242063,
    processes=[procs.ggtozzto2e2tau],
    keys=[
        "/gluglutocontintozzto2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=500000,
)

cpn.add_dataset(
    name="gluglutocontintozzto2mu2tau_mcfm",
    id=14266664,
    processes=[procs.ggtozzto2mu2tau],
    keys=[
        "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=496000,
)

cpn.add_dataset(
    name="gluglutocontintozzto4e_mcfm",
    id=14242982,
    processes=[procs.ggtozzto4e],
    keys=[
        "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=974000,
)

cpn.add_dataset(
    name="gluglutocontintozzto4mu_mcfm",
    id=14266651,
    processes=[procs.ggtozzto4mu],
    keys=[
        "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=845232,
)

cpn.add_dataset(
    name="gluglutocontintozzto4tau_mcfm",
    id=14253997,
    processes=[procs.ggtozzto4tau],
    keys=[
        "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=493998,
)

#
# WW
#

cpn.add_dataset(
    name="ww_pythia8",
    id=14229986,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=31,
    n_events=15679000,
)


#
# triboson
#

cpn.add_dataset(
    name="www_4f_amcatnlo",
    id=14229671,
    processes=[procs.www4f],
    keys=[
        "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=240000,
)

cpn.add_dataset(
    name="wwz_4f_amcatnlo",
    id=14230361,
    processes=[procs.wwz4f],
    keys=[
        "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=248000,
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=14241104,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=9994000,
)

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=14241940,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=60,
    n_events=9889000,
)
