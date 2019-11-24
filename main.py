from flask import Flask, render_template, session
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'KEY'


class LoginForm(FlaskForm):
	username = StringField('Nombre de usuario', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	fields = SelectMultipleField('fields', choices=['1', '2', '3'])
	submit = SubmitField('Log In')


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/login')
def login():
	login_form = LoginForm()

	context = {
		'login_form': login_form,
	}

	return render_template('login.html', **context)


@app.route('/appointment')
def schedule():
	return render_template('schedule.html')


@app.route('/device-status')
def status():
	return render_template('status.html')
