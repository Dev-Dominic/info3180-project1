from app.models import User
from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename 
from .forms import SignUpForm
from datetime import date

import os

@app.route("/")
def home(): 
    return render_template("home.html", title='Home')

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

    def createTemplate(error=None, error_msg=None, form=form):
        """Creates create profile teimplate

            Arg: 
                error: Error type
                error_msg: Error message to be render to create profile template

           Return:
                template: Renders teimplate for create profile with any
                errors or error messages
        """
        return render_template(
                'createProfile.html', 
                error=error, 
                error_msg=error_msg, 
                form=form,
                title='Create Profile')


    if request.method != "POST": 
        template = createTemplate()
        return template  

    if 'profilePicture' not in request.files: # Checking if image was sent with request
        template = createTemplate('alert-warning', 'No profile picture uploaded!')
        return template

    _file = request.files['profilePicture']

    # Validation of form data 
    # Checks that a file was submitted
    # Checks that file does not contain empty string
    # as filename

    if not (form.validate() or _file or _file.filename):
        template = createTemplate(error='alert-danger', error_msg='Sign up failed!')
        return template

    # User email addresses should be unique
    # User email entered is queried to the database
    # Renders flash message and returns to /profile endpoint
    # If email exists in database

    checkEmail = User.query.filter_by(email=form.email.data).first()
    if checkEmail != None: 
        template = createTemplate(error='alert-warning', error_msg='User email has already been used!')
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

    flash('Succesful signup', 'alert-success')
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
    """Renders a given users profile

    Args:
        uid: id of a given user stored in the database

    Return:
        template: Rendered template of a given user

    """
    user = User.query.get(uid)

    template = render_template('profile.html', user=user)
    return template 

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

    template = render_template('profiles.html', users=users, title='Profiles')  
    return template 

@app.route('/upload/<path:filename>')
def uploaded_file(filename):
    """Retrieves an upload file 

    Retrives file path from upload_folder if file exists,
    otherwise a default_image is sent in place. 

    Args:
        filename: Name of file to retrieve 

    Return:
       filepath: Path to file in upload_folder

    """
    filePath = os.path.join(app.config['UPLOAD_FOLDER'], filename) 
    if not os.path.exists(filePath):
        filename = 'default_image.jpg'

    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
