from app import app
from flask import render_template, request, redirect, url_for, flash
from .forms import NewUserForm

@app.route("/")
def home(): 
    return render_template("home.html")

@app.route("/about")
def about(): 
    return "about"

@app.route("/profile")
def createProfile(): 
    form = NewUserForm() 
    return render_template("createProfile.html", form=form) 

@app.route("/profile/<uid>")
def profile(uid): 
    return "profile"

@app.route("/profiles")
def profiles(): 
    return "profiles"

