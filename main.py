from flask import Flask
from flask_restful import Api, Resource
from operations import linearReg, decisionTree, getLastWeek,getAllCategories,getAllSubCategories,getAllTypes,getAllColors,getAllClothes

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

class getAllCategories_(Resource):
    def get(self):

        json = {"categories" : getAllCategories()}
        return json

class getAllSubCategories_(Resource):
    def get(self):

        json = {"subCategories" : getAllSubCategories()}
        return json

class getAllTypes_(Resource):
    def get(self):

        json = {"types" : getAllTypes()}
        return json

class getAllColors_(Resource):
    def get(self):

        json = {"colors" : getAllColors()}
        return json

class getAllClothes_(Resource):
    def get(self):

        json = {"clothes" : getAllClothes()}
        return json


api.add_resource(regression, "/linear")
api.add_resource(classify, "/decisionTree")
api.add_resource(getLastWeekWeather, "/weakly")
api.add_resource(getAllCategories_, "/categories")
api.add_resource(getAllSubCategories_, "/subCategories")
api.add_resource(getAllTypes_, "/types")
api.add_resource(getAllColors_, "/colors")
api.add_resource(getAllClothes_, "/clothes")

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
