import tweepy
import time

# Twitter API credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open text file containing tweets
with open("tweets.txt", "r") as f:
    tweets = f.readlines()

# Keep track of tweets that have been shared
shared_tweets = set()

while len(shared_tweets) < len(tweets):
    for tweet in tweets:
        if tweet in shared_tweets:
            continue
        try:
            # Share tweet
            api.update_status(tweet)
            shared_tweets.add(tweet)
            print("Tweet shared: ", tweet)
            # Wait for 3 minutes
            time.sleep(180)
        except tweepy.TweepError as e:
            print("Error: ", e)
print("All tweets have been shared.")
