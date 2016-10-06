# goal: given a list of graduates and a list of vpn account holders,
# find which vpn accounts should be expired

import csv

GRADUATES = "examples/graduates.csv"
VPN_ACCOUNTS = "examples/vpn_list.csv"
OUTPUT_FILE = "examples/vpn_accounts_to_expire_v1_tested.csv"

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

if __name__ == "__main__":
	graduate_user_ids = get_ids_from_file(GRADUATES)
	vpn_account_ids = get_ids_from_file(VPN_ACCOUNTS)
	vpn_accounts_to_expire = get_expire_list(graduate_user_ids, vpn_account_ids)

	with open(OUTPUT_FILE, "wb") as f:
	    writer = csv.writer(f)
	    writer.writerow(vpn_accounts_to_expire)
