from flask import jsonify
import pandas as pd
import numpy as np
from flask_cors import cross_origin
from flask_restful import Resource
from flask_restful.utils import cors


class Entity(Resource):

    def __init__(self):
        self.df = pd.DataFrame(columns=["Start", "Stop", "Period", "Info"])

    # @cross_origin(origin='*')
    def get(self):
        self.df.loc[len(self.df)] = [np.random.rand(4)]
        self.df.reset_index(drop=True)
        print("Hello from Python!")
        print(self.df.to_json())

        return self.df.to_json()
        # return jsonify({
        #     'Orc': 800,
        #     'Farnir': 400,
        #     'Goblin': 200,
        # })

    def save(self):
        pass

    def data_output(self):
        pass
