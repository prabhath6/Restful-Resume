from flask import Flask, jsonify
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

app.config['MONGO_DBNAME'] = "resume" # adding database name
app.config["MONGO_URI"] = "mongodb://"+ os.environ["USERNAME"] + ":" + os.environ["PASSWORD"] + "@ds015995.mlab.com:15995/resume"

mongo = PyMongo(app)

@app.route("/", methods=["GET"])
def home():
    return "test"

@app.route("/resume", methods=["GET"])
def complete_resume():
    frame_work = mongo.db.my_resume

    output = []
    for i in frame_work.find():
        output.append({"contact" : i["contact_info"],
        "edu" : i["Education"],
        "Exp": i["Experience"],
        "skills" : i["Skills"], 
        "projects" : i["Projects"], 
        "links" : i["Links"]})

    return jsonify({"result" : output})


if __name__ == "__main__":
    app.run(debug=True)
