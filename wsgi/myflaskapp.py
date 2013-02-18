from flask import Flask, render_template
from pymongo import Connection
import settings
import json
from utils import json_encoders
from datetime import datetime, timedelta

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


def _get_records(deep):

	db = Connection(settings.mongodb_host, settings.mongodb_port)[settings.mongodb_database]

	if settings.mongodb_user:
		db.authenticate(settings.mongodb_user, settings.mongodb_password)

	if deep == None: 
		deep = 24


	d=datetime.today()-timedelta(hours = deep)

	return db.records.find({"date": {"$gte":d }}).sort('date')


@app.route("/list.json/<int:deep>")
def all(deep=None):

	
	
	'''
	dataset = db.record.aggregate(
		[
			{"$
			match": {"date": {"$lte": "new Date()" }}},
			{"$group":    


				{ 	"_id": "$name",      
					"trend": { "$push": { "speed": "$speed", "date": "$date"}}    
				} 
			}
		]
	)
	'''

	docs = _get_records(deep)

	return str(json.dumps(list(docs), cls=json_encoders.Encoder))

@app.route("/")
@app.route("/<int:deep>")
def index(deep=None):

	docs = _get_records(deep)

	#data = json.dumps(list(docs), cls=json_encoders.Encoder)
	

	return render_template('index.html', data=docs, time=datetime.today())



if __name__ == "__main__":
    app.run()
