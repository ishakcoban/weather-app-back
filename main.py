from flask import Flask
from flask_restful import Api, Resource
from operations import linearReg, decisionTree, getLastWeek

app = Flask(__name__)
api = Api(app)


class regression(Resource):
    def get(self):
        json = {
            'temperature': linearReg('temperature'),
            'wind': linearReg('wind'),
            'humidity': linearReg('humidity'),
            'pressure': linearReg('pressure'),

        }

        return json


class classify(Resource):
    def get(self):
        json = {
            'generalWeatherResult': decisionTree(linearReg('temperature'), linearReg('wind'), linearReg('humidity'),
                                                 linearReg('pressure'), ),
        }

        return json


class getLastWeekWeather(Resource):
    def get(self):

        json = {"oneWeek" : getLastWeek()}
        return json


api.add_resource(regression, "/linear")
api.add_resource(classify, "/decisionTree")
api.add_resource(getLastWeekWeather, "/weakly")

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
