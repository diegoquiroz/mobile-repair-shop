from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'KEY'


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Log In')


class PhoneForm(FlaskForm):
	brand = SelectMultipleField('Brand', choices=[
		('1', 'Apple'),
		('2', 'Huawei'),
		('3', 'Samsung'),
		('4', 'LG'),
		('5', 'Xiaomi'),
		('6', 'Nokia')
	])
	model = SelectMultipleField('Model', choices=[
		('1', 'iPhone 11 Pro'),
		('2', 'iPhone 11 Pro Max'),
		('3', 'iPhone 11'),
		('4', 'iPhone XS'),
		('5', 'iPhone XS Max'),
		('6', 'iPhone XR'),
		('7', 'iPhone X'),
		('8', 'iPhone 8 Plus'),
		('9', 'iPhone 8')
	])


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/appointment')
def schedule():
	form = PhoneForm()

	context = {
		'form': form,
	}

	return render_template('schedule.html', **context)


@app.route('/dashboard')
def dashboard():
	username = session.get('username')

	if not username:
		return '<h1>No encontramos la página que buscas</h1>'

	context = {
		'username': username
	}

	return render_template('dashboard.html', **context)


@app.route('/device-status')
def status():
	return render_template('status.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	login_form = LoginForm()
	username = session.get('username')

	context = {
		'login_form': login_form,
		'username': username
	}

	if username:
		return redirect(url_for('dashboard'))

	if login_form.validate_on_submit():
		username = login_form.username.data
		# response = make_response(redirect(url_for('dashboard')))
		session['username'] = username
		print('perros')

		return redirect(url_for('dashboard'))

	return render_template('login.html', **context)
