# coding: utf-8

"""
Top-related process definitions.
"""

__all__ = [
    "tt",
    "tt_sl", "tt_dl", "tt_fh",
    "st",
    "st_tchannel", "st_tchannel_t", "st_tchannel_tbar",
    "st_twchannel", "st_twchannel_t", "st_twchannel_tbar",
    "st_twchannel_t_sl", "st_twchannel_tbar_sl",
    "st_twchannel_t_dl", "st_twchannel_tbar_dl",
    "st_twchannel_t_fh", "st_twchannel_tbar_fh",
    "st_schannel", "st_schannel_lep", "st_schannel_had",
    "st_schannel_t", "st_schannel_t_lep", "st_schannel_t_had",
    "st_schannel_tbar", "st_schannel_tbar_lep", "st_schannel_tbar_had",
    "tzq",
    "twz", "twztoll_thad_wlept_5f", "twztoll_tlept_whad_5f", "twztoll_tlept_wlept_5f",
    "ttv",
    "ttz", "ttz_llnunu_m10", "ttz_llnunu_m1",
    "ttw", "ttw_lnu", "ttw_qq",
    "tth", "tthjetstononbb",
    "ttgamma", "ttgamma_dilept",
    "ttxx",
    "ttvv",
    "ttzz", "ttwz", "ttww", "tthh", "ttwh", "ttzh", "tttt"
]

from order import Process
from scinum import Number

import cmsdb.constants as const


#
# ttbar
# (ids up to 1999)
#
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO?rev=16#Top_quark_pair_cross_sections_at
# use mtop = 172.5 GeV, see
# https://twiki.cern.ch/twiki/bin/view/CMS/TopMonteCarloSystematics?rev=7#mtop
#

tt = Process(
    name="tt",
    id=1000,
    label=r"$t\bar{t}$",
    color=(205, 0, 9),
    xsecs={
        13: Number(831.76, {
            "scale": (19.77, 29.20),
            "pdf": 35.06,
            "mtop": (23.18, 22.45),
        }),
    },
)

tt_sl = tt.add_process(
    name="tt_sl",
    id=1100,
    label=f"{tt.label}, SL",
    color=(205, 0, 9),
    xsecs={
        13: tt.get_xsec(13) * const.br_ww.sl,
    },
)

tt_dl = tt.add_process(
    name="tt_dl",
    id=1200,
    label=f"{tt.label}, DL",
    color=(235, 230, 10),
    xsecs={
        13: tt.get_xsec(13) * const.br_ww.dl,
    },
)

tt_fh = tt.add_process(
    name="tt_fh",
    id=1300,
    label=f"{tt.label}, FH",
    color=(255, 153, 0),
    xsecs={
        13: tt.get_xsec(13) * const.br_ww.fh,
    },
)


#
# single-top
#
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma?rev=12#Single_Top_Cross_sections_at_13
#

st = Process(
    name="st",
    id=2000,
    label=r"Single $t$/$\bar{t}$",
    color=(2, 210, 209),
)

st_tchannel = st.add_process(
    name="st_tchannel",
    id=2100,
    label=f"{st.label}, t-channel",
    xsecs={
        13: Number(216.99, dict(
            scale=(6.62, 4.64),
            pdf=6.16,  # includes alpha_s
            mtop=1.81,
        )),
    },
)

st_tchannel_t = st_tchannel.add_process(
    name="st_tchannel_t",
    label=r"Single $t$, t-channel",
    id=2110,
    xsecs={
        13: Number(136.02, dict(
            scale=(4.09, 2.92),
            pdf=3.52,  # includes alpha_s
            mtop=1.11,
        )),
    },
)

st_tchannel_tbar = st_tchannel.add_process(
    name="st_tchannel_tbar",
    label=r"Single $\bar{t}$, t-channel",
    id=2120,
    xsecs={
        13: Number(80.95, dict(
            scale=(2.53, 1.71),
            pdf=3.18,  # includes alpha_s
            mtop=(0.71, 0.70),
        )),
    },
)

st_twchannel = st.add_process(
    name="st_twchannel",
    id=2200,
    label=f"{st.label}, tW-channel",
    xsecs={
        13: Number(71.7, dict(
            scale=1.8,
            pdf=3.4,
        )),
    },
)

st_twchannel_t = st_twchannel.add_process(
    name="st_twchannel_t",
    id=2210,
    xsecs={
        13: Number(35.85, dict(
            scale=0.90,
            pdf=1.70,
        )),
    },
)

st_twchannel_t_sl = st_twchannel_t.add_process(
    name="st_twchannel_t_sl",
    id=2211,
    xsecs={13: Number(0.1)},  # TODO
)

st_twchannel_t_dl = st_twchannel_t.add_process(
    name="st_twchannel_t_dl",
    id=2212,
    xsecs={13: Number(0.1)},  # TODO
)

st_twchannel_t_fh = st_twchannel_t.add_process(
    name="st_twchannel_t_fh",
    id=2213,
    xsecs={13: Number(0.1)},  # TODO
)

st_twchannel_tbar = st_twchannel.add_process(
    name="st_twchannel_tbar",
    id=2220,
    xsecs={
        13: Number(35.85, dict(
            scale=0.90,
            pdf=1.70,
        )),
    },
)

st_twchannel_tbar_sl = st_twchannel_tbar.add_process(
    name="st_twchannel_tbar_sl",
    id=2221,
    xsecs={13: Number(0.1)},  # TODO
)

st_twchannel_tbar_dl = st_twchannel_tbar.add_process(
    name="st_twchannel_tbar_dl",
    id=2222,
    xsecs={13: Number(0.1)},  # TODO
)

st_twchannel_tbar_fh = st_twchannel_tbar.add_process(
    name="st_twchannel_tbar_fh",
    id=2223,
    xsecs={13: Number(0.1)},  # TODO
)

st_schannel = st.add_process(
    name="st_schannel",
    id=2300,
    label=f"{st.label}, s-channel",
    xsecs={
        13: Number(11.36, dict(
            scale=0.18,
            pdf=(0.40, 0.45),
        )),
    },
)

st_schannel_lep = st_schannel.add_process(
    name="st_schannel_lep",
    id=2301,
    xsecs={
        13: st_schannel.get_xsec(13) * const.br_w.lep,
    },
)

st_schannel_had = st_schannel.add_process(
    name="st_schannel_had",
    id=2302,
    xsecs={
        13: st_schannel.get_xsec(13) * const.br_w.had,
    },
)

st_schannel_t = st_schannel.add_process(
    name="st_schannel_t",
    id=2310,
    xsecs={
        13: Number(7.20, dict(
            scale=0.13,
            pdf=(0.29, 0.23),
        )),
    },
)

st_schannel_t_lep = st_schannel_t.add_process(
    name="st_schannel_t_lep",
    id=2311,
    xsecs={
        13: st_schannel_t.get_xsec(13) * const.br_w.lep,
    },
)

st_schannel_t_had = st_schannel_t.add_process(
    name="st_schannel_t_had",
    id=2312,
    xsecs={
        13: st_schannel_t.get_xsec(13) * const.br_w.had,
    },
)

st_schannel_tbar = st_schannel.add_process(
    name="st_schannel_tbar",
    id=2320,
    xsecs={
        13: Number(4.16, dict(
            scale=0.05,
            pdf=(0.12, 0.23),
        )),
    },
)

st_schannel_tbar_lep = st_schannel_tbar.add_process(
    name="st_schannel_tbar_lep",
    id=2321,
    xsecs={
        13: st_schannel_tbar.get_xsec(13) * const.br_w.lep,
    },
)

st_schannel_tbar_had = st_schannel_tbar.add_process(
    name="st_schannel_tbar_had",
    id=2322,
    xsecs={
        13: st_schannel_tbar.get_xsec(13) * const.br_w.had,
    },
)

# define the combined single top cross section as the sum of the three channels
st.set_xsec(
    13,
    st_tchannel.get_xsec(13) + st_twchannel.get_xsec(13) + st_schannel.get_xsec(13),
)

# Single top + vector boson

tzq = Process(
    name="tzq",
    id=2500,
    label='tZq',
    xsecs={13: 0.07358},
)

twz = Process(
    name="twz",
    id=2600,
    label='tWZ',
    xsecs={13: Number(0.1)},
)

twztoll_thad_wlept_5f = twz.add_process(
    name="twztoll_thad_wlept_5f",
    id=2610,
    label='twztoll_thad_wlept_5f',
    xsecs={13: Number(0.003004)},
)

twztoll_tlept_whad_5f = twz.add_process(
    name="twztoll_tlept_whad_5f",
    id=2620,
    label='twztoll_tlept_whad_5f',
    xsecs={13: Number(0.003004)},
)

twztoll_tlept_wlept_5f = twz.add_process(
    name="twztoll_tlept_wlept_5f",
    id=2630,
    label='twztoll_tlept_wlept_5f',
    xsecs={13: Number(0.0015)},
)


#
# ttbar + 1 vector boson
#


ttv = Process(
    name="ttv",
    id=3000,
    label=f"{tt.label} + V",
    xsecs={13: Number(0.1)},  # TODO
)

ttz = ttv.add_process(
    name="ttz",
    id=3100,
    label=f"{tt.label} + Z",
    xsecs={13: Number(0.1)},  # TODO
)

ttz_llnunu_m10 = ttz.add_process(
    name="ttz_llnunu_m10",  # non-hadronically decaying Z m10>
    id=3110,
    xsecs={13: 0.281},
)


ttz_llnunu_m1 = ttz.add_process(
    name="ttz_llnunu_m1",  # non-hadronically decaying Z m1-10
    id=3120,
    xsecs={13: 0.08416},
)

ttz.set_xsec(
    13,
    ttz_llnunu_m10.get_xsec(13) + ttz_llnunu_m1.get_xsec(13)
)


ttw = ttv.add_process(
    name="ttw",
    id=3200,
    label=f"{tt.label} + W",
    xsecs={13: Number(0.1)},  # TODO
)

ttw_lnu = ttw.add_process(
    name="ttw_lnu",
    id=3210,
    xsecs={13: Number(0.235)},
)

ttw_qq = ttw.add_process(
    name="ttw_qq",
    id=3220,
    xsecs={13: Number(0.1)},  # TODO
)


tth = ttv.add_process(
    name="tth",
    id=3300,
    label=f"{tt.label} + H",
    xsecs={13: Number(0.1)},  # TODO
)

tthjetstononbb = tth.add_process(
    name="tthjetstononbb",
    id=3310,
    label=f"{tt.label} + H (nonbb)",
    xsecs={13: Number(0.211)},
)

ttgamma = ttv.add_process(
    name="ttgamma",
    id=3400,
    label=f"${tt.label} + \gamma$",
    xsecs={13: Number(0.1)},  # TODO
)

ttgamma_dilept = ttgamma.add_process(
    name="ttgamma_dilept",
    id=3410,
    label=f"${tt.label} + \gamma(ll)$",
    xsecs={13: Number(2.22)},
)


#
# ttbar + 2 bosons/fermions
#

ttxx = Process(
    name="ttxx",
    id=3999,
    label=f"{tt.label} + XX",
    xsecs={13: Number(0.1)},
)

#
# ttbar + 2 vector bosons
#


ttvv = ttxx.add_process(
    name="ttvv",
    id=4000,
    label=f"{tt.label} + VV",
    xsecs={13: Number(0.1)},
)

ttzz = ttvv.add_process(
    name="ttzz",
    id=4100,
    xsecs={13: Number(0.001386)},
)

ttwz = ttvv.add_process(
    name="ttwz",
    id=4200,
    xsecs={13: Number(0.002453)},
)

ttww = ttvv.add_process(
    name="ttww",
    id=4300,
    xsecs={13: Number(0.007003)},
)

#
# ttbar + 2 bosons with atleast 1 Higgs
#

tthh = ttxx.add_process(
    name="tthh",
    id=4400,
    label=f"{tt.label} + HH",
    xsecs={13: Number(0.0003697)},
)

ttwh = ttxx.add_process(
    name="ttwh",
    id=4500,
    label=f"{tt.label} + WH",
    xsecs={13: Number(0.001141)},
)

ttzh = ttxx.add_process(
    name="ttzh",
    id=4600,
    label=f"{tt.label} + ZH",
    xsecs={13: Number(0.00113)},
)

tttt = ttxx.add_process(
    name="ttt",
    id=4700,
    label=f"{tt.label}{tt.label}",
    xsecs={13: Number(0.01337)},
)
