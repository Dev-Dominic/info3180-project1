# FLASK CONFIG

from flask import Flask 
# from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)

# FLASK DATABASE CONFIG
# db = SQLAlchemy(app)


from app import views
