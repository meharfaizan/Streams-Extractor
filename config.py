#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5442493323:AAHGeguKxL1ZjBzbk8AtDa2hSpk-d77hcK8")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "6534707"))
    API_HASH = os.environ.get("API_HASH", "4bcc61d959a9f403b2f20149cbbe627a")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1430593323").split())
    
