# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 20:14:17 2021

@author: 97250
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/' or '/index.html')
def index():
    return render_template('index.html')

@app.route('/flow_chart.html')
def flow_chart():
    return render_template('flow_chart.html')

@app.route('/procedure.html')
def procedure():
    return render_template('procedure.html')

@app.route('/intro_project.html')
def intro_project():
    return render_template('intro_project.html')

@app.route('/intro_press.html')
def intro_press():
    return render_template('intro_press.html')

@app.route('/about_QDPS.html')
def about_QDPS():
    return render_template('about_QDPS.html')

if __name__ == "__main__":
    app.run(port=5050, debug=True)