from pymongo import Connection, ASCENDING, DESCENDING
from datetime import datetime
import settings
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(settings.fh)


def save(name, speed, acceleration):

	try:

		db = Connection(settings.mongodb_host, settings.mongodb_port)[settings.mongodb_database]

		db.authenticate(settings.mongodb_user, settings.mongodb_password)

		db.record.insert({
			'name': name,
			'date': datetime.today(),
			'speed' : speed,
			'acceleration': acceleration
		})

	
		db.record.create_index([("date", DESCENDING), ("name", ASCENDING)])

	except Exception, e:

		logger.error(e)