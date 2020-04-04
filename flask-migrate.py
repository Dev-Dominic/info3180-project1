#!/usr/env/python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app 
from app import db

migrate = Migrate(app,db)
manager = Manager(app,db)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
