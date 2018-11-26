from flask import Blueprint
from flask import request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from threading import Timer
from flask import Response

from datetime import datetime
import json

# blueprint for message_route
message_route = Blueprint("message_route", __name__)

#Initiate the scheduler
scheduler = BackgroundScheduler({'apscheduler.timezone':'Asia/Calcutta'})
scheduler.start()

@message_route.route("/message", methods=["POST"])
def print_messages():
    """
    print the incoming message after the given interval of time
    """
    data = request.get_json()
    if ('delivery_time' in data) and ('message' in data):
        try:
            date_time = datetime.strptime(str(data["delivery_time"]),'%Y-%m-%dT%H:%M')
        except ValueError:
            return Response(
                response=json.dumps({"message":"Date should be in %Y-%m-%dT%H:%M format","status":400}),
                status=400, mimetype='application/json'
            )
        # Run the scheduled task -- and print the message at the given time
        job = scheduler.add_job(printing_message,trigger='date',next_run_time=str(date_time),args=[data["message"],date_time])
        payload = {
            "status":202,
            "message": "Message -- "+data["message"]+" -- will be written to the console at "+data["delivery_time"]
        }
        # Success 202 
        return Response(
            response=json.dumps(payload),
            status=202, mimetype='application/json'
        )
    else:
        # Invalid input -- with status code 400
        return Response(
            response=json.dumps({"message":"Invalid input"}),
            status=400, mimetype='application/json'
        )
def validate_date(date_text):
    """
    Vaidates the given date is in the format %Y-%m-%dT%H:%M
    """
    try:
        date_time = datetime.strptime(str(date_text),'%Y-%m-%dT%H:%M')
    except ValueError:
        return Response(
            response=json.dumps({"message":"Invalid date"}),
            status=400, mimetype='application/json'
        )

def printing_message(text,date_time):
    print("Printing %s at %s" %(text,date_time))
