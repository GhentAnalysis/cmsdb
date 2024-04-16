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

#
# W + jets
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
    name="ZZTo4L",
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
    name="GluGLuToContinToZZTo2e2mu_mcfm",
    id=14241611,
    processes=[procs.ggtozzto2e2mu],
    keys=[
        "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=500000,
)

cpn.add_dataset(
    name="GluGLuToContinToZZTo2e2tau_mcfm",
    id=14242063,
    processes=[procs.ggtozzto2e2tau],
    keys=[
        "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=500000,
)

cpn.add_dataset(
    name="GluGLuToContinToZZTo2mu2tau_mcfm",
    id=14266664,
    processes=[procs.ggtozzto2mu2tau],
    keys=[
        "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=496000,
)

cpn.add_dataset(
    name="GluGLuToContinToZZTo4e_mcfm",
    id=14242982,
    processes=[procs.ggtozzto4e],
    keys=[
        "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=974000,
)

cpn.add_dataset(
    name="GluGLuToContinToZZTo4mu_mcfm",
    id=14266651,
    processes=[procs.ggtozzto4mu],
    keys=[
        "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=845232,
)

cpn.add_dataset(
    name="GluGLuToContinToZZTo4tau_mcfm",
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
    name="WWW_4F_amcatnlo",
    id=14229671,
    processes=[procs.www4f],
    keys=[
        "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=240000,
)

cpn.add_dataset(
    name="WWZ_4F_amcatnlo",
    id=14230361,
    processes=[procs.wwz4f],
    keys=[
        "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=248000,
)

cpn.add_dataset(
    name="WZZ_amcatnlo",
    id=14241104,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=9994000,
)

cpn.add_dataset(
    name="ZZZ_amcatnlo",
    id=14241940,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=60,
    n_events=9889000,
)
