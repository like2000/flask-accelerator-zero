import numpy as np
import pandas as pd
from flask import jsonify, Response
from flask_restful import Resource


class Entity(Resource):

    def __init__(self):
        self.df = pd.DataFrame(columns=["Start", "Stop", "Period", "Info"])

    # @cross_origin(origin='*')
    def get(self):
        print(np.random.rand(4))
        self.df.loc[len(self.df)] = np.random.rand(4)
        self.df.reset_index(drop=True)
        print("Hello from Python!", len(self.df), id(self), id(self.df))
        response = Response(response=self.df.to_json(), status=200, mimetype="application/json")
        return response

    def save(self):
        pass
