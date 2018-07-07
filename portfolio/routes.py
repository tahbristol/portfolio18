from flask import render_template
from portfolio import app

@app.route('/')
def home():
	return render_template('home.html')
	
@app.route('/index')
def index():
	return render_template('index.html')