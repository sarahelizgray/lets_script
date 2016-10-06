# goal: given a list of graduates and a list of vpn account holders,
# find which vpn accounts should be expired

import csv

GRADUATES = "lets_script/examples/graduates.csv"
VPN_ACCOUNTS = "lets_script/examples/vpn_list.csv"
OUTPUT_FILE = "lets_script/examples/vpn_accounts_to_expire_v1_refined.csv"


def get_ids_from_file(input_file):
    with open(input_file, 'rb') as f:
        reader = csv.reader(f)
        users = list(reader)
    return users[0]

graduate_user_ids = get_ids_from_file(GRADUATES)
vpn_account_ids = get_ids_from_file(VPN_ACCOUNTS)

vpn_accounts_to_expire = []
for graduate in graduate_user_ids:
    vpn_account_name = "vpn-{}".format(graduate)
    if vpn_account_name in vpn_account_ids:
        vpn_accounts_to_expire.append(vpn_account_name)

with open(OUTPUT_FILE, "wb") as f:
    writer = csv.writer(f)
    writer.writerow(vpn_accounts_to_expire)
