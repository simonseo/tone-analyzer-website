#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: views.py
# @Created:   2018-11-27 10:59:29  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-11-27 11:50:42  Simon Seo (simon.seo@nyu.edu)
import os, logging
logger = logging.getLogger(__name__)

# Flask and other private libs
from flask import request, render_template, redirect, url_for, flash
from pprint import pprint

# Custom
from app.api.azure import AzureCognitiveAPI
from app import app
from app.form import EmotionAnalysisForm

api = AzureCognitiveAPI()
documents = [
	'I had a wonderful experience! The rooms were wonderful and the staff was helpful.',
	'I had a terrible time at the hotel. The staff was rude and the food was awful.',
	'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.',
	'La carretera estaba atascada. Había mucho tráfico el día de ayer.'
	]
pprint(api.analyze_emotion(documents))

@app.route('/analyze', methods=['GET', 'POST'])
def page_analyze_emotion():
    form = EmotionAnalysisForm(request.form) # is request.form required here? 
    if request.method == 'POST' and form.validate():
        if form.username.data:
        	pass
       	if form.hashtag.data:
       		pass
       	if form.text_data.data:
       		pass
        flash("Thanks for submitting. Received username:'{}', hashtag:'{}', text:'{}'".format(form.username.data, form.hashtag.data, form.text_data.data))
        return redirect(url_for('page_analyze_emotion'))
    else:
	    return render_template('analyze.html', title='How are you feeling today?', form=form)


