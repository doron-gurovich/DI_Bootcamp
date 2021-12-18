# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 20:14:17 2021

@author: 97250
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)