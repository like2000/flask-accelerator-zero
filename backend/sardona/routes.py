from backend.sardona import blueprint


@blueprint.route('/')
def index():
    return "Hello sardona!"
