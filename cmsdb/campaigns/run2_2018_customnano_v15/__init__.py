# coding: utf-8

"""
Common, analysis independent definition of the 2018 data-taking campaign with privately
produced custom NanoAOD (CustomNanoAODv15-NanoTuples-uParTv3-parTlepID) datasets, reprocessed
from the RunIISummer20UL18 MiniAODv2 samples.

See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das, instance prod/phys03).
"""

from order import Campaign


#
# campaign
#

campaign_run2_2018_customnano_v15 = Campaign(
    name="run2_2018_customnano_v15",
    id=220181501,  # 2 2018 15 01(u)
    ecm=13,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "year": 2018,
        "version": 15,
        "run": 2,
        "postfix": "",
        "is_custom": True,
    },
)


# trailing imports to load datasets
import cmsdb.campaigns.run2_2018_customnano_v15.top  # noqa
import cmsdb.campaigns.run2_2018_customnano_v15.ewk  # noqa
import cmsdb.campaigns.run2_2018_customnano_v15.higgs  # noqa
import cmsdb.campaigns.run2_2018_customnano_v15.data  # noqa
