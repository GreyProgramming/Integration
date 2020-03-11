from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, IntegerField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users

class LoginButton(FlaskForm):
	submit = SubmitField('Login Page')

class PostForm(FlaskForm):
	title = StringField('Title',
		validators = [
			DataRequired(),
			Length(min=2, max=100)
		],
	)
	content = StringField('Content',
		validators = [
			DataRequired(),
			Length(min=100, max=1000)
		]
	)
	submit = SubmitField('Send submission!')

class RegistrationForm(FlaskForm):
	first_name = StringField('First Name',
		validators = [
			DataRequired(),
			Length(min=2, max=30)
		]
	)
	last_name = StringField('Last Name',
		validators = [
			DataRequired(),
			Length(min=2, max=30)
		]
	)
	email = StringField('Email',
		validators = [
			DataRequired(),
		]
	)
	password = PasswordField('Password',
		validators = [
			DataRequired(),
		]
	)
	confirm_password = PasswordField('Confirm your Password',
		validators = [
			DataRequired(),
			EqualTo('password')
		]
	)
	submit = SubmitField('Sign Up')

	def validate_email(self, email):
		user = Users.query.filter_by(email=email.data).first()

		if user:
			raise ValidationError('That email is already in use.')

class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		]
	)

	password = PasswordField('Password',
		validators=[
			DataRequired()
		]
	)

	remember = BooleanField('Remember your login?')
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	first_name = StringField('First Name',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
		])
	last_name = StringField('Last Name',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
		])
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	submit = SubmitField('Update')

	def validate_email(self,email):
		if email.data != current_user.email:
			user = Users.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Email already in use')

class PlayerForm(FlaskForm):
	Player_name = StringField('Player Name',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
		])
	submit = SubmitField('Generate')


class GeneratorForm(FlaskForm):
	Player_name = StringField('Player Name',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
		])
	Char_name = StringField('Character Name',
		validators=[
			DataRequired(),
			Length(min=1, max=30)
		])
	Level = IntegerField('Level',
		validators=[
			DataRequired()
		])
	Alignment = StringField('Alignment',
		validators=[
			DataRequired()
		])
	Char_Gender = StringField('Gender',
		validators=[
			DataRequired()
		])
	Race = StringField('Race',
		validators=[
			DataRequired()
		])
	Class = StringField('Class',
		validators=[
			DataRequired()
		])
	STR = IntegerField('Strength',
		validators=[
			DataRequired()
		])
	DEX = IntegerField('Dexterity',
		validators=[
			DataRequired()
		])
	CON = IntegerField('Constitution',
		validators=[
			DataRequired()
		])
	INT = IntegerField('Intelligence',
		validators=[
			DataRequired()
		])
	WIS = IntegerField('Wisdom',
		validators=[
			DataRequired()
		])
	CHA = IntegerField('Charisma',
		validators=[
			DataRequired()
		])
	submit = SubmitField('Save')
