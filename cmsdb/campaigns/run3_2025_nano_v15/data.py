from order import DatasetInfo
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2025_nano_v15 import campaign_run3_2025_nano_v15 as cpn

cpn.add_dataset(
    name="data_mu0_b_v1",
    id=15312702,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon0/Run2025B-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=77,  # 77-0
            n_events=5602078,
        )
    ),
    aux={"era": "B", "jec_era": ""},
)

cpn.add_dataset(
    name="data_mu0_c_v1",
    id=15316054,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon0/Run2025C-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=638,  # 638-0
            n_events=250835953,
        )
    ),
    aux={"era": "C", "jec_era": ""},
)

cpn.add_dataset(
    name="data_mu0_d_v1",
    id=15369809,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon0/Run2025D-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=1166,  # 1166-0
            n_events=479676562,
        )
    ),
    aux={"era": "D", "jec_era": ""},
)

cpn.add_dataset(
    name="data_mu0_e_v1",
    id=15396801,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon0/Run2025E-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=600,  # 600-0
            n_events=263215051,
        )
    ),
    aux={"era": "E", "jec_era": ""},
)

cpn.add_dataset(
    name="data_mu1_b_v1",
    id=15312746,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon1/Run2025B-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=77,  # 77-0
            n_events=5598676,
        )
    ),
    aux={"era": "B", "jec_era": ""},
)

cpn.add_dataset(
    name="data_mu1_c_v1",
    id=15315938,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon1/Run2025C-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=644,  # 644-0
            n_events=250819768,
        )
    ),
    aux={"era": "C", "jec_era": ""},
)

cpn.add_dataset(
    name="data_mu1_d_v1",
    id=15369850,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon1/Run2025D-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=1159,  # 1159-0
            n_events=479642866,
        )
    ),
    aux={"era": "D", "jec_era": ""},
)

cpn.add_dataset(
    name="data_mu1_e_v1",
    id=15396848,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon1/Run2025E-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=605,  # 605-0
            n_events=263187770,
        )
    ),
    aux={"era": "E", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma0_b_v1",
    id=15312758,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma0/Run2025B-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
"/store/data/Run2025B/EGamma0/NANOAOD/PromptReco-v1/000/391/581/00000/83ed105e-4722-4b60-b8d6-f87a0859e7a3.root",  # empty file
"/store/data/Run2025B/EGamma0/NANOAOD/PromptReco-v1/000/392/086/00000/4d448857-826c-442c-af18-e769497e5415.root",  # empty file
                ],
            },
            n_files=73,  # 75-2
            n_events=5256904,
        )
    ),
    aux={"era": "B", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma0_c_v1",
    id=15316028,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma0/Run2025C-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=655,  # 655-0
            n_events=243682359,
        )
    ),
    aux={"era": "C", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma0_d_v1",
    id=15369886,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma0/Run2025D-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=1105,  # 1105-0
            n_events=414017171,
        )
    ),
    aux={"era": "D", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma0_e_v1",
    id=15396722,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma0/Run2025E-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=595,  # 595-0
            n_events=240927385,
        )
    ),
    aux={"era": "E", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma1_b_v1",
    id=15312679,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma1/Run2025B-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
"/store/data/Run2025B/EGamma1/NANOAOD/PromptReco-v1/000/392/090/00000/2f9660dd-3f0f-49bd-ae60-80d667cd4426.root",  # empty file
                ],
            },
            n_files=74,  # 75-1
            n_events=5253103,
        )
    ),
    aux={"era": "B", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma1_c_v1",
    id=15315987,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma1/Run2025C-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=652,  # 652-0
            n_events=243674671,
        )
    ),
    aux={"era": "C", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma1_d_v1",
    id=15369930,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma1/Run2025D-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2025D/EGamma1/NANOAOD/PromptReco-v1/000/395/517/00000/285d006b-02f9-4870-a8c3-232b45b15dd5.root" # currently unavailable
                ],
            },
            n_files=1095,  # 1096-1
            n_events=413998146,
        )
    ),
    aux={"era": "D", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma1_e_v1",
    id=15396831,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma1/Run2025E-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=596,  # 596-0
            n_events=240921314,
        )
    ),
    aux={"era": "E", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma2_b_v1",
    id=15312739,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma2/Run2025B-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=75,  # 75-0
            n_events=5254123,
        )
    ),
    aux={"era": "B", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma2_c_v1",
    id=15316003,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma2/Run2025C-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=656,  # 656-0
            n_events=243672282,
        )
    ),
    aux={"era": "C", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma2_d_v1",
    id=15369876,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma2/Run2025D-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=1121,  # 1121-0
            n_events=414008481,
        )
    ),
    aux={"era": "D", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma2_e_v1",
    id=15396769,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma2/Run2025E-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=592,  # 592-0
            n_events=240535413,
        )
    ),
    aux={"era": "E", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma3_b_v1",
    id=15312712,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma3/Run2025B-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
"/store/data/Run2025B/EGamma3/NANOAOD/PromptReco-v1/000/392/089/00000/13c371cc-1e34-4b80-aa18-af7b9f544d62.root",  # empty file
"/store/data/Run2025B/EGamma3/NANOAOD/PromptReco-v1/000/392/086/00000/19302938-b874-419e-b30c-bd7eaffeb8f9.root",  # empty file
                ],
            },
            n_files=73,  # 75-2
            n_events=5253489,
        )
    ),
    aux={"era": "B", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma3_c_v1",
    id=15316039,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma3/Run2025C-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=660,  # 660-0
            n_events=243679348,
        )
    ),
    aux={"era": "C", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma3_d_v1",
    id=15369929,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma3/Run2025D-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=1090,  # 1090-0
            n_events=414010046,
        )
    ),
    aux={"era": "D", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma3_e_v1",
    id=15396840,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma3/Run2025E-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=597,  # 597-0
            n_events=240896876,
        )
    ),
    aux={"era": "E", "jec_era": ""},
)

cpn.add_dataset(
    name="data_muoneg_b_v1",
    id=15312837,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2025B-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=47,  # 47-0
            n_events=910971,
        )
    ),
    aux={"era": "B", "jec_era": ""},
)

cpn.add_dataset(
    name="data_muoneg_c_v1",
    id=15316176,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2025C-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
"/store/data/Run2025C/MuonEG/NANOAOD/PromptReco-v1/000/392/674/00000/a67210fc-f344-40b6-a391-41b9ce40e92c.root",  # empty file
"/store/data/Run2025C/MuonEG/NANOAOD/PromptReco-v1/000/392/992/00000/0bc110c2-fa13-4a5d-8ba1-7d383dc05613.root",  # empty file
                ],
            },
            n_files=170,  # 172-2
            n_events=41994774,
        )
    ),
    aux={"era": "C", "jec_era": ""},
)

cpn.add_dataset(
    name="data_muoneg_d_v1",
    id=15374208,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2025D-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
"/store/data/Run2025D/MuonEG/NANOAOD/PromptReco-v1/000/395/188/00000/7e5cc229-ede7-4a4a-88ef-d10b41f3ec5a.root",  # empty file
"/store/data/Run2025D/MuonEG/NANOAOD/PromptReco-v1/000/395/187/00000/f9ddbea8-810f-4995-aa10-3c0dede035dc.root",  # empty file
"/store/data/Run2025D/MuonEG/NANOAOD/PromptReco-v1/000/395/518/00000/391d1b46-ab1a-4214-b22f-b2ff2e53bcc1.root",  # empty file
"/store/data/Run2025D/MuonEG/NANOAOD/PromptReco-v1/000/395/640/00000/bee90dfb-e61e-4874-8427-220aacc6cd63.root",  # empty file
                ],
            },
            n_files=325,  # 329-4
            n_events=72820407,
        )
    ),
    aux={"era": "D", "jec_era": ""},
)

cpn.add_dataset(
    name="data_muoneg_e_v1",
    id=15396290,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2025E-PromptReco-v1/NANOAOD",
            ],
            aux={
                "broken_files": [
"/store/data/Run2025E/MuonEG/NANOAOD/PromptReco-v1/000/396/155/00000/4d2a409c-e578-4392-96b4-4b664009d9dd.root",  # empty file
                ],
            },
            n_files=164,  # 165-1
            n_events=40691496,
        )
    ),
    aux={"era": "E", "jec_era": ""},
)

cpn.add_dataset(
    name="data_mu0_c_v2",
    id=15337002,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon0/Run2025C-PromptReco-v2/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=356,  # 356-0
            n_events=148575745,
        )
    ),
    aux={"era": "C", "jec_era": ""},
)

cpn.add_dataset(
    name="data_mu1_c_v2",
    id=15337600,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon1/Run2025C-PromptReco-v2/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=350,  # 350-0
            n_events=148565659,
        )
    ),
    aux={"era": "C", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma0_c_v2",
    id=15337612,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma0/Run2025C-PromptReco-v2/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=342,  # 342-0
            n_events=133952379,
        )
    ),
    aux={"era": "C", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma1_c_v2",
    id=15336258,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma1/Run2025C-PromptReco-v2/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=347,  # 347-0
            n_events=133951067,
        )
    ),
    aux={"era": "C", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma2_c_v2",
    id=15336993,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma2/Run2025C-PromptReco-v2/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=351,  # 351-0
            n_events=133950574,
        )
    ),
    aux={"era": "C", "jec_era": ""},
)

cpn.add_dataset(
    name="data_egamma3_c_v2",
    id=15336578,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma3/Run2025C-PromptReco-v2/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=343,  # 343-0
            n_events=133949781,
        )
    ),
    aux={"era": "C", "jec_era": ""},
)

cpn.add_dataset(
    name="data_muoneg_c_v2",
    id=15337052,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2025C-PromptReco-v2/NANOAOD",
            ],
            aux={
                "broken_files": [
                ],
            },
            n_files=92,  # 92-0
            n_events=23203653,
        )
    ),
    aux={"era": "C", "jec_era": ""},
)
