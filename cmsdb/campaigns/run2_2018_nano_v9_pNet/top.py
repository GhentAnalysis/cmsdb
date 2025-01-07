# coding: utf-8

"""
ParticleNet tagger top quark datasets for the 2018 data-taking campaign
Credit to Juhee Song for providing the datasets
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_v9_pNet import campaign_run2_2018_nano_v9_pNet as cpn


#
# st
#

cpn.add_dataset(
    name="st_schannel_had",
    id=166366322, #0
    processes=[procs.st_schannel_had],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/2018/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
            ],
            n_files=15,
            n_events=16391000,
        ),
    ),
)

cpn.add_dataset(
    name="st_schannel_lep",
    id=166366355, #0
    processes=[procs.st_schannel_lep],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/2018/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v1", #noqa
            ],
            n_files=21,
            n_events=19365999,
        ),
    ),
)

cpn.add_dataset(
    name="st_tchannel_t_powheg",
    id=142939030, #0
    processes=[procs.st_tchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/2018/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v1", #noqa
            ],
            n_files=182,
            n_events=178397000,
        ),
    ),
)

cpn.add_dataset(
    name="st_tchannel_tbar_powheg",
    id=142967560, #0
    processes=[procs.st_tchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/2018/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v1", #noqa
            ],
            n_files=95,
            n_events=95785000,
        ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_t",
    id=142488300, #0
    processes=[procs.st_twchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/2018/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v1", #noqa
            ],
            n_files=11,
            n_events=11270430,
        ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_tbar",
    id=142537780, #0
    processes=[procs.st_twchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/2018/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v1", #noqa
            ],
            n_files=11,
            n_events=11015956,
        ),
    ),
)

#
# ttbar
#

cpn.add_dataset(
    name="tt_sl_powheg",
    id=142354370, #0
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/2018/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
            ],
            n_files=250,
            n_events=478982000,
        ),
    ),
)


cpn.add_dataset(
    name="tt_dl_powheg",
    id=142344740, #NOTE adding a last 0 to the id to avoid conflicts with the original tt_dl_powheg
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/2018/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v1"
            ],
            n_files=153,
            n_events=146010000,
        ),
    ),
)

#
# TT + X
#

cpn.add_dataset(
    name="ttz_zlep_m10toinf",
    id=142531370, #0
    processes=[procs.ttz_zlep_m10toinf],
    keys=[
        "/2018/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=20,
    n_events=19608000,
)

cpn.add_dataset(
    name="ttz_zqq",
    id=143388130, #0
    processes=[procs.ttz_zqq],
    keys=[
        "/2018/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v1", #noqa
    ],
    n_files=20,
    n_events=19816000,
)


cpn.add_dataset(
    name="tthtobb_powheg",
    id=142318710, #0
    processes=[procs.tth_hbb],
    keys=[
        "/2018/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=10,
    n_events=9599000,
)

cpn.add_dataset(
    name="tthtononbb_powheg",
    id=142348710, #0
    processes=[procs.tth_hnonbb],
    keys=[
        "/2018/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v2", #noqa
    ],
    n_files=8,
    n_events=7328993,
)



cpn.add_dataset(
    name="ttw_wlnu",
    id=142323230, #0
    processes=[procs.ttw_wlnu],
    keys=[
        "/2018/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v1", #noqa
    ],
    n_files=11,
    n_events=10468937,
)

cpn.add_dataset(
    name="ttw_wqq",
    id=142323231, #0
    processes=[procs.ttw_wqq],
    keys=[
        "/2018/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/NanoTuples-28Aug2023_Run2ULNanoAOD_AK4Puppi_RunIISummer20UL18MiniAODv2-106X_v16-v1", #noqa
    ],
    n_files=1,
    n_events=970179,
)
