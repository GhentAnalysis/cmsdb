# coding: utf-8

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn

#
# VHss
#

cpn.add_dataset(
    name="wmh_wqq_hss_powheg",
    id=15325018,
    is_data=False,
    processes=[procs.wmh_wqq_hss],
    keys=[
        "/WminusH-Wto2Q-Hto2S_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=989238,
)

cpn.add_dataset(
    name="wmh_wlnu_hss_powheg",
    id=15330077,
    is_data=False,
    processes=[procs.wmh_wlnu_hss],
    keys=[
        "/WminusH-WtoLNu-Hto2S_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=497475,
)

cpn.add_dataset(
    name="wph_wqq_hss_powheg",
    id=15325015,
    is_data=False,
    processes=[procs.wph_wqq_hss],
    keys=[
        "/WplusH-Wto2Q-Hto2S_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=1595072,
)

# TODO not yet fully completed
cpn.add_dataset(
    name="wph_wlnu_hss_powheg",
    id=15324806,
    is_data=False,
    processes=[procs.wph_wlnu_hss],
    keys=[
        "/WplusH-WtoLNu-Hto2S_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=745208,
)

cpn.add_dataset(
    name="zh_zll_hss_powheg",
    id=15324966,
    is_data=False,
    processes=[procs.zh_zll_hss],
    keys=[
        "/ZH-Zto2L-Hto2S_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=249376,
)

cpn.add_dataset(
    name="zh_znunu_hss_powheg",
    id=15324831,
    is_data=False,
    processes=[procs.zh_znunu_hss],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH-Zto2Nu-Hto2S_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=13,
            n_events=250000,
            aux={
                "broken_files": [
                ],
            },
        ),
    ),
)

cpn.add_dataset(
    name="zh_zqq_hss_powheg",
    id=-15324999,
    is_data=False,
    processes=[procs.zh_zqq_hss],
    keys=[
        "/ZH-Zto2Q-Hto2S_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=495716,
)

#
# VHbb
#

cpn.add_dataset(
    name="wmh_wqq_hbb_powheg",
    id=15341180,
    is_data=False,
    processes=[procs.wmh_wqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH-Wto2Q-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=13,
            n_events=3966909,
            aux={
                "broken_files": [
                ],
            },
        ),
    ),
)

cpn.add_dataset(
    name="wmh_wlnu_hbb_powheg",
    id=15330078,
    is_data=False,
    processes=[procs.wmh_wlnu_hbb],
    keys=[
        "/WminusH-WtoLNu-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=1976960,
)

cpn.add_dataset(
    name="wph_wqq_hbb_powheg",
    id=15325013,
    is_data=False,
    processes=[procs.wph_wqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH-Wto2Q-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=6261825,
            aux={
                "broken_files": [
                ],
            },
        ),
    ),
)

cpn.add_dataset(
    name="wph_wlnu_hbb_powheg",
    id=15321740,
    is_data=False,
    processes=[procs.wph_wlnu_hbb],
    keys=[
        "/WplusH-WtoLNu-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=3068881,
)

# TODO /ZH*Hto2B*13p6*/RunIII2024*v15*/NANOAODSIM still in production
# procs.zh_zll_hbb
# procs.zh_zqq_hbb
# procs.zh_znunu_hbb

#
# VH(cc)
#

cpn.add_dataset(
    name="wmh_wqq_hcc_powheg",
    id=15330079,
    is_data=False,
    processes=[procs.wmh_wqq_hcc],
    keys=[
        "/WminusH-Wto2Q-Hto2C_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=1980289,
)

cpn.add_dataset(
    name="wmh_wlnu_hcc_powheg",
    id=15330112,
    is_data=False,
    processes=[procs.wmh_wlnu_hcc],
    keys=[
        "/WminusH-WtoLNu-Hto2C_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=991419,
)

# TODO WplusH*Hto2C still in production
# procs.whplus_wqq_hcc
# procs.whplus_wlnu_hcc

# TODO /ZH*Hto2C*13p6 still in production
# procs.zh_zll_hcc
# procs.zh_zqq_hcc
# procs.zh_znunu_hcc

#
# VH(non bb)
#

cpn.add_dataset(
    name="wmh_hnonbb_powheg",
    id=15349203,
    is_data=False,
    processes=[procs.wmh_hnonbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH-HtoNon2B_Par-M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=46,
            n_events=3697133,
            aux={
                "broken_files": [
                ],
            },
        ),
    ),
)

cpn.add_dataset(
    name="wph_hnonbb_powheg",
    id=15349193,
    is_data=False,
    processes=[procs.wph_hnonbb],
    keys=[
        "/WplusH-HtoNon2B_Par-M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=51,
    n_events=4074508,
)

cpn.add_dataset(
    name="zh_hnonbb_powheg",
    id=15349371,
    is_data=False,
    processes=[procs.zh_hnonbb],
    keys=[
        "/ZH-HtoNon2B_Par-M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=4188141,
)
