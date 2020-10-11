# Building Instagram Bot for Auto-Following

To clone this git, simply run the following command on your terminal
```
git clone https://github.com/bivanalhar/instagram_bot.git
```

This file will contain a guideline on how to operate the code successfully. First of all, note that you need to install all the necessary libraries enlisted inside the file named ```requirements.txt```. The method on doing that is very simple, which is to run the following command line into your terminal

```
pip3 install -r requirements.txt
```

Afterwards, the code implicitly uses a library named ```Selenium```, which requires Firefox as a browser in which the code will operate. Make sure to have Firefox installed in your computer (I forgot precisely the minimum version required for this Firefox, therefore just try to install the newest version of it. Or, you may just simply update your existing Firefox into the newest one).

After that, we may simply run the following code

```
python3 bot_instapy.py <list of all targeted usernames> <number of accounts to follow>
```

Here, note that those 2 fields **need to be filled in**, or otherwise you will encounter an error that will result in the early termination of this program. Several things to be noted on are the followings:
1. There should be **at least** 1 username that is to be followed
2. The number of accounts to follow **should be an integer**

For example, suppose that you want to target an account with username ```gantengbanget``` and you would like to fetch 10 of its followers. Therefore, you need to input the following command
```
python3 bot_instapy.py gantengbanget 10
```

Several mistakes that may occur are the following:
1. In the following case, user did not input the usernames to be targeted on
```
python3 bot_instapy.py 20
need to input all usernames that is to be targeted on
```

2. In the following case, the number of accounts to follow is not a valid integer
```
python3 bot_instapy.py qabdjwqbdioq uwjwq782nb
the last input of the command line should be a valid integer
```
