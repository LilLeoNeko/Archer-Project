from datetime import datetime
from flask_login import UserMixin
from archer import db,login

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

class User(UserMixin,db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20),unique=True,nullable=False)
	useremail=db.Column(db.String(120),unique=True,nullable=False)
	userpwd=db.Column(db.String(24),nullable=False)
	partitions = db.relationship('Post', backref='author', lazy=True)

	def __repr__(self):
		return '<User: %r>' % self.username
	def getid(self):
		return self.id

# NOT DECIDED CODES# NOT DECIDED CODES# NOT DECIDED CODES# NOT DECIDED CODES
class Document(db.Model):
	__tablename__ = 'document'
	id = db.Column(db.Integer,primary_key=True)
	#doc_file = db.Column(db)
	docname = db.Column(db.String(30), unique = True, nullable=False)
	doctype = db.Column(db.String(20),nullable=False)
	partitions = db.relationship('Partition', backref='doc', lazy=True)
	# docdate = db.Column(db.DateTime,nullable=False)
	

	def __repr__(self):
		return '<Document: %r>' % self.docname

class Partition(db.Model):
	__tablename__ = 'partition'
	id = db.Column(db.Integer,primary_key=True)
	doc_id = db.Column(db.Integer, db.ForeignKey('document.id'), nullable=False)
	editor1 = db.Column(db.Integer, db.ForeignKey('user.id'))
	editor2 = db.Column(db.Integer, db.ForeignKey('user.id'))

	column = db.Column(db.Integer, nullable = False)
	count = db.Column(db.Integer, nullable = False)
	flag = db.Column(db.Boolean, nullable = False)
	url = db.Column(db.String(120),nullable = False, unique = True)
	properties = db.Column(db.String, nullable=False)

	editors = db.relationship('Post', backref='partition', lazy=True)

	def getid(self):
		return self.id

	def geteditor1(self):
		return self.editor1

	def geteditor2(self):
		return self.editor2

	def getcolumn(self):
		return self.column

	def getcount(self):
		return self.count

	def getflag(self):
		return self.flag

	def geturl(self):
		return self.url

	def getproperties(self):
		return [str(i) for i in self.properties.split(';')]

'''
	def setcount(self):
		self.count += 1
	def setflag(self):
		self.flag = True
	def seteditor1(self, user_id):
		self.editor1 = user_id
	def seteditor2(self, user_id):
		self.editor2 = user_id
'''

# partition to user is a many to many relationship
# each partition may have 2 users to enter, each user can edit numerous partition
# therefore post class should be an association table
# form will be like user1.post.append(partition)

class Post(db.Model):
	__tablename__ = 'post'
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
	part_id = db.Column(db.Integer, db.ForeignKey('partition.id'), primary_key = True)
	#not sure if it still needs ID
	#id = db.Column(db.Integer, primary_key=True)
	timestamp = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
	content = db.Column(db.String, nullable = False)

	user = db.relationship('User', backref = 'part_post')
	part = db.relationship('Partition', backref = 'user_post')
	def __repr__(self):
		return '<Post user_id: %d> <Post content: %s>' % (self.user_id, self.content)
	
	def getcontent(self):
		return [str(i) for i in self.content.split(';')]

# NOT DECIDED CODES# NOT DECIDED CODES# NOT DECIDED CODES# NOT DECIDED CODES