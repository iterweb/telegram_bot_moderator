# Async Telegram Bot Moderator
This is a simple realization of an asynchronous telegram bot moderator.
## Bot Functions
- deleting duplicate messages
- deleting abusive messages
- deleting messages with external urls
- muting users

## Requirements
```pip install -r requirements.txt```

## Usage
- create a bot in ```@BotFather``` then run the command in BotFather's menu ```/setprivacy``` and set up current status in: **Disable**
- add the bot to your group and set administrator rights for it
- add received bot's token in ```config.py``` and fill other fields

## Mute Users
First you need to get the user ID
- run ```!info <full name>```<br>
Example: ```!info John Doe```<br>
You will receive a message from the bot with user data, something like this ```[('1234567', 'John Doe', '2021-08-25 23:02:37')]```
- for mute user, run ```!mute <id>```<br>
Example: ```!mute 1234567```
## Start
```python bot.py```
## Donate
If you want, you can [support](https://destream.net/live/iterweb/donate) me!
