# routes.py - 	Home page route: Use render\_template() function

from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Miguel'}
	return render_template('index.html', title='Home', user=user)