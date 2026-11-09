# coding: utf-8

"""
Higgs datasets for the 2018 data-taking campaign
"""
from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_customnano_v15 import campaign_run2_2018_customnano_v15 as cpn

cpn.add_dataset(
    name="tth_hnonbb_1j_amcatnlo",
    id=3409349,
    processes=[procs.tth_hnonbb_1j],
    keys=[
        "/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=124,
    n_events=10051443,
)

cpn.add_dataset(
    name="vh_hnonbb_amcatnlo",
    id=3396999,
    processes=[procs.vh_hnonbb],
    keys=[
        "/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=12,
    n_events=1208288,
)

cpn.add_dataset(
    name="h_vbf_hzz_zll_zll_powheg",
    id=3396963,
    processes=[procs.h_vbf_hzz4l],
    keys=[
        "/VBF_HToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=7,
    n_events=477000,
)

cpn.add_dataset(
    name="h_ggf_hzz_zll_zqq_powheg",
    id=3396954,
    processes=[procs.h_ggf_hzz2l2q],
    keys=[
        "/GluGluHToZZTo2L2Q_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=19,
    n_events=998000,
)

cpn.add_dataset(
    name="h_ggf_hzz_zll_zll_powheg",
    id=3396978,
    processes=[procs.h_ggf_hzz4l],
    keys=[
        "/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=20,
    n_events=940000,
)
