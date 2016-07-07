from flask import Flask, jsonify
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

app.config['MONGO_DBNAME'] = "resume" # adding database name
app.config["MONGO_URI"] = "mongodb://"+ os.environ["USERNAME"] + ":" + os.environ["PASSWORD"] + "@ds015995.mlab.com:15995/resume"

mongo = PyMongo(app)

@app.route("/", methods=["GET"])
def complete_resume():
    frame_work = mongo.db.my_resume

    output = []
    for i in frame_work.find():
        output.append({"Contact Information" : i["contact_info"],
        "Education" : i["Education"],
        "Experience": i["Experience"],
        "Skills" : i["Skills"], 
        "Projects" : i["Projects"], 
        "Links" : i["Links"]})

    return jsonify({"Resume" : output})


@app.route("/resume/<param>", methods=["GET"])
def get_education(param):
    frame_work = mongo.db.my_resume

    output = []

    if param == "education":
        key = "Education"
    elif param == "skills":
        key = "Skills"
    elif param == "experience":
        param == "Experience" 
    elif param == "projects":
        key = "Projects":
    elif param == "contact":
        param == "contact_info"
    elif param == "links":
        key = "Links"

    for i in frame_work.find():
        key : i[key]

    return jsonify({key : output})


if __name__ == "__main__":
    app.run(debug=True)
