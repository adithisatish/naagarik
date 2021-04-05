import pandas as pd 
import numpy as np
from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream 
import json
import pandas as pd
import preprocessor as preprocess
from framework import civic_framework

# Access Credentials from Twitter
access_token = 'add-access-token'
access_token_secret = 'add-access-token-secret'

consumer_key = 'add-consumer-key'
consumer_key_secret = 'add-consumer-key-secret'

tweets_data = []

def get_tweet(line):
    try:  
        tweet = json.loads(line)  
        tweets_data.append(tweet)  
    except:  
        print("Unable to convert")

class StdOutListener(StreamListener):
      
    def on_data(self, data):
        global tweet_count
        global n_tweets
        global stream 
        
        # tweets_data = []
        if tweet_count < n_tweets:   
            get_tweet(data)
            tweet_count+=1
            return True
        else:
            stream.disconnect()
    
    def on_error(self, status):
        print(status)
    
def clean_tweets(text):
    text = preprocess.clean(text)
    return text

def convert_to_df():
    tweets = pd.DataFrame()
    tweets['description'] = list(map(lambda tweet: tweet['text'], tweets_data))
    tweets['username'] = list(map(lambda tweet: tweet['user']['screen_name'], tweets_data))
    tweets['timestamp'] = list(map(lambda tweet: tweet['created_at'], tweets_data))
    # filename = 'streaming_tweets.json'
    # tweets.to_json(filename)
    return tweets
    # tweets.head()

# stream(0,10)

tweet_count = 0
n_tweets = int(input("Enter number of tweets to scrape: "))

l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(locations=[77.148514,12.733452,78.015747,13.141672])

tweets = convert_to_df()
tweets['description'] = tweets['description'].apply(clean_tweets)

# print(tweets.head())

civic_framework(tweets)