# goal: given a list of graduates and a list of vpn account holders,
# find which vpn accounts should be expired

import csv

def get_ids_from_file(input_file):
	with open(input_file, 'rb') as f:
	    reader = csv.reader(f)
	    users = list(reader)
	return users[0]


def get_expire_list(departing_users, vpn_account_ids):
	vpn_accounts_to_expire = []
	for user in departing_users:
		vpn_account_name = "vpn-{}".format(user)
		if  vpn_account_name in vpn_account_ids:
			vpn_accounts_to_expire.append(vpn_account_name)
	return vpn_accounts_to_expire

graduate_user_ids = get_ids_from_file("lets_script/examples/graduates.csv")
vpn_account_ids = get_ids_from_file("lets_script/examples/vpn_list.csv")
vpn_accounts_to_expire = get_expire_list(graduate_user_ids, vpn_account_ids)

with open("lets_script/examples/vpn_accounts_to_expire_v1_refined.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(vpn_accounts_to_expire)
