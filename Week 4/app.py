# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 14:14:52 2023

@author: cdbry
"""

from flask import Flask

app = Flask(__name__)

@app.route('/') #http://www.google.com/

def home():
    return "Hello World"

app.run(port = 5000)



