from flask import Flask, make_response, render_template
from pymongo import Connection, ASCENDING, DESCENDING
import settings
from bson import json_util
import json
from utils import json_encoders

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/list.json")
def all():

	db = Connection(settings.mongodb_host, settings.mongodb_port)[settings.mongodb_database]

	if settings.mongodb_user:
		db.authenticate(settings.mongodb_user, settings.mongodb_password)
	
	'''
	dataset = db.record.aggregate(
		[
			{"$match": {"date": {"$lte": "new Date()" }}},
			{"$group":    
				{ 	"_id": "$name",      
					"trend": { "$push": { "speed": "$speed", "date": "$date"}}    
				} 
			}
		]
	)
	'''

	docs = db.records.find().limit(48)
	
	
	return str(json.dumps(list(docs), cls=json_encoders.Encoder))

@app.route("/")
def index():

	db = Connection(settings.mongodb_host, settings.mongodb_port)[settings.mongodb_database]

	if settings.mongodb_user:
		db.authenticate(settings.mongodb_user, settings.mongodb_password)
	
	docs = db.records.find().limit(48)

	#data = json.dumps(list(docs), cls=json_encoders.Encoder)
	
	return render_template('index.html', data=docs)



if __name__ == "__main__":
    app.run()
