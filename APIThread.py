import datetime
import pymongo
import requests
import gzip
import io
import json
import threading

class APIThread(threading.Thread)
    def __init__(self, db):
        self.api_key = "4bd26ccf66f03a976bcd92c7eeec4627"
        self.db = db.weather.data
        #self.db = pymongo.MongoClient().weather.data
        threading.Thread.__init__()
    
    def run(self):
        self.load_cities()

        while True:
            for entry in self.db.find():
                if not "timestamp" in entry:
                    self.update_entries(entry["city"], upsert=True)
                elif (entry["timestamp"] - datetime.datetime.now()).hours > 1:
                    self.update_entries(entry["city"], upsert=False)

    def load_cities(self):
        raw_list = requests.get('http://bulk.openweathermap.org/sample/city.list.json.gz')
        buffer = io.BytesIO(raw_list.content)
        parsed_list = json.loads(gzip.GzipFile(fileobj=buffer).read().decode('utf-8'))
        db.insert_many([{"city": city["name"]} for city in parsed_list])

    def update_entries(self, entry, upsert=False):
        payload = {
            "q": entry,
            "appid": self.api_key
        }

        new_data = requests.get("api.openweathermap.org/data/2.5/weather", params=payload)

        self.db.update(
            {"_id": entry["_id"]},
            {"$set": {
                    "timestamp": datetime.datetime.fromtimestamp(new_data["dt"]),
                    "temperature": new_data["main"]["temp"],
                    "max": new_data["main"]["temp_max"],
                    "min": new_data["main"]["temp_min"]
                }
            },
            upsert=upsert
        )