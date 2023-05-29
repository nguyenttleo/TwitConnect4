import tweepy
import numpy as np
from itertools import islice

consumer_key = "YOUR-CONSUMER-KEY"
consumer_secret = "YOUR-CONSUMER-SECRET"
access_token = "YOUR-ACCESS-TOKEN"
access_token_secret = "YOUR-TOKEN-SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

f = open("gameboard.txt", "r+", encoding="utf-8")
r = open("newboard.txt", "r", encoding="utf-8")
n = open("newboard.txt", "r", encoding="utf-8")


class c4Game:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.boardList = []
        self.length = []
        for i in range(height):
            self.length.append(8)
        print(self.length)
        self.tweetMessage = ""

    def createBoard(self):
        f = open("gameboard.txt", "w", encoding="utf-8")
        f.write(n.read())
        tally = open("gamenumber.txt", "r", encoding="utf=8")
        gameNumber = int(tally.read())
        gameNumber += 1
        tallyWrite = open("gamenumber.txt", "w", encoding="utf=8")
        tallyWrite.write(str(gameNumber))

    def drawBoard(self):
        z = open("gameboard.txt", "w", encoding="utf-8")
        tally = open("gamenumber.txt", "r", encoding="utf=8")
        gameNumber = tally.read()
        for i in self.boardList:
            for item in i:
                z.write(item)
        z.write(" 0   1   2   3   4   5   6\nGame #" + gameNumber)
        print(self.boardList)

    def tweetBoard(self):
        f = open("gameboard.txt", "r", encoding="utf-8")
        api.update_status(f.read() + '\n' + self.tweetMessage)

    def readBoard(self):
        for i in f.read():
            self.boardList.append(i)
        board = iter(self.boardList)
        self.boardList = [list(islice(board, length))
                          for length in self.length]
        print(self.boardList)

    def placePiece(self, x, color):
        for i in range(len(self.boardList)):
            k = (len(self.boardList)-1)-i
            if self.boardList[k][x] == "🟦":
                if color == "yellow":
                    self.boardList[k][x] = "🟨"
                    break
                elif color == "red":
                    self.boardList[k][x] = "🟥"
                    break
        # print(self.boardList)

    def winDetection(self):
        for list in range(len(self.boardList)):
            for item in range(len(self.boardList[list])):
                if self.boardList[list][item] == "🟥" and self.boardList[list][item+1] == "🟥" and self.boardList[list][item+2] == "🟥" and self.boardList[list][item+3] == "🟥":
                    self.tweetMessage = "Red Wins!"
                    return 1
                elif self.boardList[list][item] == "🟨" and self.boardList[list][item+1] == "🟨" and self.boardList[list][item+2] == "🟨" and self.boardList[list][item+3] == "🟨":
                    self.tweetMessage = "Yellow Wins!"
                    return 1
        for list in range(len(self.boardList)-3):
            for item in range(len(self.boardList[list])):
                if self.boardList[list][item] == "🟥" and self.boardList[list+1][item] == "🟥" and self.boardList[list+2][item] == "🟥" and self.boardList[list+3][item] == "🟥":
                    self.tweetMessage = "Red Wins!"
                    return 1
                if self.boardList[list][item] == "🟨" and self.boardList[list+1][item] == "🟨" and self.boardList[list+2][item] == "🟨" and self.boardList[list+3][item] == "🟨":
                    self.tweetMessage = "Yellow Wins!"
                    return 1
                if self.boardList[list][item] == "🟥" and self.boardList[list+1][item+1] == "🟥" and self.boardList[list+2][item+2] == "🟥" and self.boardList[list+3][item+3] == "🟥":
                    self.tweetMessage = "Red Wins!"
                    return 1
                if self.boardList[list][item] == "🟨" and self.boardList[list+1][item+1] == "🟨" and self.boardList[list+2][item+2] == "🟨" and self.boardList[list+3][item+3] == "🟨":
                    self.tweetMessage = "Yellow Wins!"
                    return 1
                if self.boardList[list][item] == "🟥" and self.boardList[list+1][item-1] == "🟥" and self.boardList[list+2][item-2] == "🟥" and self.boardList[list+3][item-3] == "🟥":
                    self.tweetMessage = "Red Wins!"
                    return 1
                if self.boardList[list][item] == "🟨" and self.boardList[list+1][item-1] == "🟨" and self.boardList[list+2][item-2] == "🟨" and self.boardList[list+3][item-3] == "🟨":
                    self.tweetMessage = "Yellow Wins!"
                    return 1
