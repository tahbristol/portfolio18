from smtplib import SMTP
from flask import render_template, request
from portfolio import app
	
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/email', methods=['POST'])
def email():
	form = request.form

	if len(form.extra) > 0:
		return

	msg = {}
	msg['To'] = "tahbristol@gmail.com"
	msg['Subject'] = "From tahbristol.com"
	msg['Name'] = form['name']
	msg['From'] = form['email']
	msg['Content'] = form['message']

	content = msg['From'] + "\n" + "Message: " + msg['Content'] + "\n" + "Name: " + msg['Name']
	
	s = SMTP('smtp.gmail.com', 587)
	s.ehlo()
	s.starttls()
	s.login('tahbristol@gmail.com', 'xuxbqluoqupbarro')
	
	s.sendmail('tahbristol@gmail.com', 'tahbristol@gmail.com', content)
	s.close()
	return render_template('index.html')
	
	
