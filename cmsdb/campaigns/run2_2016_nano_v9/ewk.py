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
    id=14480799,
    processes=[procs.dy_lep_m10to50],
    keys=[
        "/DYJetsToLL_M-10to50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=49267069,
)

cpn.add_dataset(
    name="dy_lep_m50_amcatnlo",
    id=14300699,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=41,
    n_events=71839442,
)


cpn.add_dataset(
    name="dy_lept_m50_ht-100to200_madgraph",
    id=14248856,
    processes=[procs.dy_lep_m50_ht100to200],
    keys=[
        "/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=43,
    n_events=8316351,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-200to400_madgraph",
    id=14252965,
    processes=[procs.dy_lep_m50_ht200to400],
    keys=[
        "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=5653782,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-400to600_madgraph",
    id=14276110,
    processes=[procs.dy_lep_m50_ht400to600],
    keys=[
        "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=2491416,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-600to800_madgraph",
    id=14255233,
    processes=[procs.dy_lep_m50_ht600to800],
    keys=[
        "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=2299853,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-800to1200_madgraph",
    id=14251557,
    processes=[procs.dy_lep_m50_ht800to1200],
    keys=[
        "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=36,
    n_events=2393976,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-1200to2500_madgraph",
    id=14256439,
    processes=[procs.dy_lep_m50_ht1200to2500],
    keys=[
        "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=1970857,
)

#
# W + jets
#

cpn.add_dataset(
    name="w_lnu_madgraph",
    id=14231010,  # id first dataset
    processes=[procs.w_lnu],
    keys=[
        "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
        "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=68 + 796,
    n_events=80958227 + 80465376,
)
