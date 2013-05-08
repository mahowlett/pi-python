from bottle import default_app,route,template
import config


@route('/hello')
def hello():
	return "Hello World!"

@route('/hello/<name>')
def greet(name):
	return template('Hello {{name}} how you doin?',name=name)

@route('/')
def index():
	return "Smee!!!"

#mysql prefixed routes
import mysqlexamples

#led prefixed routes
import ledController

#temp prefixed routes
import tempController

application = default_app()

