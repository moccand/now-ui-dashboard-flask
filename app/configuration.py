# -*- encoding: utf-8 -*-
"""
Flask Web App - Generated by www.AppSeed.us
AppSeed - developed by RoSoft | www.RoSoftware.ro
Licence: MIT
"""

import os.path

# Only cfg is here .. 
class AppConfig(object):

	# comon vars here 
	APP         = 'app'
	SECRET_KEY  = "_9^MHFJhtTrNHFhdDdfdGJJJJJJ%$fVGhaXsa_!@#"

class Config(AppConfig):
	"""
	Configuration base, for all environments.
	"""
	DEBUG                 			= False
	TESTING               			= False
	BOOTSTRAP_FONTAWESOME 			= True
	CSRF_ENABLED          			= True

	SQLALCHEMY_TRACK_MODIFICATIONS 	= False

class ProductionConfig(Config):

	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://appseed:appseed@localhost/appseed-flask"

	SERVER_NAME   = 'www.awesome.com' # <- your public domain here
	DEBUG         = False
	TESTING       = False

class DevelopmentConfig(Config):

	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://appseed:appseed@localhost/appseed-flask"

	SERVER_NAME   = 'localhost:5000'
	DEBUG	= False
	TESTING	= False

