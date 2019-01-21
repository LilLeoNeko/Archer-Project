from flask import url_for, render_template, flash, redirect
from flask_login import current_user, login_user, logout_user
from archer import app, bcrypt, db
from archer.forms import RegistrationForm, LoginForm
from archer.models import User

@app.route('/')
def initial():
	return render_template('homePage.html')


@app.route('/home') 
def home():
	return render_template('homePage.html')


@app.route('/login', methods=['GET','POST'])
def login():

	if current_user.is_authenticated:
		return redirect(url_for('home'))

	form = LoginForm()
	if form.validate_on_submit():
		#if form.email.data in database, form.password.data == password in db
		#then
		user = User.query.filter_by(useremail=form.useremail.data).first()
		if user is None or not bcrypt.check_password_hash(user.userpwd, form.userpwd.data):
			flash('Login failed, please check your email and password', 'danger')
			return redirect(url_for('login'))
		#else if email doesn't exist, remind email not register
		else:
			login_user(user)
			return redirect(url_for('home'))
	return render_template('loginPage.html', form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('initial'))

@app.route('/register', methods=['GET','POST'])
def register():

	if current_user.is_authenticated:
		return redirect(url_for('home'))

	form = RegistrationForm()
	if form.validate_on_submit():
		#create and store hash password
		hashPwd = bcrypt.generate_password_hash(form.userpwd.data).decode('utf-8')
		newuser = User(username = form.username.data, useremail = form.useremail.data, userpwd = hashPwd)
		db.session.add(newuser)
		db.session.commit()
		#Feedback to user, auto redirect to login page
		flash('Your account has been created, please login.', 'success')
		return redirect(url_for('login'))

	return render_template('registerPage.html',form = form)

@app.route('/about')
def about():
	return render_template('aboutPage.html')