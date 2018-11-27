#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: helpers.py
# @Created:   2018-11-27 14:45:42  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-11-27 16:47:26  Simon Seo (simon.seo@nyu.edu)

def map_score_to_emotion(score):
	assert 0 <= score <= 1, "Expected score to be between 0 and 1, received score={}".format(score)
	if score > 0.8:
		return "very happy!! :)"
	elif score > 0.5:
		return "happy!"
	elif score > 0.3:
		return "okay"
	elif score > 0.1:
		return "kinda bad"
	else:
		return "sad :'("