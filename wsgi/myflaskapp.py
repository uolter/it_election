from flask import Flask, render_template
from pymongo import Connection
import settings
import json
from utils import json_encoders
from datetime import datetime, timedelta

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

_db = Connection(settings.mongodb_host, settings.mongodb_port)[settings.mongodb_database]
def _get_records(deep):

	if settings.mongodb_user:
		_db.authenticate(settings.mongodb_user, settings.mongodb_password)

	if deep == None: 
	    return _db.records.find().sort('date')

	d=datetime.today()-timedelta(hours = deep)

	return _db.records.find({"date": {"$gte":d }}).sort('date')

def _get_max_speeds():

	return _db.max_speed.find().sort("value", -1)

def _get_max_average():

	return _db.average.find().sort("value", -1)
 

@app.route("/list.json/<int:deep>")
def all(deep=None):	
	
	docs = _get_records(deep)

	return str(json.dumps(list(docs), cls=json_encoders.Encoder))

@app.route("/")
@app.route("/<int:deep>")
def index(deep=None):

	docs = _get_records(deep)

	max_speed = _get_max_speeds()

	average = _get_max_average()

	#data = json.dumps(list(docs), cls=json_encoders.Encoder)

	return render_template('index.html', 
		data=docs, 
		time=datetime.today(),
		max_speed = max_speed,
		average = average)


if __name__ == "__main__":
    app.run()
