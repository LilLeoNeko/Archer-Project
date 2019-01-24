from datetime import datetime
from flask_login import UserMixin
from archer import db,login

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

class User(UserMixin,db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20),unique=True,nullable=False)
	useremail=db.Column(db.String(120),unique=True,nullable=False)
	userpwd=db.Column(db.String(24),nullable=False)

	def __repr__(self):
		return '<User: %r>' % self.username

# NOT DECIDED CODES# NOT DECIDED CODES# NOT DECIDED CODES# NOT DECIDED CODES
class Document(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	#doc_file = db.Column(db)
	docname = db.Column(db.String(30),nullable=False)
	doctype = db.Column(db.String(20),nullable=False)
	docdate = db.Column(db.DateTime,nullable=False)
	

	def __repr__(self):
		return '<Document: %r>' % self.docname

class Partition(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	column = db.Column(db.Integer, nullable = False)
	count = db.Column(db.Integer, nullable = False, default = 0)
	flag = db.Column(db.Boolean, nullable = False, default = False)
	doc_id = db.Column(db.Integer, db.ForeignKey('document.id'), nullable=False)

	def get_column():
		return self.column
'''	def random_part():
		return Partition.query()'''

# partition to user is a many to many relationship
# each partition may have 2 users to enter, each user can edit numerous partition
# therefore post class should be an association table
# form will be like user1.post.append(partition)

'''class Post(db.Model):
	__tablename__ = 'post'
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	part_id = db.Column(db.Integer, db.ForeignKey('partition.id'), nullable = False)
	#not sure if it still needs ID
	#id = db.Column(db.Integer, primary_key=True)
	timestamp = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
	content = db.Column(db.Text, nullable = False)

	def __repr__(self):
		return '<Post content: %r>' % self.content'''
# NOT DECIDED CODES# NOT DECIDED CODES# NOT DECIDED CODES# NOT DECIDED CODES