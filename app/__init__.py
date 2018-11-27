#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: __init__.py
# @Created:   2018-11-27 11:02:06  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-11-27 13:18:04  Simon Seo (simon.seo@nyu.edu)
import os
from flask import Flask
from flask_session import Session
from dotenv import load_dotenv
load_dotenv()
SESSION_TYPE = 'filesystem'

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', "Some secret key")
Session(app)

from app import views # set views