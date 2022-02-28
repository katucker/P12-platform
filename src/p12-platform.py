# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 12:13:47 2022

@author: ktucker
"""
import os
from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def show_alternatives():
    return render_template('index.html')
    
@app.route('/show-tell')
def show_and_tell():
	return render_template('show-tell.html')

@app.route('/helpachild')
def helpachild():
	return render_template('helpachild.html')

@app.route('/p12equity')
def p12equity():
	return render_template('p12equity.html')


if __name__ == "__main__":
	port = os.getenv('PORT', '5001')
	app.run(host='0.0.0.0', port=int(port))
