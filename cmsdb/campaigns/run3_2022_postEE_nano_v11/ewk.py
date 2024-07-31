# coding: utf-8

"""
Electroweak datasets for the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_v11 import campaign_run3_2022_postEE_nano_v11 as cpn


#
# Drell-Yan
#

# inclusive (MadGraph)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYJetsToLL_M-50&nanoaod_version=v11  # noqa
cpn.add_dataset(
    name="dy_lep_m50_madgraph",
    id=14679709,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=55,
    n_events=96296977,
)

# inclusive (aMC@NLO)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYto2L-2Jets_MLL-50&nanoaod_version=v11  # noqa
cpn.add_dataset(
    name="dy_lep_m50_amcatnlo",
    id=14814859,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=[
        "DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=407,
    n_events=319825084,
)

cpn.add_dataset(
    name="dy_lep_m10to50_amcatnlo",
    id=14803206,
    is_data=False,
    processes=[procs.dy_lep_m10to50],
    keys=[
        "/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=322,
    n_events=215532589,
)


# DY in various jet bins in NanoAODv12

cpn.add_dataset(
    name="dy_lep_m50_0j_amcatnlo",
    id=14791116,
    is_data=False,
    processes=[procs.dy_lep_m50_0j],
    keys=[
        "/DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=452,
    n_events=346950546,
)

cpn.add_dataset(
    name="dy_lep_m50_1j_amcatnlo",
    id=14790681,
    is_data=False,
    processes=[procs.dy_lep_m50_1j],
    keys=[
        "/DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=454,
    n_events=322623183,
)

cpn.add_dataset(
    name="dy_lep_m50_2j_amcatnlo",
    id=14801013,
    is_data=False,
    processes=[procs.dy_lep_m50_2j],
    keys=[
        "/DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=386,
    n_events=277437970,
)


# MadGraph (n-jet binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYto2L-4  # noqa
# missing as of 2023-07-01

# POWHEG (decay to muons, MLL-binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYto2Mu  # noqa
# DAS entries:
#     /DYto2Mu_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM
#     /DYto2Mu_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM
#     /DYto2Mu_MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM
#     /DYto2Mu_MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM
#     /DYto2Mu_MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM
#     /DYto2Mu_MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM
#     /DYto2Mu_MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM
#     /DYto2Mu_MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM
#     /DYto2Mu_MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM
#     /DYto2Mu_MLL-4000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM

# POWHEG (decay to electrons, MLL-binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYto2E_MLL  # noqa
# missing as of 2023-07-01


#
# W boson production
#

# inclusive (aMC@NLO)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=WtoLNu-2Jets&nanoaod_version=v11  # noqa
cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14796394,
    is_data=False,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=381,
    n_events=281543551,
)

# MadGraph (n-jet binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=WtoLNu-4Jets_%281%7C2%7C3%7C4%29J&nanoaod_version=v11  # noqa
# missing as of 2023-07-01


#
# Diboson
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEGS&nanoaod_version=v11&short_name=VV  # noqa

# missing as of 2023-07-01
# cpn.add_dataset(
#     name="zz_pythia",
#     id=None,
#     is_data=False,
#     processes=[procs.zz],
#     keys=[
#         "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=None,
#     n_events=None,
# )

cpn.add_dataset(
    name="wz_pythia",
    id=14799680,
    is_data=False,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=90,
    n_events=26840468,
)

cpn.add_dataset(
    name="wz_lllnu_amcatnlo",
    id=14790992,
    is_data=False,
    processes=[procs.wz_lllnu],
    keys=[
        "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM ",  # noqa
    ],
    n_files=63,
    n_events=9779090,
)


cpn.add_dataset(
    name="wzto3lnu_1jets_4fs_amcatnlo",
    id=14784506,
    is_data=False,
    processes=[procs.wzto3lnu_1jets],  # TODO change processes to 1 jet specific
    keys=[
        "/WZto3LNu-1Jets-4FS_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=108,
    n_events=10095542,
)


cpn.add_dataset(
    name="ww_powheg",
    id=14801288,
    is_data=False,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=117,
    n_events=53190560,
)

cpn.add_dataset(
    name="wwto2l2nu_powheg",
    id=14791590,
    is_data=False,
    processes=[procs.ww_lnulnu],
    keys=[
        "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=57,
    n_events=22428584,
)

# ZZ
#

cpn.add_dataset(
    name="zzto4l_powheg",
    id=14790743,
    processes=[procs.zz_llll],
    keys=[
        "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=208,
    n_events=61372656,
)

#
# GluGlueToContinToZZ
#

cpn.add_dataset(
    name="gluglutocontintozzto2e2mu_mcfm",
    id=14826608,
    processes=[procs.ggtozzto2e2mu],
    keys=[
        "/GluGluToContinto2Zto2E2Mu_TuneCP5_13p6TeV_mcfm701-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=523444,
)

cpn.add_dataset(
    name="gluglutocontintozzto2e2tau_mcfm",
    id=14889511,
    processes=[procs.ggtozzto2e2tau],
    keys=[
        "/GluGluToContinto2Zto2E2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=517620,
)

cpn.add_dataset(
    name="gluglutocontintozzto2mu2tau_mcfm",
    id=14889510,
    processes=[procs.ggtozzto2mu2tau],
    keys=[
        "/GluGluToContinto2Zto2Mu2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=525000,
)

# TODO Not found in CMSDAS
# cpn.add_dataset(
#    name="gluglutocontintozzto4e_mcfm",
#    id=14242982,
#    processes=[procs.ggtozzto4e],
#    keys=[
#        "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
#    ],
#    n_files=25,
#    n_events=974000,
# )
#
# cpn.add_dataset(
#    name="gluglutocontintozzto4mu_mcfm",
#    id=14266651,
#    processes=[procs.ggtozzto4mu],
#    keys=[
#        "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
#    ],
#    n_files=34,
#    n_events=845232,
# )
#
# cpn.add_dataset(
#    name="gluglutocontintozzto4tau_mcfm",
#    id=14253997,
#    processes=[procs.ggtozzto4tau],
#    keys=[
#        "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
#    ],
#    n_files=10,
#    n_events=493998,
# )

# VH

cpn.add_dataset(
    name="vh_htononbb_m125",
    id=14850117,
    processes=[procs.vh],
    keys=[
        "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=502646,
)

#
# Triple Boson
#

cpn.add_dataset(
    name="www_4f_amcatnlo",
    id=14793787,
    processes=[procs.www4f],
    keys=[
        "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=1482480,
)

cpn.add_dataset(
    name="wwz_4f_amcatnlo",
    id=14793788,
    processes=[procs.wwz4f],
    keys=[
        "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=5601076,
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=14798602,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=40,
    n_events=5290014,
)

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=14805133,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=5803440,
)

#
# Boson + Gamma
#

# WG

cpn.add_dataset(
    name="wgtolnug_ptg10to100_amcatnlo",
    id=14787167,
    processes=[procs.wgtolnug_ptg10to100],
    keys=[
        "/WGtoLNuG-1Jets_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1014,
    n_events=5803440,
)

cpn.add_dataset(
    name="wgtolnug_ptg100to200_amcatnlo",
    id=14787642,
    processes=[procs.wgtolnug_ptg100to200],
    keys=[
        "/WGtoLNuG-1Jets_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=123,
    n_events=3517478,
)

cpn.add_dataset(
    name="wgtolnug_ptg200to400_amcatnlo",
    id=14850186,
    processes=[procs.wgtolnug_ptg200to400],
    keys=[
        "/WGtoLNuG-1Jets_PTG-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=89,
    n_events=1657844,
)

cpn.add_dataset(
    name="wgtolnug_ptg400to600_amcatnlo",
    id=14850183,
    processes=[procs.wgtolnug_ptg400to600],
    keys=[
        "/WGtoLNuG-1Jets_PTG-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=72,
    n_events=1604621,
)

cpn.add_dataset(
    name="wgtolnug_ptg600_amcatnlo",
    id=14852427,
    processes=[procs.wgtolnug_ptg600],
    keys=[
        "/WGtoLNuG-1Jets_PTG-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=76,
    n_events=1794885,
)

# WZG

cpn.add_dataset(
    name="wzgtolnuzg_amcatnlo",
    id=14797986,
    processes=[procs.wzg],
    keys=[
        "/WZGtoLNuZG_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=750000,
)

# DYG to  2LG

cpn.add_dataset(
    name="dygto2lg_mll4to50_ptg10to100_amcatnlo",
    id=14809616,
    processes=[procs.dygto2lg_mll4to50_ptg10to100],
    keys=[
        "/DYGto2LG-1Jets_MLL-4to50_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=576,
    n_events=85739885,
)

cpn.add_dataset(
    name="dygto2lg_mll4to50_ptg100to200_amcatnlo",
    id=14809461,
    processes=[procs.dygto2lg_mll4to50_ptg100to200],
    keys=[
        "/DYGto2LG-1Jets_MLL-4to50_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=75,
    n_events=1448629,
)

cpn.add_dataset(
    name="dygto2lg_mll4to50_ptg200_amcatnlo",
    id=14811651,
    processes=[procs.dygto2lg_mll4to50_ptg200],
    keys=[
        "/DYGto2LG-1Jets_MLL-4to50_PTG-200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=30,
    n_events=746202,
)

cpn.add_dataset(
    name="dygto2lg_mll50_ptg10to50_amcatnlo",
    id=14790854,
    processes=[procs.dygto2lg_mll50_ptg10to50],
    keys=[
        "/DYGto2LG-1Jets_MLL-50_PTG-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=191,
    n_events=104473209,
)

cpn.add_dataset(
    name="dygto2lg_mll50_ptg50to100_amcatnlo",
    id=14808376,
    processes=[procs.dygto2lg_mll50_ptg50to100],
    keys=[
        "/DYGto2LG-1Jets_MLL-50_PTG-50to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=90,
    n_events=48791625,
)

cpn.add_dataset(
    name="dygto2lg_mll50_ptg100to200_amcatnlo",
    id=14793597,
    processes=[procs.dygto2lg_mll50_ptg100to200],
    keys=[
        "/DYGto2LG-1Jets_MLL-50_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=696610,
)

cpn.add_dataset(
    name="dygto2lg_mll50_ptg200to400_amcatnlo",
    id=14886082,
    processes=[procs.dygto2lg_mll50_ptg200to400],
    keys=[
        "/DYGto2LG-1Jets_MLL-50_PTG-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=29,
    n_events=1785572,
)

cpn.add_dataset(
    name="dygto2lg_mll50_ptg400to600_amcatnlo",
    id=14887668,
    processes=[procs.dygto2lg_mll50_ptg400to600],
    keys=[
        "/DYGto2LG-1Jets_MLL-50_PTG-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=1776157,
)

cpn.add_dataset(
    name="dygto2lg_mll50_ptg600_amcatnlo",
    id=14886958,
    processes=[procs.dygto2lg_mll50_ptg600],
    keys=[
        "/DYGto2LG-1Jets_MLL-50_PTG-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=62,
    n_events=1797374,
)
