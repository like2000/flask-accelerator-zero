from backend.album import blueprint


@blueprint.route('/')
def index():
    return "Hello from album!"
