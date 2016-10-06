#!/bin/bash


echo Naive Implementation
rm lets_script/examples/vpn_accounts_to_expire_v1.csv
python lets_script/vpn_expire_list_v1.py

echo Refined Implementation
rm lets_script/examples/vpn_accounts_to_expire_v1_refined.csv
python lets_script/vpn_expire_list_v1_refined.py

echo Tested Implementation
rm lets_script/examples/vpn_accounts_to_expire_v1_tested.csv
python lets_script/vpn_expire_list_v1_tested.py