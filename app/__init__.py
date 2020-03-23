from flask import Flask 
# from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY'] = "qjA$A-kp>7Pe7D(" 
app.config['static_folder'] = "static" 

# FLASK DATABASE CONFIG
# db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
