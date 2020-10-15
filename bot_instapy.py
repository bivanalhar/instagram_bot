from instapy import InstaPy
import time
import sys

if len(sys.argv) != 4:
    print("need to include file of targeted users, file of usernames we would like to handle and number of followers")
    sys.exit(0)

try:
    followCount = int(sys.argv[3])
except ValueError:
    print("the last input is the number of followers, and thus should be a valid integer")
    sys.exit(0)

userFile = open(sys.argv[1], "r", encoding='utf-8')
targetFile = open(sys.argv[2], "r", encoding='utf-8')

userPass = {}
for line in userFile.readlines():
    tabs = line.strip().split()
    if len(tabs) < 2 :
        continue

    userPass[tabs[0]] = tabs[1]

if len(userPass) == 0:
    print("list of username and password are empty. Please check again")
    sys.exit(0)

username = []
for line in targetFile.readlines():
    users = line.strip().split()
    if len(users) > 1:
        continue

    username.append(users[0])

if len(username) == 0:
    print("list of targeted users are empty. Please check again")
    sys.exit(0)

sessions = []

for user in userPass:
    sess = InstaPy(username = user, password = userPass[user])
    sess.login()
    sessions.append(sess)

while True:
    for sess in sessions:
        start = time.time()
        sess.follow_user_followers(username, amount = followCount, sleep_delay = 1, randomize = False)
        print("Elapsed Time : {} seconds".format(time.time() - start))
