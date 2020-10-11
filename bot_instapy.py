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

session1 = InstaPy(username="maichaelrich001@yahoo.com", password="michael.richimon1")
session1.login()

session2 = InstaPy(username="maichaelrich002@yahoo.com", password="michael.richimon1")
session2.login()

while True:
    start = time.time()
    session1.follow_user_followers(username, amount = 15, sleep_delay=1)
    print("{} seconds".format(time.time() - start))

    start = time.time()
    session2.follow_user_followers(username, amount= 15, sleep_delay=1)
    print("{} seconds".format(time.time() - start))