from pymongo import Connection, ASCENDING, DESCENDING
from datetime import datetime
import settings
import logging
from bson.code import Code

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(settings.fh)


db = Connection(settings.mongodb_host, settings.mongodb_port)[settings.mongodb_database]

_map = Code("function() { var max = 0; var name = ''; this.stat.forEach(function(val) { emit(val.name, val.speed); }); }")

def _map_reduce_max_speed():

	reduce = Code("function(key, emits) { db.mr_log.insert({'message': 'reduce key ' + key + ' emits: ' + emits}); var max = emits[0]; emits.forEach(function(val){ if (val > max) max = val; }); return max; } ")

	# drop the max speed collection:
	db.max_speed.remove()

	# run nap reduce to compute the max speed for each canditate:
	result = db.records.map_reduce(_map, reduce, 'max_speed')

	logger.info('Map Reduce Max Speed ok')
	logger.info(result)

	db.max_speed.create_index([("value", ASCENDING)])

def _map_reduce_avarage():

	reduce = Code("var reduce_max = function(key, emits) { var adv = 0; emits.forEach(function(val){ adv += val; }); return Number(adv / emits.length).toFixed(2); }")

	# drop the max speed collection:
	db.avarage.remove()

	# run nap reduce to compute the max speed for each canditate:
	result = db.records.map_reduce(_map, reduce, 'avarage')

	logger.info('Map Reduce Avarage ok')
	logger.info(result)

	db.avarage.create_index([("value", ASCENDING)])



def save(records):

	try:

		if settings.mongodb_user:
			db.authenticate(settings.mongodb_user, settings.mongodb_password)

		doc = {'date': datetime.today(), 'stat': []}

		for r in records:
			doc['stat'].append({'name': r, 'speed': records[r][0], 'acceleration':records[r][1]})

		db.records.insert(doc)

		db.records.create_index([("date", DESCENDING)])

		_map_reduce_max_speed()

		_map_reduce_avarage()

	except Exception, e:

		logger.error(e)





