# coding: utf-8
# flake8: noqa

from order import Campaign


cpn = campaign_run3_2024_nano_v15 = Campaign(
    name="run3_2024_nano_v15",
    id=220241,
    ecm=13.6,
    aux={
        "year": 2024,
        "run": 3,
        "tier": "NanoAOD",
        "version": 15,
        "postfix": "",
    },
)

# trailing imports to load datasets
import cmsdb.campaigns.run3_2024_nano_v15.data
import cmsdb.campaigns.run3_2024_nano_v15.top
import cmsdb.campaigns.run3_2024_nano_v15.ewk
import cmsdb.campaigns.run3_2024_nano_v15.higgs
