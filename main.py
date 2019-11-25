from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'KEY'


class LoginForm(FlaskForm):
	username = StringField('Nombre de usuario', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Log In')


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/appointment')
def schedule():
	return render_template('schedule.html')


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
		'username': username	username = session.get('username')

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
