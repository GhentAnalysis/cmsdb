# coding: utf-8

"""
Common, analysis independent definition of the 2025 data-taking campaign
with datasets at NanoAOD tier in version 11. 
The corresponding set of MC samples include a siMuonlation of the detector.
See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign


#
# campaign
#

campaign_run3_2025_nano_v15 = Campaign(
    name="run3_2025_nano_v15",
    id=320221101,  # 3 2022 11 01(u)
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "year": 2025,
        "version": 15,
        "run": 3,
    },
)

# trailing imports to load datasets
import cmsdb.campaigns.run3_2025_nano_v15.data  # noqa
