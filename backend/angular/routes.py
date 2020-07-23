from backend.angular import blueprint


@blueprint.route('/')
def index():
    return "Hello angular!"
