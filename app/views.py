#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: views.py
# @Created:   2018-11-27 10:59:29  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-11-27 15:49:35  Simon Seo (simon.seo@nyu.edu)
import os, logging
logger = logging.getLogger(__name__)

# Flask and other private libs
from flask import request, render_template, redirect, url_for, flash, session
from pprint import pprint

# Custom
from app.api.azure import AzureCognitiveAPI
from app.api.twitter import TwitterAPI
from app import app
from app.form import EmotionAnalysisForm
from app.helpers import map_score_to_emotion

azure_api = AzureCognitiveAPI()
twitter_api = TwitterAPI()


@app.route('/analyze', methods=['GET', 'POST'])
def route_analyze_emotion():
	form = EmotionAnalysisForm(request.form) # is request.form required here? 
	if request.method == 'POST' and form.validate():
		if form.username.data:
			input_field = "username"
			keyword = form.username.data.replace('@', '')
			documents, response = twitter_api.get_tweets_by_username(keyword, 20)
			documents = ' '.join(documents)
			data = response
			emotion_scores, errors = azure_api.analyze_emotion([documents], ['en'])
		elif form.hashtag.data:
			input_field = "hashtag"
			keyword = form.hashtag.data.replace('#', '')
			documents, response = twitter_api.get_tweets_by_hashtag(keyword, 20)
			documents = ' '.join(documents)
			data = response
			emotion_scores, errors = azure_api.analyze_emotion([documents], ['en'])
		elif form.text_data.data:
			input_field = "text_data"
			keyword = None
			data = form.text_data.data
			emotion_scores, errors = azure_api.analyze_emotion([form.text_data.data], ['en'])
		session['results'] = {
			'input_field' : input_field,
			'keyword' : keyword,
			'data' : data,
			'score' : round(emotion_scores[0], 3)
		}
		flash("Thanks for submitting. Received username:'{}', hashtag:'{}', text:'{}'".format(form.username.data, form.hashtag.data, form.text_data.data))
		return redirect(url_for('route_analysis_results'))
	else:
		return render_template('analyze.html', title='How are you feeling today?', form=form)

@app.route('/results', methods=['GET'])
def route_analysis_results():
	score = session.get('results').get('score')
	return render_template('results.html', 
		title="I'm feeling {}".format(map_score_to_emotion(score)), 
		results=session.get('results', None),
		urls=[url_for('route_analyze_emotion')])

@app.route('/', methods=['GET'])
def route_home():
	return redirect(url_for('route_analyze_emotion'))


