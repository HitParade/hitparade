import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# This probably doesn't belong here, but I have no idea where it should go
def create_app():
    config_name = os.environ['APP_SETTINGS']

    app = Flask(__name__)
    app.config.from_object(config_name)
    db = SQLAlchemy(app)

    return app, db

app, db = create_app()

from models import *


@app.route("/")
def hello():

    print app.config

    return "Hello World from HitParade Flask in a uWSGI Nginx Docker container with \
     Python 2.7"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=81)
