# coding: utf-8

"""
top quark datasets for the 2018 data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_HIPM_nano_v9 import campaign_run2_2016_HIPM_nano_v9 as cpn


#
# ttbar
#

cpn.add_dataset(
    name="st_tchannel_t_powheg",
    id=14265728,
    processes=[procs.st_tchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"  # noqa
            ],
            n_files=49,
            n_events=55961000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5up_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=21927000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5down_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=22073000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_hdampup_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=26,
            n_events=22147000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_hdampdown_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=22237000,
        ),
        cr1_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5CR1_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=43,
            n_events=19928000,
        ),
        cr2_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5CR2_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=21590000,
        ),
        erd_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_erdON_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=22933000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_mtop1715_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=21,
            n_events=22239000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_mtop1735_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=22499000,
        ),
        wtop_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_wtop0p85_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=21012000,
        ),
        wtop_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_wtop1p15_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=54,
            n_events=22534000,
        ),
    ),
)

cpn.add_dataset(
    name="st_tchannel_tbar_powheg",
    id=14258662,
    processes=[procs.st_tchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=46,
            n_events=31024000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5up_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=10715000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5down_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=10854000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_hdampup_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=37,
            n_events=10555000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_hdampdown_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=10781000,
        ),
        cr1_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5CR1_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=43,
            n_events=19928000,
        ),
        cr2_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5CR2_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=21590000,
        ),
        erd_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_erdON_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=22933000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_mtop1715_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=17,
            n_events=10626000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_mtop1735_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=13,
            n_events=11101000,
        ),
        wtop_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_wtop0p85_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=17,
            n_events=11123000,
        ),
        wtop_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_wtop1p15_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=11091000,
        ),
    ),
)

cpn.add_dataset(
    name="st_tchannel_antitop_5f_powheg",
    id=14339795,
    processes=[procs.st_tchannel_tbar],
    keys=[
        "/ST_t-channel_antitop_5f_InclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=47,
    n_events=24681000,
)

cpn.add_dataset(
    name="st_tchannel_top_5f_powheg",
    id=14234915,
    processes=[procs.st_tchannel_t],
    keys=[
        "/ST_t-channel_top_5f_InclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=56994000,
)


cpn.add_dataset(
    name="st_twchannel_t",
    id=14238236,
    processes=[procs.st_twchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=2300000,
        ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_tbar",
    id=14238490,
    processes=[procs.st_twchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=2300000,
        ),
    ),
)

cpn.add_dataset(
    name="st_schannel_had_4f_amcatnlo",
    id=14378334,
    processes=[procs.st_schannel_had],
    keys=[
        "/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=4700000,
)

cpn.add_dataset(
    name="st_schannel_lep_4f_amcatnlo",
    id=14232944,
    processes=[procs.st_schannel_lep],
    keys=[
        "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=5518000,
)

cpn.add_dataset(
    name="tt_sl_powheg",
    id=14232860,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=117,
            n_events=132178000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=58,
            n_events=46263000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=48,
            n_events=55514300,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=51,
            n_events=56968000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=58,
            n_events=47234000,
        ),
        cr1_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=56166000,
        ),
        cr2_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=54,
            n_events=56324000,
        ),
        erd_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=57,
            n_events=55704000,
        ),
        rtt_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_RTT_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
            ],
            n_files=468,
            n_events=99911584,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=48,
            n_events=53342000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=53,
            n_events=55376000,
        ),
        wtop_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_widthx0p85_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=74,
            n_events=63682000,
        ),
        wtop_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_widthx1p15_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=119,
            n_events=63806000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_dl_powheg",
    id=14232826,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=33,
            n_events=37505000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=10381000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=21583000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=42,
            n_events=14865000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=18,
            n_events=16973000,
        ),
        cr1_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=15518000,
        ),
        cr2_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=17,
            n_events=16776000,
        ),
        erd_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=16229000,
        ),
        rtt_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5_RTT_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
            ],
            n_files=297,
            n_events=43895234,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=21,
            n_events=16828000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=16848000,
        ),
        wtop_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_widthx0p85_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=15637000,
        ),
        wtop_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_widthx1p15_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=16886000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_powheg",
    id=14236766,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=79,
            n_events=97260000,
        ),
    ),
)
