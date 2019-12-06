from flask import Flask, render_template, session, redirect, url_for, flash
from forms import LoginForm, PhoneForm, StatusForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'KEY'


@app.errorhandler(404)
def not_found(error):
	return render_template('404.html')


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/appointment', methods=['GET', 'POST'])
def schedule():
	form = PhoneForm()

	context = {
		'form': form,
	}

	if form.validate_on_submit():
		return redirect('/success')

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
	form = StatusForm()

	context = {
		'form': form,
	}

	return render_template('status.html', **context)


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

		flash('Inicio de sesión con éxito para el usuario {}'.format(username))

		return redirect(url_for('dashboard'))

	return render_template('login.html', **context)


@app.route('/success')
def success():
	email = session.get('email')

	context = {
		'email': email
	}
	return render_template('success.html', **context)
