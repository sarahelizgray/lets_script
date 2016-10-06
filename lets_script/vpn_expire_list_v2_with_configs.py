# goal: given a list of graduates, a list of students on college leave,
# a subset of students on deans leave,
# and a list of vpn account holders,
# find which vpn accounts should be expired

import csv
import sys
import pandas as pd
import ConfigParser


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


def get_eligible_deans_leave_ids(deans_leave_df, year):
    oldies = deans_leave_df[deans_leave_df['year'] <= int(year)]
    return oldies['name'].tolist()

if __name__ == "__main__":
    Config = ConfigParser.ConfigParser()
    Config.read(sys.argv[1])

    vpn_account_ids = get_ids_from_file(Config.get('VPN Accounts', 'path'))

    all_eligible_ids = []
    all_eligible_ids += get_ids_from_file(Config.get('Graduates', 'path'))
    all_eligible_ids += get_ids_from_file(Config.get('College Leave', 'path'))

    deans_leave_df = pd.read_csv(Config.get('Deans Leave', 'path'))
    deans_leave_ids = get_eligible_deans_leave_ids(deans_leave_df, Config.get('Deans Leave', 'expiration_year'))
    all_eligible_ids += deans_leave_ids

    vpn_accounts_to_expire = get_expire_list(all_eligible_ids, vpn_account_ids)
    write_file(Config.get('General', 'output_path'), vpn_accounts_to_expire)