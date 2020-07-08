# -*- coding: utf-8 -*-
"""
Author: Tanmay Gupta
Date: July 04, 2019 - 11:06 am
"""

import csv
import json
import tweepy
from pandas import read_csv

def tweets_call(twitter_handle):
    with open('twitter_credentials.json') as cred_data:
        info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_key = info['ACCESS_KEY']
    access_secret = info['ACCESS_SECRET']
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    tweets = []
    
    new_tweets = api.user_timeline(screen_name = twitter_handle, count = 200, tweet_mode = "extended")
    tweets.extend(new_tweets)
    
    oldest_tweet = tweets[-1].id - 1
    
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name = twitter_handle, count = 200, max_id = oldest_tweet, tweet_mode = "extended")
    
        print ('...%s tweets have been downloaded so far' % len(tweets))
        
        tweets.extend(new_tweets)
        oldest_tweet = tweets[-1].id - 1
    
    outtweets = [[tweet.id_str, tweet.created_at, tweet.full_text] for tweet in tweets]
    
    with open('Tweets/' + twitter_handle + '_tweets.csv', 'w', encoding = 'utf8') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'created_at', 'text'])
            writer.writerows(outtweets)
            
def get_tweets(twitter_handle):
    tweet_data = read_csv('Tweets//' + twitter_handle + '_tweets.csv', encoding = 'utf-8')
    tweet_data = tweet_data.dropna()
    return tweet_data
            
            
            