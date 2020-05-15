from flask import render_template, url_for

from backend.moment import blueprint
from backend.moment.model import Book

model = Book()


@blueprint.route("/")
def index():
    return "Hello Kevin!"
    # return render_template('index.html')
    # return render_template(url_for('backend', filename='index.html'))
