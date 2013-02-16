'''
Created on Jun 29, 2012

@author: uolter
'''

import logging
import os

consumer_key = 'vquiabfT8GjCAnrQcOPkbQ'
consumer_secret = 'DSfhhVcMVI0AAfCumYWECyO9J6Ikagy7cjPmYcazU'
access_token = '32822337-BXc7x6zQ9j72rugwHKHFgFDmuyJSVjOITplZHY5vx'
access_token_secret = '8JIvAPV6GgGm2VjcpZWolMs7XdvviH4FAFgHl0wRUHM'

fh = logging.FileHandler('twitter_speed.log')
fh.setLevel(logging.DEBUG)


# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
	

search_for = ['apple', 'microsoft']

# mongodb.
if os.environ['OPENSHIFT_MONGODB_DB_HOST'] and os.environ['OPENSHIFT_MONGODB_DB_PORT']:
	mongodb_host = os.environ['OPENSHIFT_MONGODB_DB_HOST']
	mongodb_port = int(os.environ['OPENSHIFT_MONGODB_DB_PORT'])
else:
	mongodb_host = 'localhost'
	mongodb_port = 27017

"""

MongoDB 2.2 database added.  Please make note of these credentials:

       Root User: admin
   Root Password: 8LtPnFkR6dBp
   Database Name: electionspeed

Connection URL: mongodb://$OPENSHIFT_MONGODB_DB_HOST:$OPENSHIFT_MONGODB_DB_PORT/

"""	