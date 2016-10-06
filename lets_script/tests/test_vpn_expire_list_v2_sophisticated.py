import pytest
import pandas as pd
from StringIO import StringIO
import lets_script.vpn_expire_list_v2_sophisticated as expire_list


def test_finds_matching_ids():
	graduates = ['homer', 'marge', 'lisa', 'bart']
	vpn_ids = ['vpn-homer', 'vpn-maggie', 'vpn-millhouse', 'vpn-lisa']
	assert(expire_list.get_expire_list(graduates, vpn_ids) == ['vpn-homer', 'vpn-lisa'])


def test_get_eligible_deans_leave_ids():
	deans_leave_list = StringIO("""name,year
treynold,2011 
tjohns,2014 
athompso,2016 
mwilson,2012 
""")
	deans_leave_df = pd.read_csv(deans_leave_list)
	assert(expire_list.get_eligible_deans_leave_ids(deans_leave_df, '2014') == ['treynold', 'tjohns', 'mwilson'])