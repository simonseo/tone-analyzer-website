#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: azure.py
# @Created:   2018-11-27 09:42:10  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-11-27 11:14:36  Simon Seo (simon.seo@nyu.edu)

import os
import requests
from pprint import pprint

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from dotenv import load_dotenv
load_dotenv()


class AzureCognitiveAPI():
	"""API to simplify using Azure API. Requires """
	def __init__(self):
		self.subscription_key = os.environ.get('AZURE_TEXT_ANALYTICS_KEY')
		assert self.subscription_key, "Subscription key was not found."
		self.text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
		self.language_api_url = self.text_analytics_base_url + "languages"
		self.sentiment_api_url = self.text_analytics_base_url + "sentiment"

	def detect_language(self, documents):
		'''Detect language of each entry in a list of str documents'''
		assert type(documents) is list and type(documents[0]) is str, "detect_language requires a list of strings"
		payload = { 'documents' : [{'id':'{}'.format(i+1), 'text':text} for i, text in enumerate(documents)] } # this should look like the below dict

		# documents = { 'documents': [
		#     { 'id': '1', 'text': 'This is a document written in English.' },
		#     { 'id': '2', 'text': 'Este es un document escrito en Español.' },
		#     { 'id': '3', 'text': '这是一个用中文写的文件' }
		# ]}
		headers   = {"Ocp-Apim-Subscription-Key": self.subscription_key}
		response  = requests.post(self.language_api_url, headers=headers, json=payload).json()

		errors = response.get('errors', [])
		if errors:
			logger.info("There was an error while detecting languages: {}".format(errors))
		languages = sorted(response.get('documents', []), key=lambda doc:doc['id']) # sort by id
		iso6391Names = [sorted(lang['detectedLanguages'], key=lambda l: l['score'])[-1]['iso6391Name'] for lang in languages] # get highest ranked language
		return iso6391Names
		
	def analyze_emotion(self, documents):
		'''Analyze the emotion of each entry in a list of str documents
		sentiment score for a document is between $0$ and $1$, 
		with a higher score indicating a more positive sentiment.'''
		assert type(documents) is list and type(documents[0]) is str, "analyze_emotion requires a list of strings"
		iso6391Names = self.detect_language(documents)
		payload = { 'documents' : [{'id':'{}'.format(i+1), 'language':iso6391Names[i], 'text':text} for i, text in enumerate(documents)] } # this should look like the below dict

		# documents = {'documents' : [
		#   {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
		#   {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},  
		#   {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},  
		#   {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'}
		# ]}
		headers   = {"Ocp-Apim-Subscription-Key": self.subscription_key}
		response  = requests.post(self.sentiment_api_url, headers=headers, json=payload).json()

		errors = response.get('errors', [])
		if errors:
			logger.info("There was an error while analyzing emotions: {}".format(errors))
		sentiments = sorted(response.get('documents', []), key=lambda doc:doc['id']) # sort by id
		emotion_scores = [sent['score'] for sent in sentiments] # get scores for each emotion
		return emotion_scores


if __name__ == '__main__':
	api = AzureCognitiveAPI()
	documents = [
		'I had a wonderful experience! The rooms were wonderful and the staff was helpful.',
		'I had a terrible time at the hotel. The staff was rude and the food was awful.',
		'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.',
		'La carretera estaba atascada. Había mucho tráfico el día de ayer.'
		]
	pprint(api.analyze_emotion(documents))







