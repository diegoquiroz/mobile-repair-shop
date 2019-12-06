from flask import Flask, render_template, session, redirect, url_for, flash
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from firestore_service import get_user, set_appointment
from forms import LoginForm, PhoneForm, StatusForm
from models import UserModel, UserData


app = Flask(__name__)

app.config['SECRET_KEY'] = 'KEY'

login_manager = LoginManager()
login_manager.login_view = 'login'

login_manager.init_app(app)


@login_manager.user_loader
def load_user(username):
	return UserModel.query(username)


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
		brand = form.brand.data
		model = form.model.data
		problem = form.problem.data
		problem_explanation = form.problem_explanation.data
		email = form.email.data
		set_appointment(brand, model, problem, problem_explanation, email)

		return redirect('/success')

	return render_template('schedule.html', **context)


@app.route('/dashboard')
@login_required
def dashboard():
	username = current_user.id
	context = {
		'username': username,
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

	if current_user:
		return redirect(url_for('dashboard'))

	if login_form.validate_on_submit():
		username = login_form.username.data
		password = login_form.password.data

		user_doc = get_user(username)

		if user_doc.to_dict() is not None:
			password_from_db = user_doc.to_dict()['password']

			if password == password_from_db:
				user_data = UserData(username, password)
				user = UserModel(user_data)

				login_user(user)
				flash('Login success')

				return redirect(url_for('dashboard'))
			else:
				flash('Information does not match')
		else:
			flash('User does not exist')

	return render_template('login.html', **context)


@app.route('/logout')
@login_required
def logout():
	logout_user()

	return redirect(url_for('login'))


@app.route('/success')
def success():
	email = session.get('email')

	context = {
		'email': email
	}
	return render_template('success.html', **context)
