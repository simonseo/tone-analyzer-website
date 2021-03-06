#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: form.py
# @Created:   2018-11-27 11:16:48  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-11-27 17:17:26  Simon Seo (simon.seo@nyu.edu)

from wtforms import Form, StringField, TextAreaField, validators

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
	text_data = TextAreaField(
		label='Text Data',
		validators=[
			validators.Optional(),
			validators.Length(max=5000)
			],
		description="Enter any text < 5000 characters"
		)

	def validate(self):
		if not super(EmotionAnalysisForm, self).validate():
			return False
		l = [self.username, self.hashtag, self.text_data]
		cnt = list(map(lambda x: not not x.data, l)).count(True) # count how many are provided
		if cnt is 0:
			msg = "At least one of the three fields must be given"
			self.username.errors.append(msg)
			self.hashtag.errors.append(msg)
			self.text_data.errors.append(msg)
			return False
		if cnt > 1:
			msg = "Please provide only one field"
			for field in l:
				if field.data:
					field.errors.append(msg)
			return False
		return True
