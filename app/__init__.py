#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: __init__.py
# @Created:   2018-11-27 11:02:06  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-11-27 11:12:36  Simon Seo (simon.seo@nyu.edu)

from flask import Flask

app = Flask(__name__)

from app import views # set views
