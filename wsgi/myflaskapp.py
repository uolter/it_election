from flask import Flask, make_response
from pymongo import Connection, ASCENDING, DESCENDING
import settings
from bson import json_util
import json

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


def jd(obj):
    return json.dumps(obj, default=json_util.default)

#
# Response
#

def response(data={}, code=200):
    resp = {
        "code" : code,
        "data" : data
    }
    response = make_response(jd(resp))
    response.headers['Status Code'] = resp['code']
    response.headers['Content-Type'] = "application/json"
    return response


@app.route("/")
def hello():

	db = Connection(settings.mongodb_host, settings.mongodb_port)[settings.mongodb_database]

	# db.authenticate(settings.mongodb_user, settings.mongodb_password)
	
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

	docs = db.record.find()
	
	return response(docs[:]) 

if __name__ == "__main__":
    app.run()
