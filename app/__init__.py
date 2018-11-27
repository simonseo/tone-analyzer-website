#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: __init__.py
# @Created:   2018-11-27 11:02:06  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-11-27 11:49:56  Simon Seo (simon.seo@nyu.edu)
import os
from flask import Flask
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', "Some secret key")

from app import views # set views