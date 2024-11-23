# coding: utf-8

"""
custom datasets for the 2022 preEE+ data-taking campaign
produced by Joscha Knolle for ttZ analysis
/pnfs/iihe/cms/store/user/joknolle/topproduction    
"""

from order import DatasetInfo


import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn

cpn.add_dataset(
    name="ttz_zll_m50toinf_custom",
    id=1479392900,  # ttz_zll_m50to_inf dataset id with extra 00
    processes=[procs.ttz_zll_m50toinf],
    keys=[
            "/TTLL_MLL_50_trilep_13p6TeV_amcatnlo_Run3SIM_2022MiniAODandNanoAODv12_241105_144710",  # noqa
        ],
    n_files=10,
    n_events=1000000,
)

cpn.add_dataset(
    name="wz_wlnu_zll_amcatnlo_custom",
    id=1479159100,  # wz_wlnu_zll dataset id with extra 00
    processes=[procs.wz_wlnu_zll],
    keys=[
            "/WZTo3LNu_13p6TeV_amcatnlo_Run3SIM_2022MiniAODandNanoAODv12_241107_135149",  # noqa
        ],
    n_files=11,
    n_events=1000000,
)
