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
		('Apple', 'Apple'),
		('Huawei', 'Huawei'),
		('Samsung', 'Samsung'),
		('LG', 'LG'),
		('Xiaomi', 'Xiaomi'),
		('Nokia', 'Nokia')
	])
	model = SelectMultipleField('Model', validators=[DataRequired()], choices=[
		('iPhone 11 Pro', 'iPhone 11 Pro'),
		('iPhone 11 Pro Max', 'iPhone 11 Pro Max'),
		('iPhone 11', 'iPhone 11'),
		('iPhone XS', 'iPhone XS'),
		('iPhone XS', 'iPhone XS'),
		('iPhone XR', 'iPhone XR'),
		('iPhone X', 'iPhone X'),
		('iPhone 8 Plus', 'iPhone 8 Plus'),
		('iPhone 8', 'iPhone 8')
	])
	problem = SelectMultipleField('Problem', validators=[DataRequired()], choices=[
		('Screen', 'Screen'),
		('It is soaking wet', 'It is soaking wet'),
		('Does not turn on', 'Does not turn on'),
		('Other(Specify bellow)', 'Other(Specify bellow)')
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
