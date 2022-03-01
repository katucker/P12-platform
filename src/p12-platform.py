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

@app.route('/get_stats', methods=['POST'])
def get_stats():
	data = request.form
	age = int(data.get('age'))
	grade = data.get('grade')
	raceth = int(data.get('race_ethnicity'))
	return f'Age {age}<br>Grade {grade}<br>Race/Ethnicity {raceth}<br>'
	
if __name__ == "__main__":
	port = os.getenv('PORT', '5001')
	app.run(host='0.0.0.0', port=int(port))
