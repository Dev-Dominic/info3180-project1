from flask import Flask 
# from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY'] = "qjA$A-kp>7Pe7D(" 


# Dev config variables
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


# FLASK DATABASE CONFIG
# db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
