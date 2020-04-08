from app import app, db
from app.models import User
from flask import render_template, request, redirect, url_for, flash
from .forms import SignUpForm
from datetime import date

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

    if not form.validate():
        flash('Sign Up failed!')
        return template

    # User email addresses should be unique
    # User email entered is queried to the database
    # Renders flash message and returns to /profile endpoint
    # If email exists in database

    checkEmail = User.query.filter_by(email=form.email.data).first()
    if form.email.data == None: 
        flash('User email has already been used!')
        return template
    
    # user = User(*form, date.today()) # Unpacking form data to create new user
    print(form.data)
    user = User(form.firstname.data, form.lastname.data, form.gender.data, form.email.data, form.location.data, form.biography.data, date.today())
    db.session.add(user)
    db.session.commit()

    flash('SUCCESFULL SIGNUP')
    template = redirect(url_for('profiles'))
    return template

@app.route("/profile/<uid>")
def profile(uid): 
    return "profile"

@app.route("/profiles")
def profiles(): 
    return "profiles"

