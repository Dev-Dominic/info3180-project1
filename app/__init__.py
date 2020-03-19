# FLASK CONFIG

from flask import Flask 
from flask_bootstrap import Bootstrap
# from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
Bootstrap(app)

# FLASK DATABASE CONFIG
# db = SQLAlchemy(app)


from app import views
