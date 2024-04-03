# coding: utf-8

from order import Campaign

import cmsdb.processes as procs


cpn = campaign_run2_2018_nano_v9 = Campaign(
    name="run2_2018_nano_v9",
    id=220181,
    ecm=13,
    bx=25,
    aux={"year": 2018, "tier": "NanoAOD", "version": "9"},
)

# trailing imports to load datasets
import cmsdb.campaigns.run2_2018_nano_v9.data
import cmsdb.campaigns.run2_2018_nano_v9.top
import cmsdb.campaigns.run2_2018_nano_v9.ewk
import cmsdb.campaigns.run2_2018_nano_v9.qcd