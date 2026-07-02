# coding: utf-8

"""
Top datasets for the 2024 data-taking campaign
"""
from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_customnano_v15 import campaign_run3_2024_customnano_v15 as cpn

cpn.add_dataset(
    name="tt_dl_powheg",
    id=3370666,
    processes=[procs.tt_dl],
    keys=[
        "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v3-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=5420,
    n_events=466380383,
)

cpn.add_dataset(
    name="tt_fh_powheg",
    id=3370641,
    processes=[procs.tt_fh],
    keys=[
        "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=5182,
    n_events=455390127,
)

cpn.add_dataset(
    name="tt_sl_powheg",
    id=3370665,
    processes=[procs.tt_sl],
    keys=[
        "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=5508,
    n_events=484298177,
)

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370581,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/TTBBto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=307,
#     n_events=12498392,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370634,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/TTBBto4Q_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=309,
#     n_events=14988225,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370636,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/TTBBtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=488,
#     n_events=22478238,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370736,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/TTto2L2Nu-BBDPS_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=276,
#     n_events=10725606,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370619,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/TTto4Q-BBDPS_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=327,
#     n_events=15752907,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370701,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/TTtoLNu2Q-BBDPS_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=477,
#     n_events=21157684,
# )
#

cpn.add_dataset(
    name="st_twchannel_t_dl_powheg",
    id=3371511,
    processes=[procs.st_twchannel_t_dl],
    keys=[
        "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=285,
    n_events=14999000,
)

cpn.add_dataset(
    name="st_twchannel_t_fh_powheg",
    id=3371502,
    processes=[procs.st_twchannel_t_fh],
    keys=[
        "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=372,
    n_events=23999000,
)

cpn.add_dataset(
    name="st_twchannel_t_sl_powheg",
    id=3371509,
    processes=[procs.st_twchannel_t_sl],
    keys=[
        "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=527,
    n_events=28762382,
)

cpn.add_dataset(
    name="st_twchannel_tbar_dl_powheg",
    id=3371507,
    processes=[procs.st_twchannel_tbar_dl],
    keys=[
        "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=209,
    n_events=15000000,
)

cpn.add_dataset(
    name="st_twchannel_tbar_fh_powheg",
    id=3371592,
    processes=[procs.st_twchannel_tbar_fh],
    keys=[
        "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=392,
    n_events=24000000,
)

cpn.add_dataset(
    name="st_twchannel_tbar_sl_powheg",
    id=3371591,
    processes=[procs.st_twchannel_tbar_sl],
    keys=[
        "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=528,
    n_events=29390933,
)

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3371833,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/TBbarQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=1433,
#     n_events=87565878,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3371523,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/TbarBQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=989,
#     n_events=43279124,
# )
#

cpn.add_dataset(
    name="st_tchannel_t_lep_powheg",
    id=3371512,
    processes=[procs.st_tchannel_t_lep],
    keys=[
        "/TBbarQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=784,
    n_events=44240309,
)

cpn.add_dataset(
    name="st_tchannel_tbar_lep_powheg",
    id=3371505,
    processes=[procs.st_tchannel_tbar_lep],
    keys=[
        "/TbarBQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=421,
    n_events=22115914,
)

cpn.add_dataset(
    name="ttw_wlnu_1jets_amcatnlo",
    id=3370692,
    processes=[procs.ttw_wlnu],
    keys=[
        "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-mg35x_150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=411,
    n_events=20362371,
)

cpn.add_dataset(
    name="ttw_wlnu_ewk_amcatnlo",
    id=3370653,
    processes=[procs.ttw_wlnu_ewk],
    keys=[
        "/TTLNu-EWK_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=74,
    n_events=2929000,
)

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3370729,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/TTW-WtoQQ-1Jets_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=152,
#     n_events=6210301,
# )
#

cpn.add_dataset(
    name="ttz_zll_m4to50_amcatnlo",
    id=3370705,
    processes=[procs.ttz_zll_m4to50],
    keys=[
        "/TTLL_Bin-MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=71,
    n_events=2966000,
)

cpn.add_dataset(
    name="ttz_zll_m50toinf_amcatnlo",
    id=3370694,
    processes=[procs.ttz_zll_m50toinf],
    keys=[
        "/TTLL_Bin-MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=102,
    n_events=3951000,
)

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=3370684,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/TTNuNu_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=90,
#     n_events=3999000,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370618,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/TTtoLNu2Q_Par-MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=3810,
#     n_events=197686000,
# )
#

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=3370762,
#     processes=[procs.PLACEHOLDER],
#     keys=[
#         "/TTtoLNu2Q_Par-MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
#     ],
#     n_files=3750,
#     n_events=197924000,
# )
#

cpn.add_dataset(
    name="tttt_amcatnlo",
    id=3371769,
    processes=[procs.tttt],
    keys=[
        "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=268,
    n_events=9776800,
)

cpn.add_dataset(
    name="ttww_madgraph",
    id=3371781,
    processes=[procs.ttww],
    keys=[
        "/TTWW_TuneCP5_13p6TeV_madgraph-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=136,
    n_events=5850000,
)

cpn.add_dataset(
    name="ttwz_madgraph",
    id=3371760,
    processes=[procs.ttwz],
    keys=[
        "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=125,
    n_events=5547000,
)

cpn.add_dataset(
    name="ttzz_madgraph",
    id=3371923,
    processes=[procs.ttzz],
    keys=[
        "/TTZZ_TuneCP5_13p6TeV_madgraph-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=339,
    n_events=10796000,
)

cpn.add_dataset(
    name="tttjm_amcatnlo",
    id=3371924,
    processes=[procs.tttjm],
    keys=[
        "/TTTJminus-DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=303,
    n_events=9657000,
)

cpn.add_dataset(
    name="tttjp_amcatnlo",
    id=3371944,
    processes=[procs.tttjp],
    keys=[
        "/TTTJplus-DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=272,
    n_events=9513000,
)

cpn.add_dataset(
    name="tttwm_amcatnlo",
    id=3371974,
    processes=[procs.tttwm],
    keys=[
        "/TTTWminus-DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=327,
    n_events=9690184,
)

cpn.add_dataset(
    name="tttwp_amcatnlo",
    id=3371904,
    processes=[procs.tttwp],
    keys=[
        "/TTTWplus-DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=319,
    n_events=9579250,
)

cpn.add_dataset(
    name="tzq_zll_4f_m30toinf_amcatnlo",
    id=3371831,
    processes=[procs.tzq],
    keys=[
        "/TZQB-Zto2L-4FS_Bin-MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-Madgraph_2_6_5_150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=179,
    n_events=8858000,
)

cpn.add_dataset(
    name="ttg_amcatnlo",
    id=3371911,
    processes=[procs.ttgamma],
    keys=[
        "/TTG-1Jets_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=379,
    n_events=19376611,
)

cpn.add_dataset(
    name="thw_madgraph",
    id=3372000,
    processes=[procs.thw],
    keys=[
        "/THW-5FS-ctcvcp_Par-M-125_TuneCP5_13p6TeV_madgraph-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=431,
    n_events=14983985,
)

cpn.add_dataset(
    name="thq_madgraph",
    id=3371945,
    processes=[procs.thq],
    keys=[
        "/THQ-4FS-ctcvcp_Par-M-125_TuneCP5_13p6TeV_madgraph-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=495,
    n_events=19984991,
)

cpn.add_dataset(
    name="ttwh_madgraph",
    id=3371859,
    processes=[procs.ttwh],
    keys=[
        "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=234,
    n_events=10541000,
)

cpn.add_dataset(
    name="twz_tqq_wlnu_zll_dr1_amcatnlo",
    id=3371958,
    processes=[procs.twz_tqq_wlnu_zll_dr1],
    keys=[
        "/TWZ-Tto2Q-WtoLNu-Zto2L-DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=252,
    n_events=10992000,
)

cpn.add_dataset(
    name="twz_tlnu_wqq_zll_dr1_amcatnlo",
    id=3371767,
    processes=[procs.twz_tlnu_wqq_zll_dr1],
    keys=[
        "/TWZ-TtoLNu-Wto2Q-Zto2L-DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=253,
    n_events=10969000,
)

cpn.add_dataset(
    name="twz_tlnu_wlnu_zll_dr1_amcatnlo",
    id=3371901,
    processes=[procs.twz_tlnu_wlnu_zll_dr1],
    keys=[
        "/TWZ-TtoLNu-WtoLNu-Zto2L-DR1_TuneCP5_13p6TeV_amcatnlo-pythia8/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_RunIII2024Summer24MiniAODv6-150X_v2-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=249,
    n_events=10975000,
)
