# coding: utf-8

"""
CMS datasets from the 2016 data-taking campaign (HIPM)
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_HIPM_nano_v9 import campaign_run2_2016_HIPM_nano_v9 as cpn

#
# SingleElectron
#

cpn.add_dataset(
    name="data_e_b",
    id=14345316,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleElectron/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",
        "/SingleElectron/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",

    ],
    n_files=1 + 106,
    n_events=1422819 + 246440440,
    aux=dict(
        era="B",
    ),
)

cpn.add_dataset(
    name="data_e_c",
    id=14345292,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleElectron/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",
    ],
    n_files=49,
    n_events=97259854,
    aux=dict(
        era="C",
    ),
)

cpn.add_dataset(
    name="data_e_d",
    id=14345209,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleElectron/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",
    ],
    n_files=66,
    n_events=148167727,
    aux=dict(
        era="D",
    ),
)

cpn.add_dataset(
    name="data_e_e",
    id=14345668,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleElectron/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",
    ],
    n_files=73,
    n_events=117269446,
    aux=dict(
        era="E",
    ),
)

cpn.add_dataset(
    name="data_e_f",
    id=14345250,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleElectron/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",
    ],
    n_files=40,
    n_events=61735326,
    aux=dict(
        era="F",
    ),
)


#
# Muon
#

cpn.add_dataset(
    name="data_mu_b",
    id=14345036,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",
        "/SingleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",
    ],
    n_files=2 + 70,
    n_events=2789243 + 158145722,
    aux=dict(
        era="B",
    ),
)

cpn.add_dataset(
    name="data_mu_c",
    id=14345260,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",
    ],
    n_files=28,
    n_events=67441308,
    aux=dict(
        era="C",
    ),
)

cpn.add_dataset(
    name="data_mu_d",
    id=14345352,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleMuon/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",
    ],
    n_files=40,
    n_events=98017996,
    aux=dict(
        era="D",
    ),
)

cpn.add_dataset(
    name="data_mu_e",
    id=14345735,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleMuon/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",
    ],
    n_files=47,
    n_events=90984718,
    aux=dict(
        era="E",
    ),
)

cpn.add_dataset(
    name="data_mu_f",
    id=14345750,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",
    ],
    n_files=43,
    n_events=57465359,
    aux=dict(
        era="F",
    ),
)
