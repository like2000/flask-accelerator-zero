from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_restful import Api, Resource
from backend.entities import Entity

app = Flask(__name__,
            static_folder='backend/static/')
api = Api(app)
CORS(app)

api.add_resource(Entity, '/data')


@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    return send_from_directory('backend/static', path)


@app.route('/')
def hello_world():
    return send_from_directory('backend/static', 'index.html')


if __name__ == '__main__':
    app.run()
