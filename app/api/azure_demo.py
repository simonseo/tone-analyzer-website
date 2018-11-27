#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: azure_demo.py
# @Created:   2018-11-27 09:42:10  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-11-27 10:00:58  Simon Seo (simon.seo@nyu.edu)

import os
import requests
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()

subscription_key = os.environ.get('AZURE_TEXT_ANALYTICS_KEY', False)
assert subscription_key

text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
language_api_url = text_analytics_base_url + "languages"
sentiment_api_url = text_analytics_base_url + "sentiment"
# print(language_api_url)
# print(sentiment_api_url)


# Test Language Detection
documents = { 'documents': [
    { 'id': '1', 'text': 'This is a document written in English.' },
    { 'id': '2', 'text': 'Este es un document escrito en Español.' },
    { 'id': '3', 'text': '这是一个用中文写的文件' }
]}
headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()
pprint(languages)


# Test Sentiment API. sentiment score for a document is between $0$ and $1$, with a higher score indicating a more positive sentiment.
documents = {'documents' : [
  {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
  {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},  
  {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},  
  {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'}
]}
headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(sentiment_api_url, headers=headers, json=documents)
sentiments = response.json()
pprint(sentiments)










