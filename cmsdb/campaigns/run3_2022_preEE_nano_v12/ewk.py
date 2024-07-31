# coding: utf-8

"""
Electroweak datasets for the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn


#
# Drell-Yan
#

# inclusive (MadGraph)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYJetsToLL_M-50&nanoaod_version=v11  # noqa  # noqa
# For POG #TODO change to correct one once more stats available
cpn.add_dataset(
    name="dy_lep_m50_madgraph",
    id=14802794,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22NanoAODv12-forPOG_130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=51,
    n_events=27096229,
)

# inclusive (aMC@NLO)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYto2L-2Jets_MLL-50&nanoaod_version=v11  # noqa  # noqa
cpn.add_dataset(
    name="dy_lep_m50_amcatnlo",
    id=14796042,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=115,
    n_events=65997137,
)

cpn.add_dataset(
    name="dy_lep_m10to50_amcatnlo",
    id=14803891,
    is_data=False,
    processes=[procs.dy_lep_m10to50],
    keys=[
        "/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=141,
    n_events=67681922,
)


# DY in various jet bins in NanoAODv12

cpn.add_dataset(
    name="dy_lep_m50_0j_amcatnlo",
    id=14791297,
    is_data=False,
    processes=[procs.dy_lep_m50_0j],
    keys=[
        "/DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=173,
    n_events=105230672,
)

cpn.add_dataset(
    name="dy_lep_m50_1j_amcatnlo",
    id=14791387,
    is_data=False,
    processes=[procs.dy_lep_m50_1j],
    keys=[
        "/DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=196,
    n_events=99076102,
)

cpn.add_dataset(
    name="dy_lep_m50_2j_amcatnlo",
    id=14790870,
    is_data=False,
    processes=[procs.dy_lep_m50_2j],
    keys=[
        "/DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=177,
    n_events=75705368,
)

# MadGraph (n-jet binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYto2L-4  # noqa
# missing as of 2023-07-01

# POWHEG (decay to muons, MLL-binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYto2Mu  # noqa
# DAS entries:
#     /DYto2Mu_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM
#     /DYto2Mu_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM
#     /DYto2Mu_MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM
#     /DYto2Mu_MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM
#     /DYto2Mu_MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM
#     /DYto2Mu_MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM
#     /DYto2Mu_MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM
#     /DYto2Mu_MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM
#     /DYto2Mu_MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM
#     /DYto2Mu_MLL-4000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM

# POWHEG (decay to electrons, MLL-binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYto2E_MLL  # noqa
# missing as of 2023-07-01


#
# W boson production
#

# inclusive (aMC@NLO)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=WtoLNu-2Jets&nanoaod_version=v11  # noqa  # noqa
cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14611721,
    is_data=False,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=80257100,
)

# MadGraph (n-jet binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=WtoLNu-4Jets_%281%7C2%7C3%7C4%29J&nanoaod_version=v11  # noqa  # noqa
# missing as of 2023-07-01


#
# Diboson
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22GS&nanoaod_version=v11&short_name=VV  # noqa

cpn.add_dataset(
    name="zz_pythia",
    id=14587173,
    is_data=False,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=1186860,
)

cpn.add_dataset(
    name="zzto4l_powheg",
    id=14791221,
    processes=[procs.zz_llll],
    keys=[
        "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=82,
    n_events=14629101,
)


cpn.add_dataset(
    name="wz_pythia",
    id=14803901,
    is_data=False,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=7527043,
)

cpn.add_dataset(
    name="wz_lllnu_amcatnlo",
    id=14791591,
    is_data=False,
    processes=[procs.wz_lllnu],
    keys=[
        "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=2776339,
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
    name="ww_pythia",
    id=14800098,
    is_data=False,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=63,
    n_events=15357390,
)

cpn.add_dataset(
    name="wwto2l2nu_powheg",
    id=14793091,
    is_data=False,
    processes=[procs.ww_lnulnu],
    keys=[
        "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=40,
    n_events=6135192,
)


#
# GluGlueToContinToZZ
#

# cpn.add_dataset(
#    name="gluglutocontintozzto2e2mu_mcfm",
#    id=14826608,
#    processes=[procs.ggtozzto2e2mu],
#    keys=[
#        "/GluGluToContinto2Zto2E2Mu_TuneCP5_13p6TeV_mcfm701-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#    ],
#    n_files=1,
#    n_events=523444,
# )

cpn.add_dataset(
    name="gluglutocontintozzto2e2tau_mcfm",
    id=14889015,
    processes=[procs.ggtozzto2e2tau],
    keys=[
        "/GluGluToContinto2Zto2E2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=144855,
)

cpn.add_dataset(
    name="gluglutocontintozzto2mu2tau_mcfm",
    id=14889049,
    processes=[procs.ggtozzto2mu2tau],
    keys=[
        "/GluGluToContinto2Zto2Mu2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=146285,
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
