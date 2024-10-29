# coding: utf-8

"""
ParticleNet Electroweak datasets for the 2018 data-taking campaign
Credit to Juhee for providing the datasets:
/pnfs/iihe/cms/store/user/jusong/topNanoAOD
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_v9_pNet import campaign_run2_2018_nano_v9_pNet as cpn


#
# Drell-Yan
#
cpn.add_dataset(
    name="dy_lep_m50",
    id=14235180,
    processes=[procs.dy_lep_m50],
    keys=[
        "/2018/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2",
    ],
    n_files=123,
    n_events=196376161,
)

cpn.add_dataset(
    name="dy_lep_m10to50",
    id=1423518500, #00 because the next one has the same id
    processes=[procs.dy_lep_m10to50],
    keys=[
        "/2018/DYJetsToLL_M-10to50_TuneCP5_13TeV-amcatnloFXFX-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=75,
    n_events=99091883,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-100to200_madgraph",
    id=142351850, #0
    processes=[procs.dy_lep_m50_ht100to200],
    keys=[
        "/2018UL/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/TopNanoAODv9-1-1_2018UL",
    ],
    n_files=30,
    n_events=26202328,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-200to400_madgraph",
    id=142348900, #0
    processes=[procs.dy_lep_m50_ht200to400],
    keys=[
        "/2018UL/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/TopNanoAODv9-1-1_2018UL",
    ],
    n_files=21,
    n_events=18455718,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-400to600_madgraph",
    id=142313830, #0
    processes=[procs.dy_lep_m50_ht400to600],
    keys=[
        "/2018UL/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/TopNanoAODv9-1-1_2018UL",
    ],
    n_files=28,
    n_events=8682257,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-600to800_madgraph",
    id=142355740, #0
    processes=[procs.dy_lep_m50_ht600to800],
    keys=[
        "/2018UL/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/TopNanoAODv9-1-1_2018UL",
    ],
    n_files=11,
    n_events=7035971,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-800to1200_madgraph",
    id=142363170, #0
    processes=[procs.dy_lep_m50_ht800to1200],
    keys=[
        "/2018UL/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/TopNanoAODv9-1-1_2018UL",
    ],
    n_files=24,
    n_events=6554679,
)

cpn.add_dataset(
    name="dy_lept_m50_ht-1200to2500_madgraph",
    id=142353780, #0
    processes=[procs.dy_lep_m50_ht1200to2500],
    keys=[
        "/2018UL/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/TopNanoAODv9-1-1_2018UL",
    ],
    n_files=13,
    n_events=5966661,
)

#
# W + jets
#

cpn.add_dataset(
    name="w_lnu_0j",
    id=14235183,
    processes=[procs.w_lnu_0j],
    keys=[
        "/2018/WJetsToLNu_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=91,
    n_events=168792158,
) 

cpn.add_dataset(
    name="w_lnu_1j",
    id=14235182,
    processes=[procs.w_lnu_1j],
    keys=[
        "/2018/WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v1", #noqa
    ],
    n_files=75,
    n_events=135579078,
)

cpn.add_dataset(
    name="w_lnu_2j",
    id=14235181,
    processes=[procs.w_lnu_2j],
    keys=[
        "/2018/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=96,
    n_events=94878342,
)


#
# ZZ
#

cpn.add_dataset(
    name="zz_llnunu",
    id=142299864, #0
    processes=[procs.zz_llnunu],
    keys=[
        "/2018/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v1", #noqa
    ],
    n_files=32,
    n_events=56886000,
)

cpn.add_dataset(
    name="zz_qqll_m4",
    id=142299865, #0
    processes=[procs.zz_qqll_m4],
    keys=[
        "/2018/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=29,
    n_events=29357938,
)


cpn.add_dataset(
    name="zz_llll",
    id=142299866, #0
    processes=[procs.zz_llll],
    keys=[
        "/2018/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=65,
    n_events=98705000,
)





#
# WW
#

cpn.add_dataset(
    name="ww_pythia8",
    id=142299860, #0
    processes=[procs.ww],
    keys=[
        "/2018UL/WW_TuneCP5_13TeV-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
    ],
    n_files=31,
    n_events=15679000,
)

cpn.add_dataset(
    name="ww_lnulnu",
    id=142299861, #0
    processes=[procs.ww_lnulnu],
    keys=[
        "/2018/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=7,
    n_events=9994000,
)


#
# WZ
#

cpn.add_dataset(
    name="wz_qqll_m4",
    id=142299862, #0
    processes=[procs.wz_qqll_m4],
    keys=[
        "/2018/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=25,
    n_events=28576996,
)


cpn.add_dataset(
    name="wz_lllnu",
    id=142299863, #0
    processes=[procs.wz_lllnu],
    keys=[
        "/2018/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=6,
    n_events=9821283,
)


#

#
# triboson
#

cpn.add_dataset(
    name="www_4f_amcatnlo",
    id=142296710, #0
    processes=[procs.www4f],
    keys=[
        "/2018UL/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
    ],
    n_files=5,
    n_events=240000,
)

cpn.add_dataset(
    name="wwz_4f_amcatnlo",
    id=142303610, #0
    processes=[procs.wwz4f],
    keys=[
        "/2018UL/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
    ],
    n_files=5,
    n_events=248000,
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=142411040, #0
    processes=[procs.wzz],
    keys=[
        "/2018UL/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
    ],
    n_files=20,
    n_events=9994000,
)

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=142419400, #0
    processes=[procs.zzz],
    keys=[
        "/2018UL/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/TopNanoAODv9-1-1_2018UL",  # noqa
    ],
    n_files=60,
    n_events=9889000,
)
