import tweepy
import numpy as np
import game as g
import time
import main

consumer_key = "YOUR-CONSUMER-KEY"
consumer_secret = "YOUR-CONSUMER-SECRET"
access_token = "YOUR-ACCESS-TOKEN"
access_token_secret = "YOUR-TOKEN-SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

usedTweets = []

while True:
    time.sleep(3)
    replies = api.mentions_timeline()
    if replies[0].id not in usedTweets:
        if "start game" in replies[0].text:
            exec(open('main.py').read())

repliesOld = api.mentions_timeline()
for reply in repliesOld:
    usedTweets.append(reply.id)
