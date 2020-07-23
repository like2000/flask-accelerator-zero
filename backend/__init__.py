from importlib import import_module

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def register_extensions(server: Flask):
    ...


def register_blueprints(server: Flask):
    for module_name in ('angular', 'moment', 'sardona',):
        module = import_module(f'backend.{module_name}.routes')
        server.register_blueprint(module.blueprint, url_prefix=f'/{module_name}')


def create_app():
    server = Flask(__name__)
    server.config.from_object('config.LocalConfig')

    with server.app_context():
        register_blueprints(server)
        db.init_app(server)
        db.create_all()

        return server
