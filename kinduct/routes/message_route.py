from flask import Blueprint
from flask import request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from threading import Timer

from datetime import datetime


message_route = Blueprint("message_route", __name__)
print("Iam coming here")
scheduler = BackgroundScheduler({'apscheduler.timezone':'Asia/Calcutta'})
scheduler.start()

@message_route.route("/print_message", methods=["POST"])
def print_messages():
    """
    print the incoming message after the given interval of time
    """
    data = request.get_json()
    print("Data coming",data)
    if ('delivery_time' in data) and ('message' in data):
        date_time = datetime.strptime(str(data["delivery_time"]),'%Y-%m-%dT%H:%M')
        job = scheduler.add_job(printing_message,trigger='date',next_run_time=str(date_time),args=[data["message"],date_time])
        payload = {
            "status":202,
            "message": "Message -- "+data["message"]+" -- will be written to the console at "+data["delivery_time"],
            # "job_details": job
        }
        return jsonify(payload)
    else:
        print("Invalid Input")

def printing_message(text,date_time):
    print("Printing %s at %s" %(text,date_time))
