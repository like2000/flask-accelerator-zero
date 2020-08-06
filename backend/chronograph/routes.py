import string

import numpy as np
from flask import render_template, url_for, jsonify

from backend import db
from backend.chronograph import blueprint
from backend.chronograph.model import User

model = User(username="like", email="li-shing@gmx.de")
letts = list(string.ascii_lowercase)


@blueprint.route("/")
def home():
    return render_template(url_for('backend', filename='index.html'))


@blueprint.route("/show_data", methods=["GET"])
def show_data():
    data = list(map(lambda u: u.serialize, User.query.all()))
    # print("Query: ", {'data': list(map(lambda u: u.serialize, User.query.all()))})
    # return {'data': list(map(lambda u: u.serialize, User.query.all()))}
    return jsonify(data)


@blueprint.route("/new_data", methods=['GET'])
def new_data():
    model = User(username=''.join(np.random.choice(letts, 12)),
                 email=''.join(np.random.choice(letts, 3)))
    db.session.add(model)
    db.session.commit()

    data = list(map(lambda u: u.serialize, User.query.all()))
    # print("Query: ", {'data': list(map(lambda u: u.serialize, User.query.all()))})
    # return {'data': list(map(lambda u: u.serialize, User.query.all()))}
    return jsonify(data)
