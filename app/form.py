#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: form.py
# @Created:   2018-11-27 11:16:48  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-11-27 11:44:54  Simon Seo (simon.seo@nyu.edu)

from wtforms import Form, StringField, validators

class EmotionAnalysisForm(Form):
	username = StringField(
		label='Twitter Username',
		validators=[validators.Optional()],
		description="Enter a Twitter username/handle without the @"
		)
	hashtag = StringField(
		label='Twitter Hashtag',
		validators=[validators.Optional()],
		description="Enter a Twitter Hashtag without the #"
		)
	text_data = StringField(
		label='Text Data',
		validators=[
			validators.Optional(),
			validators.Length(max=3000)
			],
		description="Enter any text < 3000 characters"
		)

	def validate(self):
		if not super(EmotionAnalysisForm, self).validate():
			return False
		if not (self.username.data or self.hashtag.data or self.text_data.data):
			msg = 'At least one of the three fields must be given'
			self.username.errors.append(msg)
			self.hashtag.errors.append(msg)
			self.text_data.errors.append(msg)
			return False
		return True
