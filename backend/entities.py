from flask import jsonify
from flask_cors import cross_origin
from flask_restful import Resource
from flask_restful.utils import cors


class Entity(Resource):

    def __init__(self):
        pass

    @cross_origin(origin='*')
    def get(self):
        print("Hello from Python!")
        return jsonify({
            'Orc': 800,
            'Farnir': 400,
            'Goblin': 200,
        })

    def data_output(self):
        pass
