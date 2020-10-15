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

Before running the code, you need to make sure that the file named ```username.txt``` exists within the same folder as ```bot_instapy.py```. The format of each line inside ```username.txt``` should be like the following (each username and its respective password is separated by one space)

```
<username1> <password1>
<username2> <password2>
...
```

After that, we may simply run the following code

```
python3 bot_instapy.py <filename of usernames> <filename of target users> <number of followers>
```

By default, the filename for usernames is ```username.txt``` and the filename for target users is ```target.txt```

Here, note that those 2 fields **need to be filled in**, or otherwise you will encounter an error that will result in the early termination of this program. Several things to be noted on are the followings:
1. There should be **at least** 1 username that is to be followed
2. The number of accounts to follow **should be an integer**

For now, the default of the valid command line should be the following:
```
python3 bot_instapy.py username.txt target.txt 100
```

Several mistakes that may occur are the following:
1. In the following case, user did not input the usernames to be targeted on
```
python3 bot_instapy.py 20
need to include file of targeted users, file of usernames we would like to handle and number of followers
```

2. In the following case, the number of accounts to follow is not a valid integer
```
python3 bot_instapy.py qabdjwqbdioq uwjwq782nb
the last input is the number of followers, and thus should be a valid integer
```
