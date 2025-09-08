# coding: utf-8

"""
CMS datasets from the 2016 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_nano_v9 import campaign_run2_2016_nano_v9 as cpn


#
# SingleElectron
#

cpn.add_dataset(
    name="data_e_f",
    id=14230145,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleElectron/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=5,
    n_events=8858206,
    aux=dict(
        era="F",
    ),
)

cpn.add_dataset(
    name="data_e_g",
    id=14239294,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleElectron/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=71,
    n_events=153363109,
    aux=dict(
        era="G",
    ),
)

cpn.add_dataset(
    name="data_e_h",
    id=14227078,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleElectron/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=80,
    n_events=129021893,
    aux=dict(
        era="H",
    ),
)

#
# Muon
#

cpn.add_dataset(
    name="data_mu_f",
    id=14233029,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleMuon/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=5,
    n_events=8024195,
    aux=dict(
        era="F",
    ),
)

cpn.add_dataset(
    name="data_mu_g",
    id=14227079,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleMuon/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=70,
    n_events=149916849,
    aux=dict(
        era="G",
    ),
)

cpn.add_dataset(
    name="data_mu_h",
    id=14227072,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleMuon/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=82,
    n_events=174035164,
    aux=dict(
        era="H",
    ),
)