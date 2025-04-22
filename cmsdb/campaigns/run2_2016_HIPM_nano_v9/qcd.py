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
    name="qcd_mu_pt15to20",
    id=14342952,
    processes=[procs.qcd_mu_pt15to20],
    keys=[
        "/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=4749558,
)

cpn.add_dataset(
    name="qcd_mu_pt20to30",
    id=14304959,
    processes=[procs.qcd_mu_pt20to30],
    keys=[
        "/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=50,
    n_events=31926643,
)

cpn.add_dataset(
    name="qcd_mu_pt30to50",
    id=14304936,
    processes=[procs.qcd_mu_pt30to50],
    keys=[
        "/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=47,
    n_events=28664840,
)


cpn.add_dataset(
    name="qcd_mu_pt50to80",
    id=14304086,
    processes=[procs.qcd_mu_pt50to80],
    keys=[
        "/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=29,
    n_events=19724658,
)


cpn.add_dataset(
    name="qcd_mu_pt80to120",
    id=14304990,
    processes=[procs.qcd_mu_pt80to120],
    keys=[
        "/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=55,
    n_events=21978558,
)

cpn.add_dataset(
    name="qcd_mu_pt120to170",
    id=14306090,
    processes=[procs.qcd_mu_pt120to170],
    keys=[
        "/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=19136907,
)

cpn.add_dataset(
    name="qcd_mu_pt170to300",
    id=14306082,
    processes=[procs.qcd_mu_pt170to300],
    keys=[
        "/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=63,
    n_events=37080544,
)

cpn.add_dataset(
    name="qcd_mu_pt300to470",
    id=14306135,
    processes=[procs.qcd_mu_pt300to470],
    keys=[
        "/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=28465385,
)

cpn.add_dataset(
    name="qcd_mu_pt470to600",
    id=14305904,
    processes=[procs.qcd_mu_pt470to600],
    keys=[
        "/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=48,
    n_events=19695298,
)

cpn.add_dataset(
    name="qcd_mu_pt600to800",
    id=14342580,
    processes=[procs.qcd_mu_pt600to800],
    keys=[
        "/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=62,
    n_events=19598815,
)

cpn.add_dataset(
    name="qcd_mu_pt800to1000",
    id=14306566,
    processes=[procs.qcd_mu_pt800to1000],
    keys=[
        "/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=80,
    n_events=38933940,
)

cpn.add_dataset(
    name="qcd_mu_pt1000",
    id=14306334,
    processes=[procs.qcd_mu_pt1000],
    keys=[
        "/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=42,
    n_events=13660999,
)




#
# QCD pt-binned (em enriched) samples
#

cpn.add_dataset(
    name="qcd_em_pt15to20",
    id=14432083,
    processes=[procs.qcd_em_pt15to20],
    keys=[
        "/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=42,
    n_events=4062805,
)

cpn.add_dataset(
    name="qcd_em_pt20to30",
    id=14414915,
    processes=[procs.qcd_em_pt20to30],
    keys=[
        "/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=7156441,
)

cpn.add_dataset(
    name="qcd_em_pt30to50",
    id=14307263,
    processes=[procs.qcd_em_pt30to50],
    keys=[
        "/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=4361931,
)

cpn.add_dataset(
    name="qcd_em_pt50to80",
    id=14307262,
    processes=[procs.qcd_em_pt50to80],
    keys=[
        "/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=5440758,
)

cpn.add_dataset(
    name="qcd_em_pt80to120",
    id=14307345,
    processes=[procs.qcd_em_pt80to120],
    keys=[
        "/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=4847354,
)

cpn.add_dataset(
    name="qcd_em_pt120to170",
    id=14307342,
    processes=[procs.qcd_em_pt120to170],
    keys=[
        "/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=4852573,
)

cpn.add_dataset(
    name="qcd_em_pt170to300",
    id=14306942,
    processes=[procs.qcd_em_pt170to300],
    keys=[
        "/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=1855461,
)


cpn.add_dataset(
    name="qcd_em_pt300toinf",
    id=14307347,
    processes=[procs.qcd_em_pt300toInf],
    keys=[
        "/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=1142775,
)