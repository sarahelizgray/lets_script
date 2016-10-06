import pytest
import lets_script.vpn_expire_list_v1_tested as expire_list


def test_finds_matching_ids():
    graduates = ['homer', 'marge', 'lisa', 'bart']
    vpn_ids = ['vpn-homer', 'vpn-maggie', 'vpn-millhouse', 'vpn-lisa']
    assert(expire_list.get_expire_list(
        graduates, vpn_ids) == ['vpn-homer', 'vpn-lisa'])
