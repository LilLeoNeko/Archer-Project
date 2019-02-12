import os
from flask import url_for, render_template, flash, redirect, request
from flask_login import current_user, login_user, logout_user, login_required
from flask_wtf import FlaskForm

from sqlalchemy.sql.expression import func, select
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from archer import app, bcrypt, db
from archer.forms import RegistrationForm, LoginForm
from archer.models import User, Document, Partition, Post
from archer.CropPdf import CropPdf

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def initial():
	return render_template('homePage.html')

@app.route('/home')
@login_required
def home():
	return render_template('homePage.html')

@app.route('/about')
def about():
	return render_template('aboutPage.html')

'''	Login as a admin
	Provide partition management and document management
	Also Flag check and success partition
'''
@app.route('/admin')
@login_required
def admin():
	if current_user.username != "admin":
		flash('Oops, wrong place to go', 'danger')
		return redirect(url_for('home'))
	return render_template('adminPage.html')

@app.route('/upload', methods=["POST"])
@login_required
def upload():
	target = os.path.join(APP_ROOT, 'static/')
	if not os.path.isdir(target):
		os.mkdir(target)
	if 'file' not in request.files:
		flash('No file has been submit', 'danger')
		return redirect(url_for('admin'))

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
			newdoc = Document(docname = filename, doctype = "birth_1")
			db.session.add(newdoc)
			db.session.commit()
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
			newdoc = Document(docname = filename, doctype = "death_1")
			db.session.add(newdoc)
			db.session.commit()
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
			newdoc = Document(docname = filename, doctype = "death_2")
			db.session.add(newdoc)
			db.session.commit()
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
			newdoc = Document(docname = filename, doctype = "death_3")
			db.session.add(newdoc)
			db.session.commit()
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
		# if user is admin
		elif user.username == "admin" and bcrypt.\
		check_password_hash(user.userpwd, form.userpwd.data):
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
		newuser = User(username = form.username.data, 
					useremail = form.useremail.data, userpwd = hashPwd)
		db.session.add(newuser)
		db.session.commit()
		#Feedback to user, auto redirect to login page
		flash('Your account has been created, please login.', 'success')
		return redirect(url_for('login'))

	return render_template('registerPage.html',form = form)

@app.route('/work', methods=['GET','POST'])
@login_required
def work():
	global cur_part
	# first of all, return a random partition id 
	# and check it has been edited by current_user or not
	rand_part = Partition.query.filter(Partition.count < 2).\
				filter(Partition.editor1 != current_user.id).\
				filter(Partition.editor2 != current_user.id).\
				order_by(func.random()).first()
				
	if request.method == 'GET':
		cur_part = rand_part
	col_num = cur_part.getcolumn()

	# considering post form as a temporal form
	# which may varies due to different partition have different columns

	class PostForm(FlaskForm):
		pass

	for i in range(0,col_num):
		setattr (PostForm,'field'+str(i), StringField('content', 
													validators = [DataRequired()]) )
	setattr(PostForm, 'submit', SubmitField('Next'))
	form = PostForm()

	if form.validate_on_submit():
		templist = ""
		for field in form:
			if field.type == 'StringField':
				templist  += ';%s' % field.data
		
		newpost = Post(user_id = current_user.getid(),
						part_id = cur_part.getid(),
						content = templist)
		db.session.add(newpost)

		# get current count
		partcount = cur_part.getcount()
		print(cur_part.id)
		print(partcount)
		print("current user id: %d" %current_user.id)
		# set editor and increase count
		if partcount == 0:
			print("editing editor1")
			#temp_part.seteditor1(current_user.getid())
			setattr(Partition.query.filter_by(id = cur_part.id).first(),
					'editor1',current_user.getid())
		elif partcount == 1:
			print("editing editor2")
			#temp_part.seteditor2(current_user.getid())
			setattr(Partition.query.filter_by(id = cur_part.id).first(),
					'editor2',current_user.getid())

		#temp_part.setcount()
		setattr(Partition.query.filter_by(id = cur_part.id).first(),
				'count', partcount + 1)

		# commit to db
		db.session.flush()
		db.session.commit()

		print("new count: %d" %cur_part.getcount())

		flash('Your post has been uploaded.', 'success')
		return redirect(url_for('home'))

	return render_template('workPage.html', form = form, part = cur_part)

@app.route('/history')
@login_required
def history():
	posts = Post.query.filter_by(user_id = current_user.getid()).all()
	return render_template('historyPage.html', posts = posts)


@app.route('/check')
@login_required
def check():
	#for admin to check current post for each partition
	#each partition has two post or less, if two post same, flag will not rise
	#otherwise flag will be rised and admin will notice the difference
	if current_user.username != "admin":
		flash('Oops, wrong place to go', 'danger')
		return redirect(url_for('home'))

	# Get current finished partitions
	temp_parts = Partition.query.filter_by(count = 2).all()

	# Get post related to finished partition
	for part in temp_parts:
		posts = Post.query.filter_by(part_id = part.getid()).all()
		post1 = posts[0].getcontent()
		post2 = posts[1].getcontent()
		if post1 != post2:
			#part.setflag()
			setattr(part, 'flag', True)
	
	temp_parts = Partition.query.filter_by(flag = True).all()
	
	return render_template('checkPage.html', parts = temp_parts, post1 = post1, post2 = post2)

@app.route('/check/detail')
@login_required
def detail():
	return render_template('test.html')