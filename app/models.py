from . import db

class User(db.Model): 
    """ Project User class """
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(256), nullable=False)
    biography = db.Column(db.Text, nullable=False)

    def __init__(self, firstname, lastname, gender, email, location, biography):
        """ Class Attributes init """
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography

    def __repr__(self):
        """ Changing object string representation """
        return f"<User {self.firstname} {self.lastname}>"
