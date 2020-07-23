from backend.chronicles import blueprint


@blueprint.route('/')
def index():
    return "Hello chronicles!"
