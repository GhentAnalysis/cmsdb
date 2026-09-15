# coding: utf-8

"""
Common, analysis independent definition of the 2024 customNanoAOD data-taking campaign
with datasets at CustomNanoAOD tier in version 15. The 'custom' refers to a modified
version of the standard NanoAOD format, including PNet Lepton ID and other enhancements.
The corresponding set of MC samples include a simulation of the detector including
the endcap region that was later affected by the leak.

See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign


#
# campaign
#

campaign_run3_2024_customnano_v15 = Campaign(
    name="run3_2024_customnano_v15",
    id=320241201,  # 3 2024 15 01(u)
    ecm=13.6,
    bx=25,
    aux={
        "tier": "CustomNanoAOD",
        "year": 2024,
        "version": 15,
        "run": 3,
        "postfix": "",
    },
)


# trailing imports to load datasets
import cmsdb.campaigns.run3_2024_customnano_v15.top  # noqa
import cmsdb.campaigns.run3_2024_customnano_v15.ewk  # noqa
import cmsdb.campaigns.run3_2024_customnano_v15.higgs  # noqa
import cmsdb.campaigns.run3_2024_customnano_v15.data  # noqa
import cmsdb.campaigns.run3_2024_customnano_v15.qcd  # noqa