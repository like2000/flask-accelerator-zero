from flask import Flask, send_from_directory
from flask_restful import Api

app = Flask(__name__,
            static_folder='backend/static/')
api = Api(app)


@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    return send_from_directory('backend/static', path)


@app.route('/')
def hello_world():
    return send_from_directory('backend/static', 'index.html')


if __name__ == '__main__':
    app.run()
