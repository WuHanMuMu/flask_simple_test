#!/usr/bin/python
#coding:utf-8


from app import db 
class Role(db.module):
	"""docstring for R"""
	__tablename__='roles'
	id=db.Column(db.Interger,primary_key=True)
	name=db.Column(db.String(64),unique=True)
	users=db.relationship('User',backref='role')
	def __init__(self, arg):
		super(R, self).__init__()
		self.arg = arg
	def __repr__(self):
		return 'table name is %s' %self.__tablename__
class User(db.module):
	"""docstring for User"""
	__tablename__='users'
	id=db.Column(db.Interger,primary_key=True)
	username=db.Column(db.String(64),unique=True,index=True)
	role_id=db.Column(db.Interger,db.ForeignKey('roles.id'))
	def __init__(self, arg):
		super(User, self).__init__()
		self.arg = arg
	def __repr__(self):
		return 'table name is %s' %self.__tablename__
		

