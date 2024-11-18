# coding: utf-8

"""
Common, analysis independent definition of the 2018 data-taking campaign
with datasets at NanoAOD tier in version 9.
See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign, DatasetInfo

import cmsdb.processes as procs


#
# campaign
#

cpn = campaign_run2_2018_nano_v9 = Campaign(
    name="run2_2018_nano_v9",
    id=220181,
    ecm=13,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 2,
        "year": 2018,
        "version": 9,
        "postfix": "",
    },
)

# trailing imports to load datasets
import cmsdb.campaigns.run2_2018_nano_v9.data
import cmsdb.campaigns.run2_2018_nano_v9.top
import cmsdb.campaigns.run2_2018_nano_v9.ewk
import cmsdb.campaigns.run2_2018_nano_v9.qcd
