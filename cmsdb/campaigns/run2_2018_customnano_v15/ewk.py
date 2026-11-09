# coding: utf-8

"""
Ewk datasets for the 2018 data-taking campaign
"""
from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_customnano_v15 import campaign_run2_2018_customnano_v15 as cpn

cpn.add_dataset(
    name="dy_m10to50_amcatnlo",
    id=3396957,
    processes=[procs.dy_m10to50],
    keys=[
        "/DYJetsToLL_M-10to50_TuneCP5_13TeV-amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=759,
    n_events=99177236,
)

cpn.add_dataset(
    name="dy_m50toinf_amcatnlo",
    id=3396969,
    processes=[procs.dy_m50toinf],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1236,
    n_events=196626007,
)

cpn.add_dataset(
    name="wz_wlnu_zll_amcatnlo",
    id=3396998,
    processes=[procs.wz_wlnu_zll],
    keys=[
        "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=66,
    n_events=9821283,
)

cpn.add_dataset(
    name="dyg_zll_amcatnlo",
    id=3396988,
    processes=[procs.dyg_ztoll_5f],
    keys=[
        "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=328,
    n_events=29919798,
)

cpn.add_dataset(
    name="zz_zll_zll_powheg",
    id=3396991,
    processes=[procs.zz_zll_zll],
    keys=[
        "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=659,
    n_events=99191000,
)

cpn.add_dataset(
    name="ww_ss_madgraph",
    id=3396992,
    processes=[procs.ss_ww],
    keys=[
        "/SSWW_TuneCP5_13TeV-madgraph-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=18,
    n_events=998000,
)

cpn.add_dataset(
    name="www_amcatnlo",
    id=3396958,
    processes=[procs.www],
    keys=[
        "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=4,
    n_events=240000,
)

cpn.add_dataset(
    name="wwz_amcatnlo",
    id=3396948,
    processes=[procs.wwz],
    keys=[
        "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=5,
    n_events=248000,
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=3397028,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=94,
    n_events=9994000,
)

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=3396961,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=104,
    n_events=9889000,
)

cpn.add_dataset(
    name="ggtozzto2e2mu_mcfm",
    id=3396967,
    processes=[procs.ggtozzto2e2mu],
    keys=[
        "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=11,
    n_events=500000,
)

cpn.add_dataset(
    name="ggtozzto2e2tau_mcfm",
    id=3397001,
    processes=[procs.ggtozzto2e2tau],
    keys=[
        "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=6,
    n_events=500000,
)

cpn.add_dataset(
    name="ggtozzto2mu2tau_mcfm",
    id=3396970,
    processes=[procs.ggtozzto2mu2tau],
    keys=[
        "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=10,
    n_events=496000,
)

cpn.add_dataset(
    name="ggtozzto4e_mcfm",
    id=3396968,
    processes=[procs.ggtozzto4e],
    keys=[
        "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=19,
    n_events=974000,
)

cpn.add_dataset(
    name="ggtozzto4mu_mcfm",
    id=3396959,
    processes=[procs.ggtozzto4mu],
    keys=[
        "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=19,
    n_events=845232,
)

cpn.add_dataset(
    name="ggtozzto4tau_mcfm",
    id=3396944,
    processes=[procs.ggtozzto4tau],
    keys=[
        "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIISummer20UL18MiniAODv2-106X_v16-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=8,
    n_events=493998,
)
