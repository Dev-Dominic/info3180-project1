# Flask Modules
from flask import Flask 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# Addition of configuration folder to the PYTHONPATH
# Needed configuration folder to retrieve database credentials

import sys
import os
sys.path.append('config')

import config

app = Flask(__name__)  

# Dev config variables
app.config['SECRET_KEY'] = os.getenv('PROJECT1-SECRET-KEY') 

if app.config['SECRET_KEY'] == None: # Checks that project secret key is set
    raise RuntimeError('Project secret key not set')

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

dbCred = config.getCredentials()

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = config.getDatabaseURI()
db = SQLAlchemy(app)
migrate = Migrate(app,db)

# File upload config
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER')

from app import views, models
