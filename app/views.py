from app import app
from flask import render_template, request, redirect, url_for, flash

@app.route("/")
def home(): 
    return render_template("base.html")

@app.route("/about")
def about(): 
    return "about"

@app.route("/profile")
def createProfile(): 
    return "createProfile"

@app.route("/profile/<uid>")
def profile(uid): 
    return "profile"

@app.route("/profiles")
def profiles(): 
    return "profiles"

