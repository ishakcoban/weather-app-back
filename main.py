from flask import Flask
from flask_restful import Api, Resource
from operations import LinearReg
app = Flask(__name__)
api = Api(app)


class Linear(Resource):
    def get(self):

        json = {
            'temperature':LinearReg('temperature'),
            'wind': LinearReg('wind'),
            'humidity': LinearReg('humidity'),
            'pressure': LinearReg('pressure'),


        }

        return json


api.add_resource(Linear, "/linear")

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
