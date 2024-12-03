
# coding: utf-8

"""
CMS datasets from the 2023 pre-BPix data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn

from order import DatasetInfo

cpn.add_dataset(
    name="tzq_zll_4f_m30toinf_custom",
    id=1491692312,  # id of 2022preEE with 12 after
    processes=[procs.tzq_wlnu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TZQB_Zto2L_4FS_MLL_30_trilep_13p6TeV_amcatnlo_Run3SIM_2023BPixMiniAODandNanoAODv12_241119_134319",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=10,
            n_events=1000000,
        ),
    ),
)
