# coding: utf-8


from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn

#
# ttbar
#

# semileptonic decay
cpn.add_dataset(
    name="tt_sl_powheg",
    id=14693443,
    is_data=False,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=790,
            n_events=484475057,
        ),
    ),
)

cpn.add_dataset(
    name="tt_dl_powheg",
    id=15304231,
    is_data=False,
    processes=[procs.tt_dl],
    keys=[
        "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=780,
    n_events=470123263,
)


# t channel
cpn.add_dataset(
    name="st_tchannel_t_lep_powheg",
    processes=[procs.st_tchannel_t_lep],
    id=15316276,
    is_data=False,
    keys=[
        "/TBbarQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=391,
    n_events=44258039,
)
cpn.add_dataset(
    name="st_tchannel_tbar_lep_powheg",
    id=15316115,
    is_data=False,
    processes=[procs.st_tchannel_tbar_lep],
    keys=[
        "/TbarBQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=249,
    n_events=22102160,
)

# tW
cpn.add_dataset(
    name="st_twchannel_tbar_dl_powheg",
    id=15376044,
    is_data=False,
    processes=[procs.st_twchannel_tbar_dl],
    keys=[
        "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=90,
    n_events=15000000,
)
cpn.add_dataset(
    name="st_twchannel_t_dl_powheg",
    id=15376104,
    is_data=False,
    processes=[procs.st_twchannel_t_dl],
    keys=[
        "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=176,
    n_events=14998000,
)

cpn.add_dataset(
    name="st_twchannel_tbar_sl_powheg",
    id=15376087,
    is_data=False,
    processes=[procs.st_twchannel_tbar_sl],
    keys=[
        "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=252,
    n_events=29395659,
)
cpn.add_dataset(
    name="st_twchannel_t_sl_powheg",
    id=15377565,
    is_data=False,
    processes=[procs.st_twchannel_t_sl],
    keys=[
        "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=252,
    n_events=28763293,
)

cpn.add_dataset(
    name="st_twchannel_tbar_fh_powheg",
    id=15375023,
    is_data=False,
    processes=[procs.st_twchannel_tbar_fh],
    keys=[
        "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=195,
    n_events=24000000,
)
cpn.add_dataset(
    name="st_twchannel_t_fh_powheg",
    id=15375712,
    is_data=False,
    processes=[procs.st_twchannel_t_fh],
    keys=[
        "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=154,
    n_events=23999000,
)
