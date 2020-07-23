from flask import render_template, send_from_directory, url_for

from backend.angular import blueprint


@blueprint.route('/')
def index():
    return render_template("index.html")


@blueprint.route('/<path:path>', methods=['GET', 'POST'])
def static_proxy(path):
    return send_from_directory('angular/static', path)
    # return send_from_directory(url_for('angular_blue.static', filename=''), path)
