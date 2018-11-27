#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: azure.py
# @Created:   2018-11-27 09:42:10  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-11-27 15:13:21  Simon Seo (simon.seo@nyu.edu)

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
		headers   = {"Ocp-Apim-Subscription-Key": self.subscription_key}
		response  = requests.post(self.language_api_url, headers=headers, json=payload).json()

		errors = response.get('errors', [])
		if errors:
			logger.info("There was an error while detecting languages: {}".format(errors))
		languages = sorted(response.get('documents', []), key=lambda doc:doc['id']) # sort by id
		iso6391Names = [sorted(lang['detectedLanguages'], key=lambda l: l['score'])[-1]['iso6391Name'] for lang in languages] # get highest ranked language
		return iso6391Names, errors
		
	def analyze_emotion(self, documents, iso6391Names):
		'''Analyze the emotion of each entry in a list of str documents
		sentiment score for a document is between $0$ and $1$, 
		with a higher score indicating a more positive sentiment.'''
		assert type(documents) is list and type(documents[0]) is str, "analyze_emotion requires a list of strings"
		if not iso6391Names:
			iso6391Names, error = self.detect_language([]+documents)
		payload = { 'documents' : [{'id':'{}'.format(i+1), 'language':iso6391Names[i], 'text':text} for i, text in enumerate(documents)] } # this should look like the below dict
		headers   = {"Ocp-Apim-Subscription-Key": self.subscription_key}
		response  = requests.post(self.sentiment_api_url, headers=headers, json=payload).json()

		errors = response.get('errors', [])
		if errors:
			logger.info("There was an error while analyzing emotions: {}".format(errors))
		sentiments = sorted(response.get('documents', []), key=lambda doc:doc['id']) # sort by id
		emotion_scores = [sent['score'] for sent in sentiments] # get scores for each emotion
		print("The documents: {} \n The scores: {} \n".format(documents, emotion_scores))
		return emotion_scores, errors


if __name__ == '__main__':
	api = AzureCognitiveAPI()
	documents = [
		'I had a wonderful experience! The rooms were wonderful and the staff was helpful.',
		'I had a terrible time at the hotel. The staff was rude and the food was awful.',
		'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.',
		'La carretera estaba atascada. Había mucho tráfico el día de ayer.'
		]
	documents = ['RT @HaroldSinnott: 5 stage #automation maturity model &gt; #AI #RPA #IPA #MachineLearning #Software #Robotics #futureofwork &gt; #PwC via @MikeQu…', 'RT @MikeQuindazzi: Ready for an #AI strategy? It’s an intelligent thing to do! &gt;&gt;&gt; @MikeQuindazzi &gt;&gt;&gt; #PwC #ArtificialIntelligence #Machine…', 'RT @PwC_Cy_Press: We are looking for Qualified Accountants (ACA/ACCA) to join our Deals Department - Learn more &amp; apply https://t.co/ACr2PR…', '5 stage #automation maturity model &gt; #AI #RPA #IPA #MachineLearning #Software #Robotics #futureofwork &gt; #PwC via @MikeQuindazzi &gt; Report https://t.co/mTfC1yxwso cc @nigewillson @PaulTDenham @grattongirl @jblefevre60 @akwyz @JGrobicki @gvalan @robrecruitsdata @IOT_Recruiting https://t.co/dIGjAsM9vm', '#PVN likumā top svarīgi grozījumi https://t.co/TqaAVwwCiu #PwC #nodokļi', 'RT @HaroldSinnott: Building #IoT? 8 industry examples of #Human experts using #data to drive more insightful decision-making &gt; #PwC via @Mi…', 'RT @snessim: 3 ways #AI can artificially act like a #human! \n#1 Sense #NLP + #MachineVision \n#2 Think #MachineLearning + #DeepLearning \n#3…', 'Kas mainīsies padziļinātās #sadarbības programmas darbības noteikumos? https://t.co/TqaAVwwCiu #PwC #nodokļi', 'RT @PwC_Middle_East: #PwC’s @ddellea and Felicien Dillard following their discussions at @iSportconnect’s 2018 #DubaiSummit, discussing PwC…', 'RT @HaroldSinnott: Building #IoT? 8 industry examples of #Human experts using #data to drive more insightful decision-making &gt; #PwC via @Mi…']
	lang = api.detect_language(documents)
	pprint(api.analyze_emotion(documents, lang))







