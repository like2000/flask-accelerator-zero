from flask import send_from_directory
from flask_cors import CORS, cross_origin

from backend import create_app

# from backend.book import Book, Base

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

# app = create_app()
# CORS(app)
#
#
# @app.route('/<path:path>', methods=['GET', 'POST'])
# @cross_origin()
# def static_proxy(path):
#     return send_from_directory('static', path)
#
#
# @app.route('/', methods=['GET', 'POST'])
# @cross_origin()
# def index():
#     return send_from_directory('static', 'index.html')


# if __name__ == '__main__':
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

# app.run()
# try:
# host = "https://accelerator-zero.herokuapp.com"
# app.run(host=host)
# except:
#     host="localhost"
#     app.run(host=host)
