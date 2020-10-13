from instapy import InstaPy
import time
import sys

if len(sys.argv[1:-1]) == 0:
    print("need to input all usernames that is to be targeted on")
    sys.exit(0)

username = sys.argv[1:-1]

try:
    followCount = int(sys.argv[-1])
except ValueError:
    print("the last input of the command line should be a valid integer")
    sys.exit(0)

userFile = open("username.txt", "r", encoding='utf-8')
userPass = {}
for line in userFile.readlines():
    tabs = line.strip().split()
    if len(tabs) < 2 :
        continue

    userPass[tabs[0]] = tabs[1]

sessions = []

for user in userPass:
    sess = InstaPy(username = user, password = userPass[user])
    sess.login()
    sessions.append(sess)

while True:
    for sess in sessions:
        start = time.time()
        sess.follow_user_followers(username, amount = followCount, sleep_delay = 1)
        print("Elapsed Time : {} seconds".format(time.time() - start))
