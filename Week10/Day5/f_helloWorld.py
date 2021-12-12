# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 10:11:18 2021

@author: 97250
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"