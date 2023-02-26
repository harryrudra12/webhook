from flask import request
from flask_app import app
import json

@app.route("/")
def main_idx():
    return "<p>Webhook Demo</p>"

@app.route("/webhook",methods=['POST'])
def get_data():
    if request.method == 'POST':
        process_data(request.json)
        if request.json["object_kind"] == "build":
            job_execution()
        elif request.json["object_kind"] == "merge_request":
            merge_request()
        print("================================")
        # print("Data received from GitLab is: ", request.json)  

        # Change made during recording (pretty print).
        print(json.dumps(request.json, indent=4) + "\n")
        return "Data received!"

def process_data(json_data):
    print(f'The data received is regarding: {json_data["object_kind"]}')
    print("====================================")

def job_execution():
    print("Do something with the job data")
    print("====================================")

def merge_request():
    print("Do something with the merge request data")
    print("====================================")

