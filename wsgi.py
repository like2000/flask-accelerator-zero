from flask import Flask, send_from_directory
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    return send_from_directory('./', path)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
