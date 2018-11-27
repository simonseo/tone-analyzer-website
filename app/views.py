#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: views.py
# @Created:   2018-11-27 10:59:29  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-11-27 11:16:15  Simon Seo (simon.seo@nyu.edu)
import os, logging
logger = logging.getLogger(__name__)

# Flask and other private libs
from flask import request, render_template, redirect, url_for, flash
from pprint import pprint

# Custom
from app.api.azure import AzureCognitiveAPI
from app import app

@app.route('/analyze', methods=['GET', 'POST'])
def page_analyze_emotion():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        #also check that account does not exist already
        password = pwd_context.hash(form.password.data)
        try:
            # hotp_secret = duo.activate(form.qr_url.data)
            hotp_secret = 'a85adc3516351791c05ef40bde772c24'
            DB.insert_user(form.email.data, password, hotp_secret)
        except Exception as e:
            flash("I\'m sorry. Try again later. Let the adminstrator know about the error: {}".format(e))
            return redirect(url_for('register_account'))
        else:
            flash("Thanks for registering. Received {} {}:{}".format(form.email.data, form.password.data, password))
            return redirect(url_for('generate_passcode'))
    return render_template('register.html', title='Register New Account', form=form)


api = AzureCognitiveAPI()
documents = [
	'I had a wonderful experience! The rooms were wonderful and the staff was helpful.',
	'I had a terrible time at the hotel. The staff was rude and the food was awful.',
	'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.',
	'La carretera estaba atascada. Había mucho tráfico el día de ayer.'
	]
pprint(api.analyze_emotion(documents))
