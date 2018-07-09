from flask import render_template, request
from portfolio import app
	
@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/contact', methods=['POST'])
def contact():
	req_data = request.form
	name = req_data['name']
	email = req_data['email']
	phone = req_data['phone']
	message = req_data['message']
	#add email sending logic