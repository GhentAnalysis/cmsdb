# coding: utf-8

"""
custom datasets for the 2022 postEE+ data-taking campaign
produced by Joscha Knolle for ttZ analysis
/pnfs/iihe/cms/store/user/joknolle/topproduction/
"""

from order import DatasetInfo


import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_v12 import campaign_run3_2022_postEE_nano_v12 as cpn

cpn.add_dataset(
    name="ttz_zll_m50toinf_custom",
    id=1479337500,  # ttz_zll_m50to_inf dataset id with extra 00
    processes=[procs.ttz_zll_m50toinf],
    keys=[
            "/TTLL_MLL_50_trilep_13p6TeV_amcatnlo_Run3SIM_2022EEMiniAODandNanoAODv12_241105_121958",  # noqa
        ],
    n_files=10,
    n_events=1000000,
)

cpn.add_dataset(
    name="wz_wlnu_zll_amcatnlo_custom",
    id=1479099200,  # wz_wlnu_zll dataset id with extra 00
    processes=[procs.wz_wlnu_zll],
    keys=[
            "/WZTo3LNu_13p6TeV_amcatnlo_Run3SIM_2022EEMiniAODandNanoAODv12_241107_134754",  # noqa
        ],
    n_files=11,
    n_events=1000000,
)

cpn.add_dataset(
    name="wz_wlnu_zll_powheg_filter1jet_custom",
    id=1479099201,  # wz_wlnu_zll dataset id with extra 01
    processes=[procs.wz_wlnu_zll],
    keys=[
            "/WZTo3LNu_filter1jet_13p6TeV_powheg_Run3SIM_2022EEMiniAODandNanoAODv12_241111_150205",  # noqa
        ],
    n_files=4,
    n_events=1000000,
)

cpn.add_dataset(
    name="wz_wlnu_zll_amcatnlo_filter1jet_custom",
    id=1479099211,  # wz_wlnu_zll dataset id with extra 11
    processes=[procs.wz_wlnu_zll],
    keys=[
            "/WZTo3LNu_filter1jet_13p6TeV_amcatnlo_Run3SIM_2022EEMiniAODandNanoAODv12_241111_150044",  # noqa
        ],
    n_files=4,
    n_events=1000000,
)

cpn.add_dataset(
    name="wz_wlnu_zll_powheg_filter2jet_custom",
    id=1479099202,  # wz_wlnu_zll dataset id with extra 02
    processes=[procs.wz_wlnu_zll],
    keys=[
            "/WZTo3LNu_filter2jet_13p6TeV_powheg_Run3SIM_2022EEMiniAODandNanoAODv12_241111_150435",  # noqa
        ],
    n_files=4,
    n_events=1000000,
)

cpn.add_dataset(
    name="wz_wlnu_zll_amcatnlo_filter2jet_custom",
    id=1479099212,  # wz_wlnu_zll dataset id with extra 12
    processes=[procs.wz_wlnu_zll],
    keys=[
            "/WZTo3LNu_filter2jet_13p6TeV_amcatnlo_Run3SIM_2022EEMiniAODandNanoAODv12_241111_150320",  # noqa
        ],
    n_files=4,
    n_events=1000000,
)

cpn.add_dataset(
    name="wz_wlnu_zll_powheg_filter3jet_custom",
    id=1479099203,  # wz_wlnu_zll dataset id with extra 03
    processes=[procs.wz_wlnu_zll],
    keys=[
            "/WZTo3LNu_filter3jet_13p6TeV_powheg_Run3SIM_2022EEMiniAODandNanoAODv12_241111_150914",  # noqa
        ],
    n_files=4,
    n_events=1000000,
)

cpn.add_dataset(
    name="wz_wlnu_zll_amcatnlo_filter3jet_custom",
    id=1479099213,  # wz_wlnu_zll dataset id with extra 13
    processes=[procs.wz_wlnu_zll],
    keys=[
            "/WZTo3LNu_filter3jet_13p6TeV_amcatnlo_Run3SIM_2022EEMiniAODandNanoAODv12_241111_150550",  # noqa
        ],
    n_files=4,
    n_events=1000000,
)
