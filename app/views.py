from app.models import User
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from .forms import SignUpForm
from datetime import date

import os

@app.route("/")
def home(): 
    return render_template("home.html")

@app.route("/about")
def about(): 
    return "about"

@app.route("/profile", methods=['GET', 'POST'])
def createProfile(): 
    """Create profile 

    Args: 
        None

    Return: 
        template: render /profile or /profiles endpoint
    """

    form = SignUpForm() 
    template = render_template("createProfile.html", form=form)

    if request.method != "POST": 
        return template  

    if 'profilePicture' not in request.files: # Checking if image was sent with request
        flash('No profile picture uploaded!')
        return template

    _file = request.files['profilePicture']

    # Validation of form data 
    # Checks that a file was submitted
    # Checks that file does not contain empty string
    # as filename

    if not (form.validate() or _file or _file.filename):
        flash('Sign Up failed!')
        return template

    # User email addresses should be unique
    # User email entered is queried to the database
    # Renders flash message and returns to /profile endpoint
    # If email exists in database

    checkEmail = User.query.filter_by(email=form.email.data).first()
    if checkEmail != None: 
        flash('User email has already been used!')
        return template

    
    filterUserData = dict(filter(lambda attr: attr[0] in User.attrs, form.data.items())) # Filter form data for user model related data
    save_user(filterUserData) 
    upload_profile_picture(_file, filterUserData['email'])


    flash('SUCCESFULL SIGNUP')
    template = redirect(url_for('profiles'))
    return template

def save_user(userData):
    """Creates and saves new user

    Args:
        userData: Dictionary containg data to create new user

    Return:
        None

    """
    
    user = User(**userData, dateJoined = date.today())
    db.session.add(user)
    db.session.commit()


def upload_profile_picture(profilePicture, email): 
    """Upload new user profile picture

    Args:
        profilePicture: File containing new user profile picture
        email:  Used to make sure each profile picture is unique

    Return: 
        None

    """
    filename = f'{email}_{secure_filename(profilePicture.filename)}'
    profilePicture.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  

@app.route("/profile/<uid>")
def profile(uid): 
    return "profile"

@app.route("/profiles")
def profiles(): 
    return "profiles"

