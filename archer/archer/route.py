import os
from flask import url_for, render_template, flash, redirect, request
from flask_login import current_user, login_user, logout_user, login_required
from flask_wtf import FlaskForm
from sqlalchemy.sql.expression import func, select
from wtforms import StringField, SubmitField
from archer import app, bcrypt, db
from archer.forms import RegistrationForm, LoginForm
from archer.models import User, Partition, Post
from archer.CropPdf import CropPdf

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

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
@app.route('/admin')
def admin():
	return render_template('adminPage.html')

@app.route('/upload', methods=["POST"])
@login_required
def upload():
	target = os.path.join(APP_ROOT, 'Certificates/')
	if not os.path.isdir(target):
		os.mkdir(target)

	for file in request.files.getlist("birth_1"):
		print(file)
		if file:
			filename=file.filename
			target1 = os.path.join(target, 'birth_1/')
			if not os.path.isdir(target1):
				os.mkdir(target1)
			destination = "/".join([target1, filename])
			print(destination)
			file.save(destination)
			CropPdf(filename, target1)


	for file in request.files.getlist("death_1"):
		print(file)
		if file:
			filename=file.filename
			target1 = os.path.join(target, 'death_1/')
			if not os.path.isdir(target1):
				os.mkdir(target1)
			destination = "/".join([target1, filename])
			print(destination)
			file.save(destination)
			CropPdf(filename, target1)

	for file in request.files.getlist("death_2"):
		print(file)
		if file:
			filename=file.filename
			target1 = os.path.join(target, 'death_2/')
			if not os.path.isdir(target1):
				os.mkdir(target1)
			destination = "/".join([target1, filename])
			print(destination)
			file.save(destination)
			CropPdf(filename, target1)

	for file in request.files.getlist("death_3"):
		print(file)
		if file:
			filename=file.filename
			target1 = os.path.join(target, 'death_3/')
			if not os.path.isdir(target1):
				os.mkdir(target1)
			destination = "/".join([target1, filename])
			print(destination)
			file.save(destination)
			CropPdf(filename, target1)

	return render_template("upload_completed.html")

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
		elif user.username is "admin":
			login_user(user)
			return redirect(url_for('admin'))
		else:
			login_user(user)
			return redirect(url_for('home'))

	return render_template('loginPage.html', form=form)

@app.route('/logout')
@login_required
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
	# first of all, return a random partition id 
	# and check it has been edited by current_user or not
	
	rand_part = Partition.query.filter(Partition.count < 2).order_by(func.random()).first()
	col_num = rand_part.getcolumn()
	
	# considering post form as a temporal form
	# which may varies due to different partition have different columns
	class PostForm(FlaskForm):
		pass

	for i in range(0,col_num):
		setattr (PostForm,'field'+str(i), StringField('content') )

	setattr(PostForm, 'submit', SubmitField('Next'))

	form = PostForm()
	if form.validate_on_submit():
		templist = ""
		for field in form:
			if field.type == 'StringField':
				templist  += ';%s' % field.data
		
		newpost = Post(user_id = current_user.getid(),
						part_id = rand_part.getid(),
						content = templist)

		# increase count by 1
		partcount = rand_part.getcount()
		rand_part.count = partcount + 1

		# commit to db
		db.session.add(newpost)
		db.session.commit()
	return render_template('workPage.html', form = form, part = rand_part)

@app.route('/test', methods=['GET','POST'])
def test():
	posts = Post.query.filter_by(user_id = current_user.getid()).all()
	return render_template('test.html', posts = posts)


@app.route('/about')
def about():
	return render_template('aboutPage.html')

@app.route('/check')
@login_required
def check():
	#for admin to check current post for each partition
	#each partition has two post or less, if two post has same content, flag will not rise
	#otherwise flag will be rised and admin will notice the difference

	
	# Get current finished partitions
	temp_parts = Partition.query.filter_by(count = 2).all()

	# Get post related to finished partition
	for part in temp_parts:
		posts = Post.query.filter_by(part_id = part.getid()).all()
		post1 = posts[0].getcontent()
		post2 = posts[1].getcontent()
		if post1 != post2:
			part.setflag()
	
	temp_parts = Partition.query.filter_by(flag = True).all()
	
	return render_template('check.html', parts = temp_parts)

@app.route('/check/detail')
@login_required
def detail():
	return render_template('test.html')