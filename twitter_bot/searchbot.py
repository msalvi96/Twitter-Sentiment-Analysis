import tweepy
import time

consumer_key = '0I9EiuaYWNOA6pa4TkkupYjTh'
consumer_secret = 'XGMweUbF3bxH4MrlSCibhatFw4XeppAwQMRMZFbCwdpGE3ftwd'

key = '336616983-n8URBjuJ7Z7tZihheUgisYXw8moeUP7kg2QhAzHA'
secret = 'HZjLsz3EbWYefXFwZV233YYcTjiySQU9aTeplW0djn1Cf'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag = "100daysofcode"
tweetNumber = 3

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def search_bot():

    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweeted...")
            time.sleep(10000)

        except tweepy.TweepError as e:
            print(e.reason)

search_bot()