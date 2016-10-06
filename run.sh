#!/bin/bash


echo Naive Implementation 1
rm lets_script/examples/vpn_accounts_to_expire_v1.csv
python lets_script/vpn_expire_list_v1.py

echo Refined Implementation 1
rm lets_script/examples/vpn_accounts_to_expire_v1_refined.csv
python lets_script/vpn_expire_list_v1_refined.py

echo Tested Implementation 1
rm lets_script/examples/vpn_accounts_to_expire_v1_tested.csv
python lets_script/vpn_expire_list_v1_tested.py

echo Naive Implementation 2
rm lets_script/examples/vpn_accounts_to_expire_v2.csv
python lets_script/vpn_expire_list_v2.py lets_script/examples/graduates.csv lets_script/examples/college_leave.csv lets_script/examples/vpn_list.csv lets_script/examples/vpn_accounts_to_expire_v2.csv