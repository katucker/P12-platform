# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 12:13:47 2022

@author: ktucker
"""
import os
import re
import time
from flask import Flask, render_template, redirect, request
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).parent

def template_modified(template):
	filepath = BASE_DIR.joinpath('templates',template)
	mtime = time.localtime(filepath.stat().st_mtime) 
	return time.strftime('%B %d, %Y', mtime)
	
def render_mtime_template(template, **kwargs):
	return render_template(template, mtime=template_modified(template), **kwargs)
	
@app.route('/')
def show_alternatives():
    return render_mtime_template('index.html')
    
@app.route('/show-tell')
def show_and_tell():
	return render_mtime_template('show-tell.html')

@app.route('/helpachild')
def helpachild():
	return render_mtime_template('helpachild.html')

@app.route('/p12equity')
def p12equity():
	return render_mtime_template('p12equity.html')

@app.route('/get_stats', methods=['POST'])
def get_stats():
	characteristics = f'Age {request.form.get("age")} Grade {request.form.get("grade")}'
	if request.form.get("gender") != "Not selected":
		characteristics += f' Gender {request.form.get("gender")}'
	characteristics += ' Race '
	characteristics += " ".join(re.findall("[A-Z][^A-Z]*", request.form.get("race")))
	if request.form.get("hispanic"):
		characteristics += " of Hispanic origin"
	disability = request.form.get("disability")
	if disability == "01":
		characteristics += " with disability of blindness or visual impairment"
	elif disability == "02":
		characteristics += " with Cerebral Palsy"
	elif disability == "03":
		characteristics += " with chronic illness"
	elif disability == "04":
		characteristics += " with disability of deafness or hearing impairment"
	elif disability == "05":
		characteristics += " with drug or alcohol addition issues"
	elif disability == "06":
		characteristics += " with emotional or psychological issues"
	elif disability == "07":
		characteristics += " with Epilepsy or seizure disorder"
	elif disability == "08":
		characteristics += " with an intellectual disability"
	elif disability == "09":
		characteristics += " with an orthopedic impairment"
	elif disability == "10":
		characteristics += " with a specific learning disability"
	elif disability == "11":
		characteristics += " with a speech or language impairment"
	elif disability == "99":
		characteristics += " with another type of impairment"
	if request.form.get("economic"):
		characteristics += " that is economically disadvantaged"
	if request.form.get("homeless"):
		characteristics += " that is experiencing homelessness"
	characteristics += f' and attends school in {request.form.get("location")}'
	return render_mtime_template('childviz.html', characteristics=characteristics)
	

@app.route('/get_area_stats', methods=['POST'])
def get_area_stats():
	return render_mtime_template('showviz.html', location=request.form.get('location'))
	
@app.route('/get_equity_stats', methods=['POST'])
def get_equity_stats():
	return render_mtime_template('equityviz.html', location=request.form.get('location'))
	
if __name__ == "__main__":
	
	port = os.getenv('PORT', '5001')
	app.run(host='0.0.0.0', port=int(port))
