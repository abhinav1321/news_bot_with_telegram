# news_bot_with_telegram

This bot is created as an API example to read news on users demand.

It uses two APIs consucitively:
    1. Telegram Bot API - for messaging
    2. newsapi.org API - to get the relevant news

Language used: Python 3.8.2

Libraries used: json, requests, time

Consist of 3 files:
 1. main.py - main file which runs the code, contains Telegram Bot API requests, News Requests are passed to functions from newsfile
 2. news_file.py - Contains Newsapi.org API requests, Returns news to main file
 3. keys.py - contains API keys for both APIs.


