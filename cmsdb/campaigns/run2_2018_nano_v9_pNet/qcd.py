# coding: utf-8

"""
QCD datasets for the 2018 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_v9_pNet import campaign_run2_2018_nano_v9_pNet as cpn


cpn.add_dataset(
    name="qcd_ht50to100",
    id=140417147,
    processes=[procs.qcd_ht50to100],
    keys=[
        "/2018/QCD_HT50to100_TuneCP5_13TeV-madgraphMLM-pythia8/dev_Run2ULPuppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=20,
    n_events=38521609,
)
cpn.add_dataset(
    name="qcd_ht100to200",
    id=140417146,
    processes=[procs.qcd_ht100to200],
    keys=[
        "/2018/QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8/dev_Run2ULPuppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=39,
    n_events=78438757,
)
cpn.add_dataset(
    name="qcd_ht200to300",
    id=140417145,
    processes=[procs.qcd_ht200to300],
    keys=[
        "/2018/QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=68,
    n_events=61565494,
)
cpn.add_dataset(
    name="qcd_ht300to500",
    id=140417144,
    processes=[procs.qcd_ht300to500],
    keys=[
        "/2018/QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=64,
    n_events=57213303,
)
cpn.add_dataset(
    name="qcd_ht500to700",
    id=140417143,
    processes=[procs.qcd_ht500to700],
    keys=[
        "/2018/QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=80,
    n_events=61644502,
)
cpn.add_dataset(
    name="qcd_ht700to1000",
    id=140417142,
    processes=[procs.qcd_ht700to1000],
    keys=[
        "/2018/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=67,
    n_events=47664468,
)
cpn.add_dataset(
    name="qcd_ht1000to1500",
    id=140417141,
    processes=[procs.qcd_ht1000to1500],
    keys=[
        "/2018/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=26,
    n_events=15230975,
)
cpn.add_dataset(
    name="qcd_ht1500to2000",
    id=140417140,
    processes=[procs.qcd_ht1500to2000],
    keys=[
        "/2018/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=26,
    n_events=12063456,
)
cpn.add_dataset(
    name="qcd_ht2000",
    id=140417139,
    processes=[procs.qcd_ht2000],
    keys=[
        "/2018/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=14,
    n_events=5710430,
)


cpn.add_dataset(
    name="qcd_bgen_ht200to300",
    id=140417138,
    processes=[procs.qcd_bgen_ht200to300],
    keys=[
        "/2018/QCD_HT200to300_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=9,
    n_events=14830551,
)
cpn.add_dataset(
    name="qcd_bgen_ht300to500",
    id=140417137,
    processes=[procs.qcd_bgen_ht300to500],
    keys=[
        "/2018/QCD_HT300to500_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=12,
    n_events=14144826,
)
cpn.add_dataset(
    name="qcd_bgen_ht500to700",
    id=140417136,
    processes=[procs.qcd_bgen_ht500to700],
    keys=[
        "/2018/QCD_HT500to700_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=7,
    n_events=8015859,
)
cpn.add_dataset(
    name="qcd_bgen_ht700to1000",
    id=140417135,
    processes=[procs.qcd_bgen_ht700to1000],
    keys=[
        "/2018/QCD_HT700to1000_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=5,
    n_events=4642245,
)
cpn.add_dataset(
    name="qcd_bgen_ht1000to1500",
    id=140417134,
    processes=[procs.qcd_bgen_ht1000to1500],
    keys=[
        "/2018/QCD_HT1000to1500_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=1,
    n_events=1537452,
)
cpn.add_dataset(
    name="qcd_bgen_ht1500to2000",
    id=140417133,
    processes=[procs.qcd_bgen_ht1500to2000],
    keys=[
        "/2018/QCD_HT1500to2000_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=1,
    n_events=1263157,
)
cpn.add_dataset(
    name="qcd_bgen_ht2000",
    id=140417132,
    processes=[procs.qcd_bgen_ht2000],
    keys=[
        "/2018/QCD_HT2000toInf_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=2,
    n_events=1300672,
)
#
# QCD pt-binned (muon enriched) samples
#

cpn.add_dataset(
    name="qcd_mu_pt20to30_pythia",
    id=14295094,
    processes=[procs.qcd_mu_pt20to30],
    keys=[
        "/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=72,
    n_events=60640516,
)

cpn.add_dataset(
    name="qcd_mu_pt30to50_pythia",
    id=14288201,
    processes=[procs.qcd_mu_pt30to50],
    keys=[
        "/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=64,
    n_events=58737695,
)

cpn.add_dataset(
    name="qcd_mu_pt50to80_pythia",
    id=14291476,
    processes=[procs.qcd_mu_pt50to80],
    keys=[
        "/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=37,
    n_events=40022458,
)

cpn.add_dataset(
    name="qcd_mu_pt80to120_pythia",
    id=14294899,
    processes=[procs.qcd_mu_pt80to120],
    keys=[
        "/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=60,
    n_events=45494357,
)

cpn.add_dataset(
    name="qcd_mu_pt120to170_pythia",
    id=14268714,
    processes=[procs.qcd_mu_pt120to170],
    keys=[
        "/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=66,
    n_events=38022194,
)

cpn.add_dataset(
    name="qcd_mu_pt170to300_pythia",
    id=14272609,
    processes=[procs.qcd_mu_pt170to300],
    keys=[
        "/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=66,
    n_events=71870974,
)

cpn.add_dataset(
    name="qcd_mu_pt300to470_pythia",
    id=14278828,
    processes=[procs.qcd_mu_pt300to470],
    keys=[
        "/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=71,
    n_events=58949756,
)

cpn.add_dataset(
    name="qcd_mu_pt470to600_pythia",
    id=14276087,
    processes=[procs.qcd_mu_pt470to600],
    keys=[
        "/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=84,
    n_events=38453296,
)

cpn.add_dataset(
    name="qcd_mu_pt600to800_pythia",
    id=14275919,
    processes=[procs.qcd_mu_pt600to800],
    keys=[
        "/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=104,
    n_events=37197942,
)

cpn.add_dataset(
    name="qcd_mu_pt800to1000_pythia",
    id=14282456,
    processes=[procs.qcd_mu_pt800to1000],
    keys=[
        "/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=94,
    n_events=78942993,
)

cpn.add_dataset(
    name="qcd_mu_pt1000_pythia",
    id=14281945,
    processes=[procs.qcd_mu_pt1000],
    keys=[
        "/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=27427130,
)

#
# QCD pt-binned (electron enriched)
#

cpn.add_dataset(
    name="qcd_em_pt15to20_pythia",
    id=14351188,
    processes=[procs.qcd_em_pt15to20],
    keys=[
        "/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=36,
    n_events=7899865,
)

cpn.add_dataset(
    name="qcd_em_pt20to30_pythia",
    id=14334474,
    processes=[procs.qcd_em_pt20to30],
    keys=[
        "/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=14328846,
)

cpn.add_dataset(
    name="qcd_em_pt30to50_pythia",
    id=14270994,
    processes=[procs.qcd_em_pt30to50],
    keys=[
        "/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=8574589,
)

cpn.add_dataset(
    name="qcd_em_pt50to80_pythia",
    id=14272610,
    processes=[procs.qcd_em_pt50to80],
    keys=[
        "/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=10497272,
)

cpn.add_dataset(
    name="qcd_em_pt80to120_pythia",
    id=14271848,
    processes=[procs.qcd_em_pt80to120],
    keys=[
        "/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=9468372,
)

cpn.add_dataset(
    name="qcd_em_pt120to170_pythia",
    id=14265953,
    processes=[procs.qcd_em_pt120to170],
    keys=[
        "/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=9677904,
)

cpn.add_dataset(
    name="qcd_em_pt170to300_pythia",
    id=14271800,
    processes=[procs.qcd_em_pt170to300],
    keys=[
        "/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=3714642,
)

cpn.add_dataset(
    name="qcd_em_pt300toInf_pythia",
    id=14271788,
    processes=[procs.qcd_em_pt300toInf],
    keys=[
        "/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=2215994,
)
