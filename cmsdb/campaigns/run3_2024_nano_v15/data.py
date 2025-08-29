

from order import DatasetInfo
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn


#
# EGamma
#

cpn.add_dataset(
    name="data_egamma0_c",
    id=15289158,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/Run2024C-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=167,
    n_events=157351226,
    aux={
        'era': 'C'
    }
)

cpn.add_dataset(
    name="data_egamma1_c",
    id=15297142,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/Run2024C-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=247,
    n_events=157860731,
    aux={
        'era': 'C'
    }
)

cpn.add_dataset(
    name="data_egamma0_d",
    id=15291573,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/Run2024D-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=173,
    n_events=156558757,
    aux={
        'era': 'D'
    }
)

# /EGamma1/Run2024D-MINIv6NANOv15-v1/NANOAOD
cpn.add_dataset(
    name="data_egamma1_d",
    id=15290911,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/Run2024D-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=279,
    n_events=156275778,
    aux={
        'era': 'D'
    }
)

cpn.add_dataset(
    name="data_egamma0_e",
    id=15291143,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/Run2024E-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=267,
    n_events=249417634,
    aux={
        'era': 'E'
    }
)

cpn.add_dataset(
    name="data_egamma1_e",
    id=15291110,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/Run2024E-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=335,
    n_events=249489829,
    aux={
        'era': 'E'
    }
)

cpn.add_dataset(
    name="data_egamma0_f",
    id=15290277,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/Run2024F-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=719,
    n_events=638196622,
    aux={
        'era': 'F'
    }
)

cpn.add_dataset(
    name="data_egamma1_f",
    id=15291531,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/Run2024F-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=747,
    n_events=631079889,
    aux={
        'era': 'F'
    }
)

cpn.add_dataset(
    name="data_egamma0_g",
    id=15299541,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/Run2024G-MINIv6NANOv15-v2/NANOAOD",
    ],
    n_files=850,
    n_events=903520258,
    aux={
        'era': 'G'
    }
)

cpn.add_dataset(
    name="data_egamma1_g",
    id=15299535,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/Run2024G-MINIv6NANOv15-v2/NANOAOD",
    ],
    n_files=888,
    n_events=903441926,
    aux={
        'era': 'G'
    }
)

cpn.add_dataset(
    name="data_egamma0_h",
    id=15299993,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/Run2024H-MINIv6NANOv15-v2/NANOAOD",
    ],
    n_files=138,
    n_events=134680448,
    aux={
        'era': 'H'
    }
)

cpn.add_dataset(
    name="data_egamma1_h",
    id=15291566,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/Run2024H-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=191,
    n_events=134835799,
    aux={
        'era': 'H'
    }
)

cpn.add_dataset(
    name="data_egamma0_i",
    id=15291530,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/Run2024I-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=211,
    n_events=132904290,
    aux={
        'era': 'I'
    }
)

cpn.add_dataset(
    name="data_egamma1_i",
    id=1529151515,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/Run2024I-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=176,
    n_events=132903874,
    aux={
        'era': 'I'
    }
)

cpn.add_dataset(
    name="data_egamma0_j",
    id=15291464,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD",
    ],
    n_files=198,
    n_events=150687674,
    aux={
        'era': 'J'
    }
)

cpn.add_dataset(
    name="data_egamma1_j",
    id=15291646,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/EGamma1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD",
    ],
    n_files=179,
    n_events=150687112,
    aux={
        'era': 'J'
    }
)


#
# Muon
#

cpn.add_dataset(
    name="data_mu0_c",
    id=15288695,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/Run2024C-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=103,
    n_events=97505587,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name="data_mu1_c",
    id=15289035,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon1/Run2024C-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=94,
    n_events=97531998,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name="data_mu0_d",
    id=15291308,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/Run2024D-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=180,
    n_events=120787065,
    aux={'era': 'D'}
)

cpn.add_dataset(
    name="data_mu1_d",
    id=15291184,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon1/Run2024D-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=168,
    n_events=120467371,
    aux={'era': 'D'}
)

cpn.add_dataset(
    name="data_mu0_e",
    id=15297256,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/Run2024E-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=255,
    n_events=169640946,
    aux={'era': 'E'}
)

cpn.add_dataset(
    name="data_mu1_e",
    id=15291567,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon1/Run2024E-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=171,
    n_events=172848674,
    aux={'era': 'E'}
)

cpn.add_dataset(
    name="data_mu0_f",
    id=15291901,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/Run2024F-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=594,
    n_events=442432787,
    aux={'era': 'F'}
)

cpn.add_dataset(
    name="data_mu1_f",
    id=15291534,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon1/Run2024F-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=538,
    n_events=442360423,
    aux={'era': 'F'}
)

cpn.add_dataset(
    name="data_mu0_g",
    id=15291960,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/Run2024G-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=948,
    n_events=642028803,
    aux={'era': 'G'}
)

cpn.add_dataset(
    name="data_mu1_g",
    id=15299779,
    is_data=True,
    processes=[procs.data],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon1/Run2024G-MINIv6NANOv15-v2/NANOAOD",
            ],
            n_files=565,
            n_events=641959643,
            aux={
                "broken_files": [
                ]
            }
        )
    ),
    aux={'era': 'G'},
)

cpn.add_dataset(
    name="data_mu0_h",
    id=15291794,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/Run2024H-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=152,
    n_events=93983627,
    aux={'era': 'H'}
)

cpn.add_dataset(
    name="data_mu1_h",
    id=15299529,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon1/Run2024H-MINIv6NANOv15-v2/NANOAOD",
    ],
    n_files=93,
    n_events=93981102,
    aux={'era': 'H'}
)

cpn.add_dataset(
    name="data_mu0_i",
    id=15291900,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/Run2024I-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=173,
    n_events=97634104,
    aux={'era': 'I'}
)

cpn.add_dataset(
    name="data_mu1_i",
    id=-1,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon1/Run2024I-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=94,
    n_events=97630010,
    aux={'era': 'I'}
)

cpn.add_dataset(
    name="data_mu0_j",
    id=-15259292,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD",
    ],
    n_files=174,
    n_events=105194627,
    aux={'era': 'I'}
)

cpn.add_dataset(
    name="data_mu1_j",
    id=15291176,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/Muon1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD",
    ],
    n_files=133,
    n_events=105189040,
    aux={'era': 'I'}
)

#
# MuonEG
#

cpn.add_dataset(
    name="data_muoneg_c",
    id=15288975,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/Run2024C-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=35,
    n_events=18312408,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name="data_muoneg_d",
    id=15291188,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/Run2024D-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=47,
    n_events=18827708,
    aux={'era': 'D'}
)

cpn.add_dataset(
    name="data_muoneg_e",
    id=15290662,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/Run2024E-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=63,
    n_events=26319233,
    aux={'era': 'E'}
)

cpn.add_dataset(
    name="data_muoneg_f",
    id=15299473,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/Run2024F-MINIv6NANOv15-v2/NANOAOD",
    ],
    n_files=106,
    n_events=67341687,
    aux={'era': 'F'}
)

cpn.add_dataset(
    name="data_muoneg_g",
    id=15297392,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/Run2024G-MINIv6NANOv15-v3/NANOAOD",
    ],
    n_files=150,
    n_events=97985222,
    aux={'era': 'G'}
)

cpn.add_dataset(
    name="data_muoneg_h",
    id=15299540,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/Run2024H-MINIv6NANOv15-v2/NANOAOD",
    ],
    n_files=25,
    n_events=14323522,
    aux={'era': 'H'}
)

cpn.add_dataset(
    name="data_muoneg_i",
    id=15299590,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/Run2024I-MINIv6NANOv15-v2/NANOAOD",
    ],
    n_files=23,
    n_events=14579063,
    aux={'era': 'I'}
)

cpn.add_dataset(
    name="data_muoneg_j",
    id=15299587,
    is_data=True,
    processes=[procs.data],
    keys=[
        "/MuonEG/Run2024I-MINIv6NANOv15_v2-v2/NANOAOD",
    ],
    n_files=22,
    n_events=14674636,
    aux={'era': 'I'}
)
