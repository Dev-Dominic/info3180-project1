from app.models import User
from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
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

    # Filter form data for user model related data
    # Securing and saving profile picture filename 
    
    filterUserData = dict(filter(lambda attr: attr[0] in User.attrs, form.data.items())) 
    profileImage = secure_filename(_file.filename)
    _file.save(os.path.join(app.config['UPLOAD_FOLDER'], profileImage))  

    # Updating filtered user data dictionary with profile image
    # filename, as well as, save the new user data to database

    filterUserData['profileImage'] = profileImage 
    save_user(filterUserData) 

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

@app.route("/profile/<uid>")
def profile(uid): 
    return "profile"

@app.route('/profiles')
def profiles(): 
    """Renders template with all user profiles listed

    Args:
        None

    Return:
        template: Rendered profiles.html template with all users
        and boolean value 

    """
    users = User.query.all()

    template = render_template('profiles.html', users=users)  
    return template 

@app.route('/upload/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
