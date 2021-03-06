'''
Created on Jun 29, 2012

@author: uolter
'''

import logging
import os

# twitter account: place here your twitter account
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

if os.environ.get('OPENSHIFT_PYTHON_LOG_DIR'):
	fh = logging.FileHandler('%stwitter_speed.log' %os.environ['OPENSHIFT_PYTHON_LOG_DIR'])
else:
	fh = logging.FileHandler('twitter_speed.log')


fh.setLevel(logging.DEBUG)


# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
	

search_for = ['bersani', 'berlusconi', 'grillo', 'monti', 'vendola']

# mongodb.
if os.environ.get('OPENSHIFT_MONGODB_DB_HOST') and os.environ.get('OPENSHIFT_MONGODB_DB_PORT'):
	mongodb_host = os.environ['OPENSHIFT_MONGODB_DB_HOST']
	mongodb_port = int(os.environ['OPENSHIFT_MONGODB_DB_PORT'])
	mongodb_user = 'admin'
	mongodb_password = '8LtPnFkR6dBp'	

else:
	mongodb_host = 'localhost'
	mongodb_port = 27017
	mongodb_user = mongodb_password = None

mongodb_database = 'electionspeed'
