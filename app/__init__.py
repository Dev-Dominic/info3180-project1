# Flask Modules
from flask import Flask 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Addition of configuration folder to the PYTHONPATH
# Needed configuration folder to retrieve database credentials
# For database init

import sys
sys.path.append('config')

import config

app = Flask(__name__)  

# Dev config variables
app.config['SECRET_KEY'] = "qjA$A-kp>7Pe7D(" 
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

dbCred = config.getCredentials()

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{dbCred['DB_USER']}:{dbCred['DB_PASSWORD']}@localhost/{dbCred['DB_NAME']}"
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app import views, models
