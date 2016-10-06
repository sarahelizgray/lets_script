# goal: given a list of graduates, a list of students on college leave,
# and a list of vpn account holders,
# find which vpn accounts should be expired

import csv
import sys


def get_ids_from_file(input_file):
    with open(input_file, 'rb') as f:
        reader = csv.reader(f)
        users = list(reader)
    return users[0]


def get_expire_list(departing_users, vpn_account_ids):
    vpn_accounts_to_expire = []
    for user in departing_users:
        vpn_account_name = "vpn-{}".format(user)
        if vpn_account_name in vpn_account_ids:
            vpn_accounts_to_expire.append(vpn_account_name)
    return vpn_accounts_to_expire


def write_file(output_file, vpn_accounts_to_expire):
    with open(output_file, "wb") as f:
        writer = csv.writer(f)
        writer.writerow(vpn_accounts_to_expire)


if __name__ == "__main__":
    graduates = sys.argv[1]
    college_leave = sys.argv[2]
    vpn_accounts = sys.argv[3]
    output_file = sys.argv[4]

    graduate_user_ids = get_ids_from_file(graduates)
    college_leave_ids = get_ids_from_file(college_leave)
    vpn_account_ids = get_ids_from_file(vpn_accounts)

    vpn_accounts_to_expire = get_expire_list(
        graduate_user_ids + college_leave_ids, vpn_account_ids)
    write_file(output_file, vpn_accounts_to_expire)
