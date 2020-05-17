from flask import Blueprint

name = 'moment'

blueprint = Blueprint(
    name + '_blueprint',
    import_name=__name__,
    template_folder='templates'
)
