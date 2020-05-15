from importlib import import_module

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def register_extentions(server: Flask):
    ...


def register_blueprints(server: Flask):
    for module_name in ('moment',):
        module = import_module(f'backend.{module_name}.routes')
        server.register_blueprint(module.blueprint, url_prefix=f'/{module_name}')


def register_db(server: Flask, path='sqlite:///data/data.db'):
    server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    server.config['SQLALCHEMY_DATABASE_URI'] = path
    db.init_app(server)


def create_app():
    # server = Flask(
    #     __name__,
    #     static_folder='backend/static',
    #     template_folder='backend/templates',
    # )
    server = Flask(
        __name__,
        static_folder='static',
        template_folder='templates',
    )

    register_blueprints(server)
    register_db(server)

    return server
