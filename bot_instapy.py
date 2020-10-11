from instapy import InstaPy
import time

session1 = InstaPy(username="maichaelrich001@yahoo.com", password="michael.richimon1")
session1.login()

session2 = InstaPy(username="maichaelrich002@yahoo.com", password="michael.richimon1")
session2.login()

for i in range(2):
    start = time.time()
    session1.follow_user_followers(['najwashihab'], amount = 15, sleep_delay=1)
    print("{} seconds".format(time.time() - start))

    start = time.time()
    session2.follow_user_followers(['najwashihab'], amount= 15, sleep_delay=1)
    print("{} seconds".format(time.time() - start))