import os


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