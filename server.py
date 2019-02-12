import gzip
import io
import json
import pymongo
import requests
import time
import zmq

from APIThread import APIThread

db = pymongo.MongoClient()

def get_data():

def get_temperature(city):
    result = db.find_one({ "city": city })
    return json.dumps({
        "daily_max": result["temp_max"]
        "daily_min": result["temp_min"]
    })

def get_current_temp(city):
    result = db.find_one({ "city": city })
    return json.dumps({
        "temperature": result["temperature"]
    })

def get_cities(city=None):
    result = db.find()
    return json.dumps({
        "cities": [value for value in result["city"]]
    })

callback_list = {
    "temperature": get_temperature,
    "current_temp": get_current_temp,
    "cities": get_cities
}

def run_callback(command, data):
    if command in callback_list:
        response = callback_list[command](data)
        socket.send(response)
    else:
        payload = json.dumps({ "error": "command not found" })
        #  Send reply back to client
        socket.send(payload)

api = APIThread(db)
api.start()

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = json.loads(socket.recv())
    
    run_callback(message["command"], message["data"])

