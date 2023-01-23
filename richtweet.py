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

# Create an instance of the URL shortener
s = pyshorteners.Shortener()

# Shorten URLs in tweets.txt
for i, tweet in enumerate(tweets):
    url_match = re.search("https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", tweet)
    if url_match:
        original_url = url_match.group(0)
        short_url = s.tinyurl.short(original_url)
        tweets[i] = tweet.replace(original_url, short_url)

while len(shared_tweets) < len(tweets):
    for tweet in tweets:
        if tweet in shared_tweets:
            continue
        try:
            # Share tweet
            api.update_status(tweet)
            shared_tweets.add(tweet)
            print("Tweet shared: ", tweet)
            for i in range(180, 0, -1):
                print("Next tweet in: ", i, " seconds", end='\r')
                time.sleep(1)
        except tweepy.TweepError as e:
            print("Error: ", e)
print("All tweets have been shared.")
