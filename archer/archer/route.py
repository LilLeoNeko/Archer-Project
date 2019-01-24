from flask import url_for, render_template, flash, redirect
from flask_login import current_user, login_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from archer import app, bcrypt, db
from archer.forms import RegistrationForm, LoginForm
from archer.models import User, Partition

@app.route('/')
def initial():
	return render_template('homePage.html')

@app.route('/home')
@login_required
def home():
	return render_template('homePage.html')

'''	Login as a admin
	Provide partition management and document management
	Also Flag check and success partition
'''
@app.route('/administrator')
@login_required
def admin():
	return render_template('adminPage.html')

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

@app.route('/work', methods=['GET','POST'])
@login_required
def work():
	# Get corresponding partition first
	'''

	if request.method is 'POST':
		abcd
		form = PostForm()
	if form.validate_on_submit():
		return redirect(url_for('work'))
	'''

	return render_template('workPage.html')

@app.route('/test', methods=['GET','POST'])
def test():
	class TestForm(FlaskForm):
		pass
	x = 5
	for i in range(0,x):
		setattr (TestForm,'field'+str(i), StringField('content') )

	setattr(TestForm, 'submit', SubmitField('Next'))

	form = TestForm()
	return render_template('test.html', form = form)


@app.route('/about')
def about():
	return render_template('aboutPage.html')