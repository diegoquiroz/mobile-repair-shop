from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'KEY'

class LoginForm(FlaskForm):
	username = StringField('Nombre de usuario', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Enviar')


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/login')
def login():
	login_form = LoginForm()
	context = {
		'login_form': login_form
	}
	return render_template('form.html', **context)
