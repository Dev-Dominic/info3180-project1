#!/usr/bin/python

from app.models import User
from app import db

def newTestUser(*args):
    user = User(*args)
    db.session.add(user)
    db.session.commit()

if __name__ == "__main__":
    newTestUser("dominic", "henry", "M", "dominichenrywork@hotmail.com", "Jamaica", "Dominic bio")
    newTestUser("ladonna", "larmine", "F", "la_ladonna@hotmail.com", "Jamaica", "Ladonna bio")

    users = User.query.all()
    for user in User.query.all(): 
        print(user)
