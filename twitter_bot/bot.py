import tweepy
import time

consumer_key = '0I9EiuaYWNOA6pa4TkkupYjTh'
consumer_secret = 'XGMweUbF3bxH4MrlSCibhatFw4XeppAwQMRMZFbCwdpGE3ftwd'

key = '336616983-n8URBjuJ7Z7tZihheUgisYXw8moeUP7kg2QhAzHA'
secret = 'HZjLsz3EbWYefXFwZV233YYcTjiySQU9aTeplW0djn1Cf'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)



FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():

    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if 'manoj' in tweet.full_text.lower():
            print(f"Replied to: {tweet.id}")
            api.update_status("@" + tweet.user.screen_name + "Hi! My name is Mrunal and not Manoj.", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)


while True:
    reply()
    time.sleep(10000)








# id = read_last_seen(FILE_NAME)
# print(id)

#     if 'live' in tweet.text.lower():
#         print("New tweet found!")
