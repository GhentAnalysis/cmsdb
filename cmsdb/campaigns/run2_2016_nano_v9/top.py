# coding: utf-8

"""
top quark datasets for the 2018 data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_nano_v9 import campaign_run2_2016_nano_v9 as cpn


#
# ttbar
#

cpn.add_dataset(
    name="st_tchannel_t_powheg",
    id=14266078,
    processes=[procs.st_tchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=86,
            n_events=63073000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5up_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=25025000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5down_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=23751000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_hdampup_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=39,
            n_events=24584000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_hdampdown_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=25401000,
        ),
        cr1_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5CR1_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=25457000,
        ),
        cr2_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5CR2_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=23728000,
        ),
        erd_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_erdON_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=24527000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_mtop1715_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=24833000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_mtop1735_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=65,
            n_events=24764000,
        ),
        wtop_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_wtop0p85_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=72,
            n_events=24917000,
        ),
        wtop_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_wtop1p15_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=24643000,
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
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=35,
            n_events=30609000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5up_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=12591000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5down_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=12042000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_hdampup_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=12506000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_hdampdown_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=50,
            n_events=11902000,
        ),
        cr1_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5CR1_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=12557000,
        ),
        cr2_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5CR2_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=13,
            n_events=12213000,
        ),
        erd_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_erdON_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=34,
            n_events=12632000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_mtop1715_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=15,
            n_events=12661000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_mtop1735_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=14,
            n_events=12319000,
        ),
        wtop_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_wtop0p85_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=13,
            n_events=12604000,
        ),
        wtop_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_wtop1p15_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=12326000,
        ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_t",
    id=14238236,
    processes=[procs.st_twchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=2491000,
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
                "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=2554000,
        ),
    ),
)

cpn.add_dataset(
    name="st_schannel_had_4f_amcatnlo",
    id=14369560,
    processes=[procs.st_schannel_had],
    keys=[
        "/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=5300000,
)

cpn.add_dataset(
    name="st_schannel_lep_4f_amcatnlo",
    id=14341788,
    processes=[procs.st_schannel_lep],
    keys=[
        "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=5471000,
)

cpn.add_dataset(
    name="tt_sl_powheg",
    id=14232860,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=138,
            n_events=144722000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=56,
            n_events=57909000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=21,
            n_events=19427000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=58,
            n_events=60762000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=51,
            n_events=60649000,
        ),
        cr1_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=67,
            n_events=61029000,
        ),
        cr2_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=62693000,
        ),
        erd_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=65,
            n_events=54573000,
        ),
        rtt_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_RTT_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
            ],
            n_files=606,
            n_events=92581792,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=56,
            n_events=62661000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=57,
            n_events=62827000,
        ),
        wtop_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_widthx0p85_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=71,
            n_events=57310000,
        ),
        wtop_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_widthx1p15_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=90,
            n_events=57310000,
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
                "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=49,
            n_events=43546000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=42,
            n_events=18066000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=18305000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=18790000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=18,
            n_events=18100999,
        ),
        cr1_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=18121000,
        ),
        cr2_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=17,
            n_events=18015000,
        ),
        erd_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=28,
            n_events=17506000,
        ),
        rtt_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5_RTT_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
            ],
            n_files=325,
            n_events=48987022,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=72,
            n_events=16976000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=18601000,
        ),
        wtop_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_widthx0p85_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=40,
            n_events=18449000,
        ),
        wtop_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_widthx1p15_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=26,
            n_events=17756000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_powheg",
    id=14231933,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=146,
            n_events=107067000,
        ),
    ),
)
