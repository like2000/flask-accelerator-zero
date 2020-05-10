from flask import jsonify
from flask_restful import Resource


class Entity(Resource):

    def __init__(self):
        pass

    def get(self):
        print("Hello from Python!")
        return jsonify({
            'Orc': 800,
            'Farnir': 400,
            'Goblin': 200,
        })

    def data_output(self):
        pass
