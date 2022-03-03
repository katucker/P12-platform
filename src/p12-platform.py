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
	return f"Age {request.form.get('age')}<br>Grade {request.form.get('grade')}<br>Race {request.form.get('race')}<br>Hispanic/Latino {request.form.get('hispanic')}<br>Disability {request.form.get('disability')}<br>Economically Disadvantaged {request.form.get('economic')}<br>Experiencing Homelessness {request.form.get('homeless')}"
	

@app.route('/get_area_stats', methods=['POST'])
def get_area_stats():
	return f"Metrics for area {request.form.get('location')}"
	
@app.route('/get_equity_stats', methods=['POST'])
def get_equity_stats():
	return f"Equity metrics for area {request.form.get('location')}"
	
if __name__ == "__main__":
	
	port = os.getenv('PORT', '5001')
	app.run(host='0.0.0.0', port=int(port))
