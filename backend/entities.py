import numpy as np
import pandas as pd
from flask import jsonify
from flask_restful import Resource


class Entity(Resource):

    def __init__(self):
        self.df = pd.DataFrame(columns=["Start", "Stop", "Period", "Info"])

    # @cross_origin(origin='*')
    def get(self):
        print(np.random.rand(4))
        self.df.loc[len(self.df)] = np.random.rand(4)
        self.df.reset_index(drop=True)
        print("Hello from Python!")
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
