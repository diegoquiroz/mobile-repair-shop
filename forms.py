from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Log In')


class PhoneForm(FlaskForm):
	brand = SelectMultipleField('Brand', validators=[DataRequired()], choices=[
		('1', 'Apple'),
		('2', 'Huawei'),
		('3', 'Samsung'),
		('4', 'LG'),
		('5', 'Xiaomi'),
		('6', 'Nokia')
	])
	model = SelectMultipleField('Model', validators=[DataRequired()], choices=[
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
	problem = SelectMultipleField('Problem', validators=[DataRequired()], choices=[
		('1', 'Screen'),
		('2', 'It is soaking wet'),
		('3', 'Does not turn on'),
		('4', 'Other(Specify bellow)')
	])
	problem_explanation = StringField('Explain with your own words')
	date = DateField('Select a Day', format='%Y-%m-%d', validators=[DataRequired()])
	time = TimeField('Select a time', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired()])
	schedule = SubmitField('Schedule')


class StatusForm(FlaskForm):
	order_id = StringField('Introduce your order ID',  validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired()])
	check = SubmitField('Check')
