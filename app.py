from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Sensor_Reading(Resource):
    def get(self, data):
        return {'data': data}


api.add_resource(Sensor_Reading, '/sensor-reading/<string:data>')


if __name__ == '__main__':
    app.run(port=5000)
