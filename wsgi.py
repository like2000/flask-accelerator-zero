from flask import Flask, send_from_directory, render_template, request, redirect, url_for
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from backend.book import Book, Base

from backend import create_app
from backend.entities import Entity

# api = Api(app)
# api.add_resource(Entity, '/data')


# import pandas as pd
#
# df = pd.DataFrame(columns=["Start", "Stop", "Period", "Info"])

# @app.route('/newData', methods=['GET', 'POST'])
# def getData():
#     df.loc[len(df)] = np.random.rand(4)
#     df.reset_index(drop=True)
#     print(df.to_dict(orient='records'))
#
#     return {'data': [df.to_dict(orient='records')]}

# print("Running from inside main!")
app = create_app()
CORS(app)


@app.route('/<path:path>', methods=['GET', 'POST'])
@cross_origin()
def static_proxy(path):
    return send_from_directory('static', path)


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def index():
    return send_from_directory('static', 'index.html')


# try:
host = "https://accelerator-zero.herokuapp.com"
app.run(host=host)

if __name__ == '__main__':
    print("Running from inside main!")
    app = create_app()
    CORS(app)

    # try:
    host = "https://accelerator-zero.herokuapp.com"
    app.run(host=host)
    # except:
    #     host="localhost"
    #     app.run(host=host)
