# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 20:14:17 2021

@author: 97250
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5050, debug=True)