# coding: utf-8

"""
data datasets for the 2025 data-taking campaign
"""

import cmsdb.processes as procs

from cmsdb.campaigns.run3_2025_customnano_v15 import campaign_run3_2025_customnano_v15 as cpn

cpn.add_dataset(
    name="data_mu0_b_v1",
    id=3372440,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025B-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=57,
    n_events=5602078,
)

cpn.add_dataset(
    name="data_mu0_c_v1",
    id=3372420,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2623,
    n_events=250835953,
)

cpn.add_dataset(
    name="data_mu0_c_v2",
    id=3372450,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1544,
    n_events=148575745,
)

cpn.add_dataset(
    name="data_mu0_d_v1",
    id=3372414,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025D-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=5013,
    n_events=479676562,
)

cpn.add_dataset(
    name="data_mu0_e_v1",
    id=3372423,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025E-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2788,
    n_events=265645863,
)

cpn.add_dataset(
    name="data_mu0_f_v1",
    id=3372428,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=3941,
    n_events=377119912,
)

cpn.add_dataset(
    name="data_mu0_f_v2",
    id=3372439,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1510,
    n_events=143519758,
)

cpn.add_dataset(
    name="data_mu0_g_v1",
    id=3372435,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025G-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=4621,
    n_events=442329683,
)

cpn.add_dataset(
    name="data_mu1_b_v1",
    id=3372647,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025B-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=57,
    n_events=5598676,
)

cpn.add_dataset(
    name="data_mu1_c_v1",
    id=3372655,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2607,
    n_events=250819768,
)

cpn.add_dataset(
    name="data_mu1_c_v2",
    id=3372665,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1545,
    n_events=148565659,
)

cpn.add_dataset(
    name="data_mu1_d_v1",
    id=3372689,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025D-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=5012,
    n_events=479642866,
)

cpn.add_dataset(
    name="data_mu1_e_v1",
    id=3372662,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025E-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2791,
    n_events=265630211,
)

cpn.add_dataset(
    name="data_mu1_f_v1",
    id=3372646,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=3942,
    n_events=377092035,
)

cpn.add_dataset(
    name="data_mu1_f_v2",
    id=3372679,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1508,
    n_events=143511119,
)

cpn.add_dataset(
    name="data_mu1_g_v1",
    id=3372692,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025G-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=4621,
    n_events=442232031,
)

cpn.add_dataset(
    name="data_muoneg_b_v1",
    id=3372812,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025B-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=11,
    n_events=910971,
)

cpn.add_dataset(
    name="data_muoneg_c_v1",
    id=3372712,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=423,
    n_events=41994774,
)

cpn.add_dataset(
    name="data_muoneg_c_v2",
    id=3372749,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=234,
    n_events=23203653,
)

cpn.add_dataset(
    name="data_muoneg_d_v1",
    id=3372643,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025D-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=740,
    n_events=72820407,
)

cpn.add_dataset(
    name="data_muoneg_e_v1",
    id=3372760,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025E-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=410,
    n_events=40691496,
)

cpn.add_dataset(
    name="data_muoneg_f_v1",
    id=3372863,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=587,
    n_events=58301670,
)

cpn.add_dataset(
    name="data_muoneg_f_v2",
    id=3372816,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=227,
    n_events=22447339,
)

cpn.add_dataset(
    name="data_muoneg_g_v1",
    id=3372781,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025G-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=678,
    n_events=67268221,
)

cpn.add_dataset(
    name="data_egamma0_b_v1",
    id=3372480,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025B-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=53,
    n_events=5256904,
)

cpn.add_dataset(
    name="data_egamma0_c_v1",
    id=3372516,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2522,
    n_events=243682359,
)

cpn.add_dataset(
    name="data_egamma0_c_v2",
    id=3372434,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1392,
    n_events=133952379,
)

cpn.add_dataset(
    name="data_egamma0_d_v1",
    id=3372449,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025D-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=4294,
    n_events=414017171,
)

cpn.add_dataset(
    name="data_egamma0_e_v1",
    id=3375240,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025E-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2512,
    n_events=240927385,
)

cpn.add_dataset(
    name="data_egamma0_f_v1",
    id=3372490,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=3608,
    n_events=346019505,
)

cpn.add_dataset(
    name="data_egamma0_f_v2",
    id=3372433,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1448,
    n_events=139317024,
)

cpn.add_dataset(
    name="data_egamma0_g_v1",
    id=3372455,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025G-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=4408,
    n_events=421374702,
)

cpn.add_dataset(
    name="data_egamma1_b_v1",
    id=3372890,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025B-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=53,
    n_events=5253103,
)

cpn.add_dataset(
    name="data_egamma1_c_v1",
    id=3372891,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2519,
    n_events=243674671,
)

cpn.add_dataset(
    name="data_egamma1_c_v2",
    id=3372856,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1392,
    n_events=133951067,
)

cpn.add_dataset(
    name="data_egamma1_d_v1",
    id=3372866,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025D-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=4297,
    n_events=413998146,
)

cpn.add_dataset(
    name="data_egamma1_e_v1",
    id=3372865,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025E-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2509,
    n_events=240921314,
)

cpn.add_dataset(
    name="data_egamma1_f_v1",
    id=3372896,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=3608,
    n_events=346000262,
)

cpn.add_dataset(
    name="data_egamma1_f_v2",
    id=3372859,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1447,
    n_events=139310909,
)

cpn.add_dataset(
    name="data_egamma1_g_v1",
    id=3372886,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025G-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=4408,
    n_events=421102377,
)

cpn.add_dataset(
    name="data_egamma2_b_v1",
    id=3372878,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma2/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025B-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=53,
    n_events=5254123,
)

cpn.add_dataset(
    name="data_egamma2_c_v1",
    id=3372867,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma2/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2523,
    n_events=243672282,
)

cpn.add_dataset(
    name="data_egamma2_c_v2",
    id=3372794,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma2/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1392,
    n_events=133950574,
)

cpn.add_dataset(
    name="data_egamma2_d_v1",
    id=3372854,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma2/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025D-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=4291,
    n_events=414008481,
)

cpn.add_dataset(
    name="data_egamma2_e_v1",
    id=3372824,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma2/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025E-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2512,
    n_events=240923259,
)

cpn.add_dataset(
    name="data_egamma2_f_v1",
    id=3372869,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma2/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=3609,
    n_events=346008679,
)

cpn.add_dataset(
    name="data_egamma2_f_v2",
    id=3372872,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma2/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1448,
    n_events=139313488,
)

cpn.add_dataset(
    name="data_egamma2_g_v1",
    id=3372885,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma2/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025G-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=4410,
    n_events=421453068,
)

cpn.add_dataset(
    name="data_egamma3_b_v1",
    id=3373930,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma3/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025B-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=53,
    n_events=5253489,
)

cpn.add_dataset(
    name="data_egamma3_c_v1",
    id=3372044,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma3/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2521,
    n_events=243679348,
)

cpn.add_dataset(
    name="data_egamma3_c_v2",
    id=3372026,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma3/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1392,
    n_events=133949781,
)

cpn.add_dataset(
    name="data_egamma3_d_v1",
    id=3372080,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma3/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025D-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=4295,
    n_events=414010046,
)

cpn.add_dataset(
    name="data_egamma3_e_v1",
    id=3372078,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma3/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025E-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2512,
    n_events=240923335,
)

cpn.add_dataset(
    name="data_egamma3_f_v1",
    id=3372034,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma3/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=3603,
    n_events=345909453,
)

cpn.add_dataset(
    name="data_egamma3_f_v2",
    id=3372029,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma3/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1449,
    n_events=139314438,
)

cpn.add_dataset(
    name="data_egamma3_g_v1",
    id=3372010,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma3/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025G-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=4410,
    n_events=421124471,
)

cpn.add_dataset(
    name="data_jetmet0_b_v1",
    id=3373286,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025B-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=137,
    n_events=13561943,
)

cpn.add_dataset(
    name="data_jetmet0_c_v1",
    id=3373279,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1588,
    n_events=155327920,
)

cpn.add_dataset(
    name="data_jetmet0_c_v2",
    id=3373333,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=836,
    n_events=81725663,
)

cpn.add_dataset(
    name="data_jetmet0_d_v1",
    id=3373328,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025D-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2639,
    n_events=257411297,
)

cpn.add_dataset(
    name="data_jetmet0_e_v1",
    id=3373276,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025E-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1490,
    n_events=145280947,
)

cpn.add_dataset(
    name="data_jetmet0_f_v1",
    id=3373061,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2054,
    n_events=200129655,
)

cpn.add_dataset(
    name="data_jetmet0_f_v2",
    id=3373268,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=786,
    n_events=76494690,
)

cpn.add_dataset(
    name="data_jetmet0_g_v1",
    id=3373261,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET0/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025G-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2708,
    n_events=259829148,
)

cpn.add_dataset(
    name="data_jetmet1_b_v1",
    id=3373226,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025B-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=137,
    n_events=13551058,
)

cpn.add_dataset(
    name="data_jetmet1_c_v1",
    id=3374454,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1589,
    n_events=155309595,
)

cpn.add_dataset(
    name="data_jetmet1_c_v2",
    id=3373290,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=836,
    n_events=81736350,
)

cpn.add_dataset(
    name="data_jetmet1_d_v1",
    id=3373308,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025D-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2632,
    n_events=257342455,
)

cpn.add_dataset(
    name="data_jetmet1_e_v1",
    id=3373272,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025E-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1489,
    n_events=145256476,
)

cpn.add_dataset(
    name="data_jetmet1_f_v1",
    id=3373138,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2062,
    n_events=200859929,
)

cpn.add_dataset(
    name="data_jetmet1_f_v2",
    id=3373285,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=785,
    n_events=76479375,
)

cpn.add_dataset(
    name="data_jetmet1_g_v1",
    id=3373266,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/JetMET1/phys_higgs-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025G-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2709,
    n_events=259876805,
)

cpn.add_dataset(
    name="data_parkinghh0_b_v1",
    id=3373920,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025B-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=23,
    n_events=2197413,
)

cpn.add_dataset(
    name="data_parkinghh0_c_v1",
    id=3371948,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1072,
    n_events=105521325,
)

cpn.add_dataset(
    name="data_parkinghh0_c_v2",
    id=3371849,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=633,
    n_events=62282749,
)

cpn.add_dataset(
    name="data_parkinghh0_d_v1",
    id=3371975,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025D-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2144,
    n_events=210139262,
)

cpn.add_dataset(
    name="data_parkinghh0_e_v1",
    id=3371870,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025E-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1207,
    n_events=118376379,
)

cpn.add_dataset(
    name="data_parkinghh0_f_v1",
    id=3371920,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1701,
    n_events=166703677,
)

cpn.add_dataset(
    name="data_parkinghh0_f_v2",
    id=3371968,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=688,
    n_events=67312325,
)

cpn.add_dataset(
    name="data_parkinghh0_g_v1",
    id=3371907,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH0/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025G-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2050,
    n_events=200710715,
)

cpn.add_dataset(
    name="data_parkinghh1_b_v1",
    id=3371908,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025B-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=22,
    n_events=2192548,
)

cpn.add_dataset(
    name="data_parkinghh1_c_v1",
    id=3371892,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1072,
    n_events=105515995,
)

cpn.add_dataset(
    name="data_parkinghh1_c_v2",
    id=3371902,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025C-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=633,
    n_events=62281707,
)

cpn.add_dataset(
    name="data_parkinghh1_d_v1",
    id=3371965,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025D-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2144,
    n_events=210130176,
)

cpn.add_dataset(
    name="data_parkinghh1_e_v1",
    id=3371960,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025E-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1208,
    n_events=118370823,
)

cpn.add_dataset(
    name="data_parkinghh1_f_v1",
    id=3371981,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=1700,
    n_events=166697042,
)

cpn.add_dataset(
    name="data_parkinghh1_f_v2",
    id=3371962,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025F-PromptReco-v2-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=687,
    n_events=67310765,
)

cpn.add_dataset(
    name="data_parkinghh1_g_v1",
    id=3372035,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/ParkingHH1/CustomNanoAODv15-NanoTuples-uParTv3-parTlepID-NanoAODv15_Run2025G-PromptReco-v1-00000000000000000000000000000000/USER",  # noqa
    ],
    n_files=2051,
    n_events=200707042,
)
