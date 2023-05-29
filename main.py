import tweepy
import numpy as np
import game as g
import controller as c
import time

consumer_key = "YOUR-CONSUMER-KEY"
consumer_secret = "YOUR-CONSUMER-SECRET"
access_token = "YOUR-ACCESS-TOKEN"
access_token_secret = "YOUR-TOKEN-SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

game1 = g.c4Game(7, 6)

game1.createBoard()
game1.readBoard()
game1.drawBoard()
game1.tweetBoard()

usedTweets = []


def getReplies():

    replies = api.mentions_timeline()

    if len(replies) > 0:
        if replies[0].id not in usedTweets:
            reply = replies[0]
            response = reply.text.lower()
            choiceColor = (response.split(" ")[1])
            choiceColumn = (response.split(" ")[2])
            print(choiceColor + "\n" + choiceColumn)
            usedTweets.append(reply.id)
            game1.placePiece(int(choiceColumn), choiceColor)
            game1.winDetection()
            game1.drawBoard()
            game1.tweetBoard()


repliesOld = api.mentions_timeline()
for reply in repliesOld:
    usedTweets.append(reply.id)


while True:

    getReplies()
    time.sleep(5)
