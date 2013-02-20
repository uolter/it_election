from pymongo import Connection, ASCENDING, DESCENDING
from datetime import datetime
import settings
import logging
from bson.code import Code

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(settings.fh)


db = Connection(settings.mongodb_host, settings.mongodb_port)[settings.mongodb_database]

def save(records):

	try:

		if settings.mongodb_user:
			db.authenticate(settings.mongodb_user, settings.mongodb_password)

		doc = {'date': datetime.today(), 'stat': []}

		for r in records:
			doc['stat'].append({'name': r, 'speed': records[r][0], 'acceleration':records[r][1]})

		db.records.insert(doc)


		db.records.create_index([("date", DESCENDING)])

		# drop the max speed collection:
		db.max_speed.remove()

		# run nap reduce to compute the max speed for each canditate:
		result = db.records.map_reduce(_map, _reduce, 'max_speed')

		logger.info('Map Reduce ok')
		logger.info(result)

		db.max_speed.create_index([("value", ASCENDING)])



	except Exception, e:

		logger.error(e)

_map = Code("function() { var max = 0; var name = ''; this.stat.forEach(function(val) { emit(val.name, val.speed); }); }")

_reduce = Code("function(key, emits) { db.mr_log.insert({'message': 'reduce key ' + key + ' emits: ' + emits}); var max = emits[0]; emits.forEach(function(val){ if (val > max) max = val; }); return max; } ")

