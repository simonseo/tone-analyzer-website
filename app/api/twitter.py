#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: twitter.py
# @Created:   2018-11-27 09:42:10  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-11-27 15:30:18  Simon Seo (simon.seo@nyu.edu)

import os
import requests
from requests_oauthlib import OAuth1
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()

class TwitterAPI():
	"""API to simplify using Twitter API. Requires Tokens and secrets"""
	def __init__(self):
		ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', False)
		ACCESS_SECRET = os.environ.get('ACCESS_SECRET', False)
		CONSUMER_KEY = os.environ.get('CONSUMER_KEY', False)
		CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET', False)
		assert CONSUMER_KEY and CONSUMER_SECRET and ACCESS_TOKEN and ACCESS_SECRET
		self.auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

		self.twitter_base_url = "https://api.twitter.com/1.1/"
		self.tweet_hashtag_url = "{}{}?q={}&count={}&tweet_mode=extended".format(self.twitter_base_url, "search/tweets.json", '{}', '{}')
		self.tweet_user_url = "{}{}?screen_name={}&count={}&tweet_mode=extended".format(self.twitter_base_url, "statuses/user_timeline.json", '{}', '{}')
		# Check API status
	def get_tweets_by_hashtag(self, hashtag, count=200):
		assert '#' not in hashtag and '%23' not in hashtag, "Remove # before passing to get_by_hashtag please"
		hashtag = '%23' + hashtag
		tweet_hashtag_url = self.tweet_hashtag_url.format(hashtag, count)

		response = requests.get(tweet_hashtag_url, auth=self.auth).json()
		return [status['full_text'] for status in response['statuses']], response

	def get_tweets_by_username(self, username, count=200):
		assert '@' not in username and '%40' not in username, "Remove @ before passing username to get_tweets_by_username please"
		tweet_user_url = self.tweet_user_url.format(username, count)

		response = requests.get(tweet_user_url, auth=self.auth).json()
		return [status['full_text'] for status in response], response

if __name__ == '__main__':
	api = TwitterAPI()
	print(api.get_tweets_by_hashtag('uae', 1))
	print(api.get_tweets_by_username('elonmusk', 1))










