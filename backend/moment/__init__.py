from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

name = 'moment'

blueprint = Blueprint(
    name + '_blueprint',
    import_name=__name__,
    template_folder='templates'
)
