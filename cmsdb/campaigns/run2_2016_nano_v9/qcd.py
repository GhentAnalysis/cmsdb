# coding: utf-8

"""
QCD datasets for the 2018 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_v9 import campaign_run2_2018_nano_v9 as cpn

#
# QCD pt-binned (muon enriched) samples
#


cpn.add_dataset(
    name="qcd_mu_pt15to20_pythia",
    id=14238188,
    processes=[procs.qcd_mu_pt15to20],
    keys=[
        "/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=4529975,
)

cpn.add_dataset(
    name="qcd_mu_pt20to30_pythia",
    id=14247731,
    processes=[procs.qcd_mu_pt20to30],
    keys=[
        "/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=30853571,
)

cpn.add_dataset(
    name="qcd_mu_pt30to50_pythia",
    id=14235547,
    processes=[procs.qcd_mu_pt30to50],
    keys=[
        "/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=35474172,
)


cpn.add_dataset(
    name="qcd_mu_pt50to80_pythia",
    id=14234462,
    processes=[procs.qcd_mu_pt50to80],
    keys=[
        "/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=21491325,
)

cpn.add_dataset(
    name="qcd_mu_pt80to120_pythia",
    id=14233884,
    processes=[procs.qcd_mu_pt80to120],
    keys=[
        "/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=43,
    n_events=22005632,
)

cpn.add_dataset(
    name="qcd_mu_pt120to170_pythia",
    id=14230015,
    processes=[procs.qcd_mu_pt120to170],
    keys=[
        "/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=31,
    n_events=19772747,
)

cpn.add_dataset(
    name="qcd_mu_pt170to300_pythia",
    id=14230308,
    processes=[procs.qcd_mu_pt170to300],
    keys=[
        "/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=71,
    n_events=34183334,
)

cpn.add_dataset(
    name="qcd_mu_pt300to470_pythia",
    id=14235600,
    processes=[procs.qcd_mu_pt300to470],
    keys=[
        "/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=31,
    n_events=29824712,
)

cpn.add_dataset(
    name="qcd_mu_pt470to600_pythia",
    id=14235048,
    processes=[procs.qcd_mu_pt470to600],
    keys=[
        "/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=19771458,
)

cpn.add_dataset(
    name="qcd_mu_pt600to800_pythia",
    id=14230791,
    processes=[procs.qcd_mu_pt600to800],
    keys=[
        "/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=57,
    n_events=18165741,
)

cpn.add_dataset(
    name="qcd_mu_pt800to1000_pythia",
    id=14230009,
    processes=[procs.qcd_mu_pt800to1000],
    keys=[
        "/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=83,
    n_events=38913226,
)

cpn.add_dataset(
    name="qcd_mu_pt1000_pythia",
    id=14235164,
    processes=[procs.qcd_mu_pt1000],
    keys=[
        "/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=13905446,
)
