import string

import numpy as np
from flask import render_template, url_for, jsonify

from backend import db
from backend.moment import blueprint
from backend.moment.model import User

model = User(username="like", email="li-shing@gmx.de")
letts = list(string.ascii_lowercase)


@blueprint.route("/")
def home():
    return render_template(url_for('backend', filename='index.html'))


@blueprint.route("/newData", methods=['GET'])
def newData():
    model = User(username=''.join(np.random.choice(letts, 12)),
                 email=''.join(np.random.choice(letts, 3)))
    db.session.add(model)
    db.session.commit()

    data = list(map(lambda u: u.serialize, User.query.all()))
    # print("Query: ", {'data': list(map(lambda u: u.serialize, User.query.all()))})
    # return {'data': list(map(lambda u: u.serialize, User.query.all()))}
    return jsonify(data)
