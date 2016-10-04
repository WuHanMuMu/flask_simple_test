#!/usr/bin/python
#coding:utf-8

from flask import Flask 
from flask import request 
from flask import render_template
from flask.ext.script import Manager
from flask_sqlalchemy import SQLAlchemy
import os
app=Flask(__name__)
manager=Manager(app)
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data/sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db=SQLAlchemy(app)
print basedir


# sql jiegou 
class Role(db.Model):
	"""docstring for R"""
	__tablename__='roles'
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(64),unique=True)
	users=db.relationship('User',backref='role')
	
	def __repr__(self):
		return 'table name is %s' %self.__tablename__
class User(db.Model):
	"""docstring for User"""
	__tablename__='users'
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(64),unique=True,index=True)
	role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))

	def __repr__(self):
		return 'table name is %s' %self.__tablename__


@app.route('/')
def index():
	
	return render_template('index.html',user='wang')
	#return 'static uri error'


@app.route('/<anything>')
def othertry(anything):
	return 'oher try %s' %anything


if __name__=='__main__':
	#app.run(debug=True)
	manager.run()
