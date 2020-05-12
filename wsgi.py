from flask import Flask, send_from_directory
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource
from backend.entities import Entity

app = Flask(__name__,
            static_folder='backend/static/')
app.config['CORS_HEADERS'] = 'Content-Type'

api = Api(app)
api.add_resource(Entity, '/data')

CORS(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route('/<path:path>', methods=['GET', 'POST'])
# @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@cross_origin(origin='*')
def static_proxy(path):
    return send_from_directory('backend/static', path)


@app.route('/', methods=['GET', 'POST'])
# @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@cross_origin(origin='*')
def hello_world():
    return send_from_directory('backend/static', 'index.html')


if __name__ == '__main__':
    # try:
    host = "https://accelerator-zero.herokuapp.com"
    app.run(host=host)
# except:
#     host="localhost"
#     app.run(host=host)
