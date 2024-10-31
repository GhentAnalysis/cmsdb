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
    name="dy_m50toinf",
    id=14235180,
    processes=[procs.dy_m50toinf],
    keys=[
        "/2018/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2",  # noqa
    ],
    n_files=123,
    n_events=196376161,
)

cpn.add_dataset(
    name="dy_m10to50",
    id=1423518500,  # 00 because the next one has the same id
    processes=[procs.dy_m10to50],
    keys=[
        "/2018/DYJetsToLL_M-10to50_TuneCP5_13TeV-amcatnloFXFX-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2",  # noqa
    ],
    n_files=75,
    n_events=99091883,
)

#
# W + jets
#

cpn.add_dataset(
    name="w_lnu_0j",
    id=14235183,
    processes=[procs.w_lnu_0j],
    keys=[
        "/2018/WJetsToLNu_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2",  # noqa
    ],
    n_files=91,
    n_events=168792158,
)

cpn.add_dataset(
    name="w_lnu_1j",
    id=14235182,
    processes=[procs.w_lnu_1j],
    keys=[
        "/2018/WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v1",  # noqa
    ],
    n_files=75,
    n_events=135579078,
)

cpn.add_dataset(
    name="w_lnu_2j",
    id=14235181,
    processes=[procs.w_lnu_2j],
    keys=[
        "/2018/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2",  # noqa
    ],
    n_files=96,
    n_events=94878342,
)


#
# ZZ
#

cpn.add_dataset(
    name="zz_llnunu",
    id=142299864,  # 0
    processes=[procs.zz_zll_znunu],
    keys=[
        "/2018/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v1",  # noqa
    ],
    n_files=32,
    n_events=56886000,
)

cpn.add_dataset(
    name="zz_qqll_m4",
    id=142299865,  # 0
    processes=[procs.zz_zqq_zll],
    keys=[
        "/2018/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2",  # noqa
    ],
    n_files=29,
    n_events=29357938,
)


cpn.add_dataset(
    name="zz_llll",
    id=142299866,  # 0
    processes=[procs.zz_zll_zll],
    keys=[
        "/2018/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2",  # noqa
    ],
    n_files=65,
    n_events=98705000,
)


#
# WW
#

cpn.add_dataset(
    name="ww_lnulnu",
    id=142299861,  # 0
    processes=[procs.ww_dl],
    keys=[
        "/2018/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2",  # noqa
    ],
    n_files=7,
    n_events=9994000,
)


#
# WZ
#

cpn.add_dataset(
    name="wz_qqll_m4",
    id=142299862,  # 0
    processes=[procs.wz_wqq_zll],
    keys=[
        "/2018/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2",  # noqa
    ],
    n_files=25,
    n_events=28576996,
)


cpn.add_dataset(
    name="wz_lllnu",
    id=142299863,  # 0
    processes=[procs.wz_wlnu_zll],
    keys=[
        "/2018/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2",  # noqa
    ],
    n_files=6,
    n_events=9821283,
)
