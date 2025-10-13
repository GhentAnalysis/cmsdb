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

#
# t channel
#

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

#
# tW
#

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

#
# TT + X
#

cpn.add_dataset(
    name="ttz_zll_m4to50_amcatnlo",
    id=15390973,
    processes=[procs.ttz_zll_m4to50],
    keys=[
        "/TTLL_Bin-MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=37,
    n_events=2965000,
)

cpn.add_dataset(
    name="ttz_zll_m50toinf_amcatnlo",
    id=15390855,
    processes=[procs.ttz_zll_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTLL_Bin-MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=47,
            n_events=3952000,
        ),
    ),
)

cpn.add_dataset(
    name="ttw_wlnu_ewk_amcatnlo",
    id=15370310,
    processes=[procs.ttw_wlnu_ewk],
    keys=[
        "/TTLNu-EWK_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=38,
    n_events=2999000,
)

#
# TT + XX
#

cpn.add_dataset(
    name="ttww_madgraph",
    id=15393150,
    processes=[procs.ttww],
    keys=[
        "/TTWW_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=56,
    n_events=5801000,
)

cpn.add_dataset(
    name="ttwz_madgraph",
    id=15393070,
    processes=[procs.ttwz],
    keys=[
        "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=51,
    n_events=5529000,
)

# cpn.add_dataset(
#     name="ttzz_madgraph",
#     id=14800072,
#     processes=[procs.ttzz],
#     keys=[
#         "/TTZZ_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=0,
#     n_events=0,
# )

cpn.add_dataset(
    name="tzq_zll_4f_m30toinf_amcatnlo",
    id=15393166,
    processes=[procs.tzq],
    keys=[
        "/TZQB-Zto2L-4FS_Bin-MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-Madgraph_2_6_5_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=73,
    n_events=8839000,
)