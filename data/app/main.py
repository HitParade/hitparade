import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import Result

@app.route("/")
def hello():

    print app.config

    return "Hello World from HitParade Flask in a uWSGI Nginx Docker container with \
     Python 2.7"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=81)
