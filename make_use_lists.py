from faker import Faker
import random

fake = Faker()

ALL_ACCOUNTS  = 1000
STUDENT_COUNT = 500
GRADUATE_COUNT = 350
COLLEGE_LEAVE_COUNT = 50
DEANS_LEAVE_COUNT = 100

def make_user_ids(count):
	account_ids = []
	for i in range(count):
		first =  fake.first_name()
		last = fake.last_name()
		username = (first[0] + last[:7]).lower()
		account_ids.append(username)
	return list(set(account_ids))

# get student accounts set up
all_accounts = make_user_ids(ALL_ACCOUNTS)

college_leave_index = GRADUATE_COUNT + COLLEGE_LEAVE_COUNT
deans_leave_index = college_leave_index + DEANS_LEAVE_COUNT

graduates = all_accounts[:GRADUATE_COUNT]
college_leave = all_accounts[GRADUATE_COUNT:college_leave_index]
deans_leave = all_accounts[college_leave_index: deans_leave_index]
noise = all_accounts[deans_leave_index:]	

#make a subset of those students as vpn account holders
graduates_vpn_count = int(GRADUATE_COUNT * .3)
college_leave_vpn_count = int(COLLEGE_LEAVE_COUNT * .1)
deans_leave_vpn_count = int(DEANS_LEAVE_COUNT * .5)

graduates_with_vpn = random.sample(graduates, graduates_vpn_count)
college_leave_with_vpn = random.sample(college_leave, college_leave_vpn_count)
deans_leave_with_vpn = random.sample(deans_leave, deans_leave_vpn_count)

#make the vpn list
vpn_list = list(graduates_with_vpn + college_leave_with_vpn + deans_leave_with_vpn + noise)
vpn_list = [ "vpn-" + username for username in vpn_list]
print vpn_list


	

