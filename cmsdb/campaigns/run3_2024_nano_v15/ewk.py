# coding: utf-8

"""
Electroweak datasets for the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn

#
# Drell-Yan
#

# DY samples binned in lepton final state
cpn.add_dataset(
    name="dy_ee_m10to50_powheg",
    id=15297455,
    is_data=False,
    processes=[procs.dy_ee_m10to50],
    keys=[
        "/DYto2E_Bin-MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=395,
    n_events=348121585,
)

cpn.add_dataset(
    name="dy_ee_m50toinf_amcatnlo",
    id=15292625,
    is_data=False,
    processes=[procs.dy_ee_m50toinf],
    keys=[
        "/DYto2E-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM",  # noqa
    ],
    n_files=2990,
    n_events=486448139,
)

cpn.add_dataset(
    name="dy_mumu_m10to50_powheg",
    id=15297453,
    is_data=False,
    processes=[procs.dy_mumu_m10to50],
    keys=[
        "/DYto2Mu_Bin-MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=405,
    n_events=341634068,
)

cpn.add_dataset(
    name="dy_mumu_m50toinf_amcatnlo",
    id=15302208,
    is_data=False,
    processes=[procs.dy_mumu_m50toinf],
    keys=[
        "/DYto2Mu-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v6/NANOAODSIM",  # noqa
    ],
    n_files=2975,
    n_events=490076405,
)

cpn.add_dataset(
    name="dy_tautau_m10to50_powheg",
    id=15297458,
    is_data=False,
    processes=[procs.dy_tautau_m10to50],
    keys=[
        "/DYto2Tau_Bin-MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=400,
    n_events=344069532,
)

cpn.add_dataset(
    name="dy_tautau_m50toinf_amcatnlo",
    id=15292169,
    is_data=False,
    processes=[procs.dy_tautau_m50toinf],
    keys=[
        "/DYto2Tau-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v5/NANOAODSIM",  # noqa
    ],
    n_files=2947,
    n_events=520946105,
)

# DY samples binned in jets mll and ptll
# https://cms-pdmv-prod.web.cern.ch/grasp/samples?dataset_query=DYto2L*13p6*&nanoaod_version=v15
# dasgoclient -query="dataset=/DYto2L*13p6*/RunIII*Summer24*NanoAODv15*/NANOAODSIM"
# binned in J, MLL and PTLL (10 bins in total)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt40to100_amcatnlo",
    id=14679151,
    processes=[procs.dy_m50toinf_1j_pt40to100],
    keys=[
        "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=3045,
    n_events=479655476,
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt100to200_amcatnlo",
    id=14679152,
    processes=[procs.dy_m50toinf_1j_pt100to200],
    keys=[
        "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=355,
    n_events=227319605,
)

cpn.add_dataset(
    name="dy_lep_j1_m50toinf_pt200to400_amcatnlo",
    id=14679153,
    processes=[procs.dy_m50toinf_1j_pt200to400],
    keys=[
        "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=54,
    n_events=22383959,
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt400to600_amcatnlo",
    id=14679154,
    processes=[procs.dy_m50toinf_1j_pt400to600],
    keys=[
        "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=58,
    n_events=10404540,
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt600toinf_amcatnlo",
    id=14679155,
    processes=[procs.dy_m50toinf_1j_pt600toinf],
    keys=[
        "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=42,
    n_events=9996457,
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt40to100_amcatnlo",
    id=14679251,
    processes=[procs.dy_m50toinf_2j_pt40to100],
    keys=[
        "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=1787,
    n_events=247167836,
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt100to200_amcatnlo",
    id=14679252,
    processes=[procs.dy_m50toinf_2j_pt100to200],
    keys=[
        "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=389,
    n_events=246696940,
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt200to400_amcatnlo",
    id=14679253,
    processes=[procs.dy_m50toinf_2j_pt200to400],
    keys=[
        "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=139,
    n_events=44028174,
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt400to600_amcatnlo",
    id=14679254,
    processes=[procs.dy_m50toinf_2j_pt400to600],
    keys=[
        "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=47,
    n_events=9893470,
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt600_amcatnlo",
    id=14679255,
    processes=[procs.dy_m50toinf_2j_pt600],
    keys=[
        "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=50,
    n_events=9801431,
)

#
# W boson production
#

# w jets samples binned in lepton flavor
cpn.add_dataset(
    name="w_enu_amcatnlo",
    id=15297431,
    is_data=False,
    processes=[procs.w_enu],
    keys=[
        "/WtoENu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=3017,
    n_events=553868158,
)

cpn.add_dataset(
    name="w_munu_amcatnlo",
    id=15292952,
    is_data=False,
    processes=[procs.w_munu],
    keys=[
        "/WtoMuNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=2962,
    n_events=534824098,
)

cpn.add_dataset(
    name="w_taunu_amcatnlo",
    id=15292944,
    is_data=False,
    processes=[procs.w_taunu],
    keys=[
        "/WtoTauNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=2747,
    n_events=500139084,
)

# W jets samples binnedin jets, ptlnu
# https://cms-pdmv-prod.web.cern.ch/grasp/samples?dataset_query=WtoLNu*13p6*&nanoaod_version=v15
cpn.add_dataset(
    name="w_lnu_j1_pt40to100_amcatnlo",
    id=14611111,
    processes=[procs.w_lnu_j1_pt40to100],
    keys=[
        "/WtoLNu-2Jets_Bin-1J-PTLNu-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=3384,
    n_events=447467775,
)

cpn.add_dataset(
    name="w_lnu_j1_pt100to200_amcatnlo",
    id=14611112,
    processes=[procs.w_lnu_j1_pt100to200],
    keys=[
        "/WtoLNu-2Jets_Bin-1J-PTLNu-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=3089,
    n_events=494167270,
)

cpn.add_dataset(
    name="w_lnu_j1_pt200to400_amcatnlo",
    id=14611113,
    processes=[procs.w_lnu_j1_pt200to400],
    keys=[
        "/WtoLNu-2Jets_Bin-1J-PTLNu-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=109,
    n_events=45096548,
)

cpn.add_dataset(
    name="w_lnu_j1_pt400to600_amcatnlo",
    id=14611114,
    processes=[procs.w_lnu_j1_pt400to600],
    keys=[
        "/WtoLNu-2Jets_Bin-1J-PTLNu-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=62,
    n_events=14159808,
)

cpn.add_dataset(
    name="w_lnu_j1_pt600_amcatnlo",
    id=14611115,
    processes=[procs.w_lnu_j1_pt600],
    keys=[
        "/WtoLNu-2Jets_Bin-1J-PTLNu-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=15305397,
)

cpn.add_dataset(
    name="w_lnu_j2_pt40to100_amcatnlo",
    id=14611121,
    processes=[procs.w_lnu_j2_pt40to100],
    keys=[
        "/WtoLNu-2Jets_Bin-2J-PTLNu-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=3309,
    n_events=483030994,
)

cpn.add_dataset(
    name="w_lnu_j2_pt100to200_amcatnlo",
    id=14611122,
    processes=[procs.w_lnu_j2_pt100to200],
    keys=[
        "/WtoLNu-2Jets_Bin-2J-PTLNu-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=3262,
    n_events=470520533,
)

cpn.add_dataset(
    name="w_lnu_j2_pt200to400_amcatnlo",
    id=14611123,
    processes=[procs.w_lnu_j2_pt200to400],
    keys=[
        "/WtoLNu-2Jets_Bin-2J-PTLNu-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=136,
    n_events=75124628,
)

cpn.add_dataset(
    name="w_lnu_j2_pt400to600_amcatnlo",
    id=14611124,
    processes=[procs.w_lnu_j2_pt400to600],
    keys=[
        "/WtoLNu-2Jets_Bin-2J-PTLNu-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=51,
    n_events=14222725,
)

cpn.add_dataset(
    name="w_lnu_j2_pt600_amcatnlo",
    id=14611125,
    processes=[procs.w_lnu_j2_pt600],
    keys=[
        "/WtoLNu-2Jets_Bin-2J-PTLNu-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=67,
    n_events=14991109,
)

#
# Diboson
#

# ZZ
# https://cms-pdmv-prod.web.cern.ch/grasp/samples?dataset_query=ZZto*13p6*&nanoaod_version=v15
# TODO do we need 4q or 4nu sample?
cpn.add_dataset(
    name="zz_zll_znunu_powheg",
    id=14587220,
    processes=[procs.zz_zll_znunu],
    keys=[
        "/ZZto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=228,
    n_events=188715312,
)

cpn.add_dataset(
    name="zz_zqq_zll_powheg",
    id=14587202,
    processes=[procs.zz_zqq_zll],
    keys=[
        "/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=215,
    n_events=171627615,
)

cpn.add_dataset(
    name="zz_znunu_zqq_powheg",
    id=14587022,
    processes=[procs.zz_znunu_zqq],
    keys=[
        "/ZZto2Nu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=65,
    n_events=46047410,
)

cpn.add_dataset(
    name="zz_zll_zll_powheg",
    id=14587400,
    processes=[procs.zz_zll_zll],
    keys=[
        "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=273,
    n_events=236757511,
)

# WZ
# https://cms-pdmv-prod.web.cern.ch/grasp/samples?dataset_query=WZto*13p6*&nanoaod_version=v15a
# dasgoclient -query="dataset=/WZto*13p6*/RunIII*Summer24*NanoAODv15*/NANOAODSIM"
# missing WqqZqq, WqqZnunu, WlnuZnunu,
cpn.add_dataset(
    name="wz_wqq_zll_powheg",
    id=14596202,
    processes=[procs.wz_wqq_zll],
    keys=[
        "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=257,
    n_events=236049432,
)

cpn.add_dataset(
    name="wz_wlnu_zll_powheg",
    id=14596310,
    processes=[procs.wz_wlnu_zll],
    keys=[
        "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=296,
    n_events=248149069,
)

cpn.add_dataset(
    name="wz_wlnu_zqq_powheg",
    id=14596112,
    processes=[procs.wz_wlnu_zqq],
    keys=[
        "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=156,
    n_events=143874689,
)

# WW
# https://cms-pdmv-prod.web.cern.ch/grasp/samples?dataset_query=WWto*13p6*&nanoaod_version=v15

cpn.add_dataset(
    name="ww_fh_powheg",
    id=14694004,
    processes=[procs.ww_fh],
    keys=[
        "/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=185,
    n_events=151214029,
)

cpn.add_dataset(
    name="ww_dl_powheg",
    id=14694220,
    processes=[procs.ww_dl],
    keys=[
        "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=278,
    n_events=239943886,
)

cpn.add_dataset(
    name="ww_sl_powheg",
    id=14694112,
    processes=[procs.ww_sl],
    keys=[
        "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=326,
    n_events=275723961,
)
