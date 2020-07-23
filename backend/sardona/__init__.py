from flask import Blueprint

import pathlib

name = pathlib.Path(__file__).parent.name

Blueprint(
    name + '_blue', __name__,
)
