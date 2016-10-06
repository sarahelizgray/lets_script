# goal: given a list of graduates and a list of vpn account holders,
# find which vpn accounts should be expired

import csv

with open('lets_script/examples/vpn_list.csv', 'rb') as f:
    reader = csv.reader(f)
    vpn_accounts = list(reader)

with open('lets_script/examples/graduates.csv', 'rb') as f:
    reader = csv.reader(f)
    graduates = list(reader)

vpn_accounts_to_expire = []
graduate_user_ids = graduates[0]
vpn_account_ids = vpn_accounts[0]

for graduate in graduate_user_ids:
    vpn_account_name = "vpn-{}".format(graduate)
    if vpn_account_name in vpn_account_ids:
        vpn_accounts_to_expire.append(vpn_account_name)

with open("lets_script/examples/vpn_accounts_to_expire_v1.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(vpn_accounts_to_expire)
