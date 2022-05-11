import zmqpubsub
from flask import Flask, request
from flask_restful import Api, Resource
from tinydb import TinyDB

from vessel_data import VesselValues

app = Flask(__name__)
api = Api(app)

vesselValues = VesselValues()


class RetrieveVesselData(Resource):
    def get(self):
        return {"type": vesselValues.types,
                "geometry": vesselValues.geometry_type,
                "latitude": vesselValues.latitude,
                "longitude": vesselValues.longitude,
                "sogkph": vesselValues.sogKph,
                "headingTrueDegrees": vesselValues.headingTrueDegrees,
                "epochSeconds": vesselValues.epochSeconds}


class VesselSpeed(Resource):
    def get(self):
        return {"speed": vesselValues.sogKph}


class VesselHeading(Resource):
    def get(self):
        return {"heading": vesselValues.headingTrueDegrees}


class VesselLocation(Resource):
    def get(self):
        return {"latitude": vesselValues.latitude, "longitude": vesselValues.longitude}


# class VesselHistoricalData(Resource):
#     def get(self):
#         return json.dumps()


# return str(database.get_vessel_historical_data()).replace('[', '{', 1).replace(']', '}', 1)


class HelloWorld(Resource):
    def get(self):
        return {"about": "Hello world"}

    def post(self):
        some_json = request.get_json()
        return {"you sent": some_json}, 201


class Multi(Resource):
    def get(self, num):
        return {"result": num * 10}


api.add_resource(HelloWorld, "/helloworld")
api.add_resource(Multi, "/multi/go/<int:num>")
api.add_resource(RetrieveVesselData, "/data")
api.add_resource(VesselSpeed, "/data/speed")
api.add_resource(VesselHeading, "/data/heading")
api.add_resource(VesselLocation, "/data/location")
# api.add_resource(VesselHistoricalData, "/data/historicalData")
