import os
import json
from flask import Flask 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = "qjA$A-kp>7Pe7D(" 


# Dev config variables
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


# FLASK DATABASE CONFIG
ROOTDIR = os.getenv('INFO3180_PROJECT1_ROOTDIR')  
if ROOTDIR == None:
    print("Project path variable not set! Please Set first!")

credentialsFile = os.path.join(ROOTDIR, "config", "database_credentials.json")

with open(credentialsFile) as fptr:
    db = json.load(fptr) 

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db['DB_USER']}:{db['DB_PASSWORD']}@localhost/{db['DB_NAME']}"
db = SQLAlchemy(app)

app.config['SQLALCHMEY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app,db)

app.config.from_object(__name__)
from app import views, models
