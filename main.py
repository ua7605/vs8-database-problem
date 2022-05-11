import threading
import time

import zmqpubsub

import RESTApi
from database import Database

from vessel_data import VesselValues

db = Database()
vesselValues = VesselValues()

class Vincent:
    number = 20

def read_vessel_data():
    while True:
        print(vesselValues.longitude)
        time.sleep(1)

# In this function the received data of VS8 in JSON format will be accessible.
def callbackFunc(message_in_json_object):
    vesselValues.types = message_in_json_object["type"]
    vesselValues.geometry_type = message_in_json_object["geometry"]["type"]
    vesselValues.latitude = message_in_json_object["geometry"]["coordinates"][1]
    vesselValues.longitude = message_in_json_object["geometry"]["coordinates"][0]
    vesselValues.sogKph = message_in_json_object["properties"]["sogKph"]
    vesselValues.headingTrueDegrees = message_in_json_object["properties"]["headingTrueDegrees"]
    vesselValues.epochSeconds = message_in_json_object["properties"]["epochSeconds"]
    try:
        db.insert_values(type=vesselValues.types,
                         geometry_type=vesselValues.geometry_type,
                         latitude=vesselValues.latitude,
                         longitude=vesselValues.longitude,
                         sogkph=vesselValues.sogKph,
                         headingTrueDegrees=vesselValues.headingTrueDegrees,
                         epochSeconds=vesselValues.epochSeconds)
        print("stored in db")
    except:
        print("An exception ERROR occurred")

if __name__ == '__main__':
    #  IMEC public IP: 193.190.127.147, for testing with the demo publisher local host IP: 127.0.0.1
    subscriber = zmqpubsub.Subscriber(ip='193.190.127.147', port='2001')
    subscriber.subscribe(topic="allData", callback=callbackFunc)
    thread = threading.Thread(target=read_vessel_data)
    thread.start()
    # RESTApi.app.run(host="127.0.0.1", debug=False)
    RESTApi.app.run(host="143.129.80.148", debug=False)

