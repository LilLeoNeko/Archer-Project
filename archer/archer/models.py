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
	# docdate = db.Column(db.DateTime,nullable=False)
	

	def __repr__(self):
		return '<Document: %r>' % self.docname

class Partition(db.Model):
	__tablename__ = 'partition'
	id = db.Column(db.Integer,primary_key=True)
	doc_id = db.Column(db.Integer, db.ForeignKey('document.id'), nullable=False)
	editor1 = db.Column(db.String(20), db.ForeignKey('user.username'))
	editor2 = db.Column(db.String(20), db.ForeignKey('user.username'))

	column = db.Column(db.Integer, nullable = False)
	count = db.Column(db.Integer, nullable = False, default = 0)
	flag = db.Column(db.Boolean, nullable = False, default = False)
	url = db.Column(db.String(120),nullable = False, unique = True)

	def getid(self):
		return self.id

	def geteditor1(self):
		return self.editor1

	def seteditor1(self, name):
		self.editor1 = name

	def seteditor2(self, name):
		self.editor2 = name

	def geteditor2(self):
		return self.editor2

	def getcolumn(self):
		return self.column

	def getcount(self):
		return self.count

	def getflag(self):
		return self.flag

	def setflag(self):
		self.flag = True

	def geturl(self):
		return self.url

# partition to user is a many to many relationship
# each partition may have 2 users to enter, each user can edit numerous partition
# therefore post class should be an association table
# form will be like user1.post.append(partition)

class Post(db.Model):
	__tablename__ = 'post'
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True, nullable=False)
	part_id = db.Column(db.Integer, db.ForeignKey('partition.id'), primary_key = True, nullable = False)
	#not sure if it still needs ID
	#id = db.Column(db.Integer, primary_key=True)
	timestamp = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
	content = db.Column(db.String, nullable = False)

	def __repr__(self):
		return '<Post user_id: %d> <Post content: %s>' % (self.user_id, self.content)
	
	def getcontent(self):
		return [str(i) for i in self.content.split(';')]

# NOT DECIDED CODES# NOT DECIDED CODES# NOT DECIDED CODES# NOT DECIDED CODES