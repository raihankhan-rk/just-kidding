from utils.helper import parse_json
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from datetime import datetime, date
from db.db import db
import pytz


app = Flask(__name__)
cors = CORS(app)
now = datetime.now(pytz.timezone("Asia/Calcutta"))
today = date.today()

app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin()
def home():
    return jsonify({"status": 200, "message": "Server Up and running!"})


@app.route("/post-joke", methods=["POST"])
@cross_origin()
def post_joke():
    try:
        data = request.json
        data["time"] = now.strftime("%H:%M")
        data["date"] = today.strftime("%d/%m/%Y")
        db.jokes.insert_one(parse_json(data))
        print(data)
        # return data
        return "Voila! You just posted a joke on Just-kidding! Check it out on https://just-kidding.vercel.app"
    except:
        return "Oops! Some Error occured. you might wanna recheck your json data once again."


@app.route("/get-jokes", methods=["GET"])
@cross_origin()
def get_jokes():
    data = db.jokes.find()
    return parse_json(data)


if __name__ == '__main__':
    app.run(debug=True)
