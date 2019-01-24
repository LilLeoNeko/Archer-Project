from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from archer.models import User


class RegistrationForm(FlaskForm):
	username = StringField('User Name',
		validators=[DataRequired(),Length(min=3, max=20)])
	useremail = StringField('Email',
		validators=[DataRequired(),Email()])
	userpwd = PasswordField('Password',
		validators = [DataRequired(),Length(min=6, max=24)])
	confirmpwd = PasswordField('Comfirm Password',
		validators = [DataRequired(), EqualTo('userpwd')])
	#submit registration
	submit = SubmitField('Register Now')

	def checkNameExist(self,username):
		#basicly it should be unique, therefore only check 1st exist or not
		user = User.query.filter_by(username = username.data).first()
		if user:
			raise ValidationError('User name exist!')

	def checkEmailExist(self,useremail):
		#basicly it should be unique, therefore only check 1st exist or not
		user = User.query.filter_by(useremail=useremail.data).first()
		if user:
			raise ValidationError('User e-mail has been registered!')

class LoginForm(FlaskForm):
	useremail = StringField('Email',
		validators=[DataRequired(),Email()])
	userpwd = PasswordField('Password',
		validators = [DataRequired()])
	#submit registration
	submit = SubmitField('Login')

class PostForm(FlaskForm):
	submit = SubmitField('Complete')

	def appendField(Pos, name, field):
		setattr(PostForm, content, TextAreaField())
		return PostForm