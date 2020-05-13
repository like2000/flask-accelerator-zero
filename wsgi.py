from flask import Flask, send_from_directory
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource
from backend.entities import Entity

app = Flask(__name__,
            static_folder='backend/static/')
CORS(app)

api = Api(app)
api.add_resource(Entity, '/data')


@app.route('/<path:path>', methods=['GET', 'POST'])
@cross_origin()
def static_proxy(path):
    return send_from_directory('backend/static', path)


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def hello_world():
    return send_from_directory('backend/static', 'index.html')


if __name__ == '__main__':
    # app.run()

    # try:
    host = "https://accelerator-zero.herokuapp.com"
    app.run(host=host)
    # except:
    #     host="localhost"
    #     app.run(host=host)
