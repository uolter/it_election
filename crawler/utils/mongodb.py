from pymongo import Connection, ASCENDING, DESCENDING
from datetime import datetime
import settings
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(settings.fh)


def save(records):

	try:

		db = Connection(settings.mongodb_host, settings.mongodb_port)[settings.mongodb_database]

		if settings.mongodb_user:
			db.authenticate(settings.mongodb_user, settings.mongodb_password)

		doc = {'date': datetime.today(), 'stat': []}

		for r in records:
			doc['stat'].append({'name': r, 'speed': records[r][0], 'acceleration':records[r][1]})

		db.records.insert(doc)

	
		db.records.create_index([("date", DESCENDING)])

	except Exception, e:

		logger.error(e)