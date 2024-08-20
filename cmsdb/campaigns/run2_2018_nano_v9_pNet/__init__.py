# coding: utf-8

from order import Campaign

import cmsdb.processes as procs


cpn = campaign_run2_2018_nano_v9_pNet = Campaign(
    name="run2_2018_nano_v9_pNet",
    id=220181,
    ecm=13,
    bx=25,
    aux={"year": 2018, "run": 2, "tier": "NanoAOD", "version": "9"},
)

# trailing imports to load datasets
import cmsdb.campaigns.run2_2018_nano_v9_pNet.data
import cmsdb.campaigns.run2_2018_nano_v9_pNet.top
import cmsdb.campaigns.run2_2018_nano_v9_pNet.ewk
