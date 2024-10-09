# coding: utf-8

"""
Higgs datasets for the 2023postBPix data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_v12 import campaign_run3_2023_postBPix_nano_v12 as cpn

####################################################################################################
#
# ggH
#
####################################################################################################

cpn.add_dataset(
    name="tth_hnonbb_powheg",
    id=14920188,
    processes=[procs.tth_hnonbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=138,
            n_events=5887987,
        ),
    ),
)
cpn.add_dataset(
    name="tth_hnonbb_1j_amcatnlo",
    id=14918806,
    processes=[procs.tth_hnonbb_1j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTHtoNon2B-1Jets_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=140,
            n_events=5595534,
        ),
    ),
)


####################################################################################################
#
# TTWH, TTZH
#
####################################################################################################


cpn.add_dataset(
    name="ttwh_madgraph",
    id=14932716,
    processes=[procs.ttwh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=969000,
        ),
    ),
)
cpn.add_dataset(
    name="ttzh_madgraph",
    id=14937478,
    processes=[procs.ttzh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=994000,
        ),
    ),
)
