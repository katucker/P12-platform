# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 12:13:47 2022

@author: ktucker
"""
import os
import time
from flask import Flask, render_template, redirect, request
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).parent

def template_modified(template):
	filepath = BASE_DIR.joinpath('templates',template)
	mtime = time.localtime(filepath.stat().st_mtime) 
	return time.strftime('%B %d, %Y', mtime)
	
@app.route('/')
def show_alternatives():
    return render_template('index.html', mtime=template_modified('index.html'))
    
@app.route('/show-tell')
def show_and_tell():
	return render_template('show-tell.html', mtime=template_modified('show-tell.html'))

@app.route('/helpachild')
def helpachild():
	return render_template('helpachild.html', mtime=template_modified('helpachild.html'))

@app.route('/p12equity')
def p12equity():
	return render_template('p12equity.html', mtime=template_modified('p12equity.html'))

@app.route('/get_stats', methods=['POST'])
def get_stats():
	return render_template('childviz.html', mtime=template_modified('childviz.html'), age=request.form.get('age'), grade=request.form.get('grade'),race=request.form.get('race'),hispanic=request.form.get('hispanic'),disability=request.form.get('disability'),economic=request.form.get('economic'),homeless=request.form.get('homeless'))
	

@app.route('/get_area_stats', methods=['POST'])
def get_area_stats():
	return f"Metrics for area {request.form.get('location')}"
	
@app.route('/get_equity_stats', methods=['POST'])
def get_equity_stats():
	return f"Equity metrics for area {request.form.get('location')}"
	
if __name__ == "__main__":
	
	port = os.getenv('PORT', '5001')
	app.run(host='0.0.0.0', port=int(port))
