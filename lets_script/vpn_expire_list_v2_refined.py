# goal: given a list of graduates, a list of students on college leave, 
# and a list of vpn account holders,
# find which vpn accounts should be expired

import csv
import argparse

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


def write_file(output_file, vpn_accounts_to_expire):
	with open(output_file, "wb") as f:
	    writer = csv.writer(f)
	    writer.writerow(vpn_accounts_to_expire)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='get list of vpn accounts to expire')
	parser.add_argument('--graduates', required=True, type=str, help='path to csv of graduate user ids')
	parser.add_argument('--college_leave', required=True, type=str, help='path to csv of college leave user ids')
	parser.add_argument('--vpn_accounts', required=True, type=str, help='path to csv of vpn user ids')
	parser.add_argument('--output_file', required=True, type=str, help='name of outputfile')

	args = parser.parse_args()

	graduate_user_ids = get_ids_from_file(args.graduates)
	college_leave_ids = get_ids_from_file(args.college_leave)
	vpn_account_ids = get_ids_from_file(args.vpn_accounts)

	vpn_accounts_to_expire = get_expire_list(graduate_user_ids + college_leave_ids, vpn_account_ids)
	write_file(args.output_file, vpn_accounts_to_expire)
