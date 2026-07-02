# coding: utf-8

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn24

# ------------------------------------------------
# QCD (pythia, pt-binned, muon enriched)
# ------------------------------------------------

for cpn in [cpn24]:

    cpn.add_dataset(
        name="qcd_mu_pt15to20_pythia",
        id=15316273,
        processes=[procs.qcd_mu_pt15to20],
        keys=[
            "/QCD_Bin-PT-15to20_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
        ],
        n_files=859,
        n_events=124873343,
    )

    cpn.add_dataset(
        name="qcd_mu_pt20to30_pythia",
        id=15315886,
        processes=[procs.qcd_mu_pt20to30],
        keys=[
            "/QCD_Bin-PT-20to30_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
        ],
        n_files=657,
        n_events=93246015,
    )
    cpn.add_dataset(
        name="qcd_mu_pt30to50_pythia",
        id=15315309,
        processes=[procs.qcd_mu_pt30to50],
        keys=[
            "/QCD_Bin-PT-30to50_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
        ],
        n_files=729,
        n_events=95229839,
    )
    cpn.add_dataset(
        name="qcd_mu_pt50to80_pythia",
        id=15316568,
        processes=[procs.qcd_mu_pt50to80],
        keys=[
            "/QCD_Bin-PT-50to80_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
        ],
        n_files=714,
        n_events=107361868,
    )
    cpn.add_dataset(
        name="qcd_mu_pt80to120_pythia",
        id=15316584,
        processes=[procs.qcd_mu_pt80to120],
        keys=[
            "/QCD_Bin-PT-80to120_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
        ],
        n_files=680,
        n_events=94158748,
    )
    cpn.add_dataset(
        name="qcd_mu_pt120to170_pythia",
        id=15316135,
        processes=[procs.qcd_mu_pt120to170],
        keys=[
            "/QCD_Bin-PT-120to170_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
        ],
        n_files=683,
        n_events=99977764,
    )
    cpn.add_dataset(
        name="qcd_mu_pt170to300_pythia",
        id=15315581,
        processes=[procs.qcd_mu_pt170to300],
        keys=[
            "/QCD_Bin-PT-170to300_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
        ],
        n_files=695,
        n_events=94354003,
    )
    cpn.add_dataset(
        name="qcd_mu_pt300to470_pythia",
        id=15315699,
        processes=[procs.qcd_mu_pt300to470],
        keys=[
            "/QCD_Bin-PT-300to470_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
        ],
        n_files=591,
        n_events=79686379,
    )
    cpn.add_dataset(
        name="qcd_mu_pt470to600_pythia",
        id=15316109,
        processes=[procs.qcd_mu_pt470to600],
        keys=[
            "/QCD_Bin-PT-470to600_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
        ],
        n_files=590,
        n_events=71842009,
    )
    cpn.add_dataset(
        name="qcd_mu_pt600to800_pythia",
        id=15315212,
        processes=[procs.qcd_mu_pt600to800],
        keys=[
            "/QCD_Bin-PT-600to800_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
        ],
        n_files=764,
        n_events=85759452,
    )
    cpn.add_dataset(
        name="qcd_mu_pt800to1000_pythia",
        id=15315633,
        processes=[procs.qcd_mu_pt800to1000],
        keys=[
            "/QCD_Bin-PT-800to1000_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
        ],
        n_files=673,
        n_events=81633640,
    )
    cpn.add_dataset(
        name="qcd_mu_pt1000toinf_pythia",
        id=15316533,
        processes=[procs.qcd_mu_pt1000toinf],
        keys=[
            "/QCD_Bin-PT-1000_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
        ],
        n_files=703,
        n_events=87267908,
    )

    # ------------------------------------------------
    # QCD (pythia, pt-binned, electron enriched)
    # ------------------------------------------------
