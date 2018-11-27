#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: twitter_demo.py
# @Created:   2018-11-27 09:42:10  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-11-27 14:21:58  Simon Seo (simon.seo@nyu.edu)

import os
import requests
from requests_oauthlib import OAuth1
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', False)
ACCESS_SECRET = os.environ.get('ACCESS_SECRET', False)
CONSUMER_KEY = os.environ.get('CONSUMER_KEY', False)
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET', False)
assert CONSUMER_KEY and CONSUMER_SECRET and ACCESS_TOKEN and ACCESS_SECRET
auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

twitter_base_url = "https://api.twitter.com/1.1/"

q = '%23PwC'
if q:
	tweet_hashtag_url = "{}{}?q={}&count={}&tweet_mode=extended".format(twitter_base_url, "search/tweets.json", q, 10)
	print(tweet_hashtag_url)
	response = requests.get(tweet_hashtag_url, auth=auth).json()
	# pprint(response)
print([status['full_text'] for status in response['statuses']])


# This one works!
username = ""
# username = "elonmusk"
if username:
	tweet_user_url = "{}{}?screen_name={}&count={}&tweet_mode=extended".format(twitter_base_url, "statuses/user_timeline.json", username, 5)
	response = requests.get(tweet_user_url, auth=auth).json()
	pprint(response)












