# coding: utf-8

"""
Electroweak datasets for the 2023 post-BPix data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_v12 import campaign_run3_2023_postBPix_nano_v12 as cpn

####################################################################################################
#
# Drell-Yan
#
####################################################################################################


#
# LO
#

cpn.add_dataset(
    name="dy_m10to50_madgraph",
    id=14889366,
    processes=[procs.dy_m10to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-10to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=481,
            n_events=142310722,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_madgraph",
    id=14846437,
    processes=[procs.dy_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=218,
            n_events=69035447,
        ),
    ),
)

#
# NLO
#

cpn.add_dataset(
    name="dy_m10to50_amcatnlo",
    id=14905314,
    processes=[procs.dy_m10to50],
    info=dict(
        # NOTE: this is an extension, but there was no "non-extension" dataset to be found in DAS
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2_ext1-v3/NANOAODSIM",  # noqa
            ],
            n_files=328,
            n_events=100386286,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_amcatnlo",
    id=14851777,
    processes=[procs.dy_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=221,
            n_events=95472230,
        ),
    ),
)

####################################################################################################
#
# W boson production
#
####################################################################################################

#
# NLO
#

cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14978436,
    processes=[procs.w_lnu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=352,
            n_events=95759797,
        ),
    ),
)

####################################################################################################
#
# Diboson
#
####################################################################################################

#
# ZZ
#

cpn.add_dataset(
    name="zz_pythia",
    id=14784123,
    is_data=False,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=2517000,
)

cpn.add_dataset(
    name="zz_zll_zll_powheg",
    id=14888198,
    processes=[procs.zz_zll_zll],
    keys=[
        "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=81,
    n_events=14625000,
)

#
# WZ
#

cpn.add_dataset(
    name="wz_pythia",
    id=14784070,
    is_data=False,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=8379000,
)

cpn.add_dataset(
    name="wz_wlnu_zll_powheg",
    id=14837052,
    is_data=False,
    processes=[procs.wz_wlnu_zll],
    keys=[
        "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
        "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=34 + 53,
    n_events=2713000 + 10312000,
)

cpn.add_dataset(
    name="wz_wlnu_zll_1jets_amcatnlo",
    id=15204555,
    is_data=False,
    processes=[procs.wz_wlnu_zll_1jets],  # TODO change processes to 1 jet specific
    keys=[
        "/WZto3LNu-1Jets-4FS_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6_ext1-v2/NANOAODSIM"  # noqa
    ],
    n_files=57,
    n_events=11200104,
)

#
# GluGluToContinToZZ
#

cpn.add_dataset(
    name="ggtozzto2e2mu_mcfm",
    id=15016914,
    processes=[procs.ggtozzto2e2mu],
    keys=[
        "/GluGluToContinto2Zto2E2Mu_TuneCP5_13p6TeV_mcfm701-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=512000,
)

cpn.add_dataset(
    name="ggtozzto2e2tau_mcfm",
    id=15020485,
    processes=[procs.ggtozzto2e2tau],
    keys=[
        "/GluGluToContinto2Zto2E2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=524000,
)

cpn.add_dataset(
    name="ggtozzto2mu2tau_mcfm",
    id=15017227,
    processes=[procs.ggtozzto2mu2tau],
    keys=[
        "/GluGluToContinto2Zto2Mu2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=516000,
)

cpn.add_dataset(
    name="ggtozzto4e_mcfm",
    id=14930991,
    processes=[procs.ggtozzto4e],
    keys=[
        "/GluGlutoContinto2Zto4E_TuneCP5_13p6TeV_mcfm701-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=375000,
)

cpn.add_dataset(
    name="ggtozzto4mu_mcfm",
    id=14944685,
    processes=[procs.ggtozzto4mu],
    keys=[
        "/GluGlutoContinto2Zto4Mu_TuneCP5_13p6TeV_mcfm701-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=371000,
)

cpn.add_dataset(
    name="ggtozzto4tau_mcfm",
    id=14944419,
    processes=[procs.ggtozzto4tau],
    keys=[
        "/GluGlutoContinto2Zto4Tau_TuneCP5_13p6TeV_mcfm701-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=375000,
)

#
# WW
#

cpn.add_dataset(
    name="ww_pythia",
    id=14783236,
    processes=[procs.ww],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=54,
            n_events=16734000,
        ),
    ),
)


cpn.add_dataset(
    name="ww_fh_powheg",
    id=14836868,
    processes=[procs.ww_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=166,
            n_events=27640000,
        ),
    ),
)

cpn.add_dataset(
    name="ww_wlnu_wlnu_powheg",
    id=14837063,
    processes=[procs.ww_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=92,
            n_events=6390000,
        ),
    ),
)
cpn.add_dataset(
    name="ww_sl_powheg",
    id=14839745,
    processes=[procs.ww_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=212,
            n_events=26336000,
        ),
    ),
)


####################################################################################################
#
# Triboson
#
####################################################################################################

cpn.add_dataset(
    name="wwz_amcatnlo",
    id=14827071,
    processes=[procs.wwz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=28,
            n_events=1746000,
        ),
    ),
)
cpn.add_dataset(
    name="www__amcatnlo",
    id=14787825,
    processes=[procs.www],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=2,
            n_events=466500,
        ),
    ),
)

cpn.add_dataset(
    name="wzz__amcatnlo",
    id=14788046,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=1788000,
)

cpn.add_dataset(
    name="zzz__amcatnlo",
    id=14784436,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=1788000,
)
