import json
import string

from flask import render_template, url_for, jsonify

import numpy as np
from backend import db
from backend.moment import blueprint
from backend.moment.model import Book, User

model = User(username="like", email="li-shing@gmx.de")
letts = list(string.ascii_lowercase)


@blueprint.route("/")
def index():
    return "Hello Kevin!"
    # return render_template('index.html')
    # return render_template(url_for('backend', filename='index.html'))


@blueprint.route("/newData", methods=['GET'])
def newData():
    model = User(username=''.join(np.random.choice(letts, 12)),
                 email=''.join(np.random.choice(letts, 3)))
    db.session.add(model)
    db.session.commit()

    print("Query: ", User.query.all())
    return User.query.all()
