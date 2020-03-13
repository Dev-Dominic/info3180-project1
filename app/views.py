from app import app
from flask import render_template

@app.route("/")
def home(): 
    return "home"

@app.route("/profile")
def createProfile(): 
    return "createProfile"

@app.route("/profile/<uid>")
def profile(uid): 
    return "profile"

@app.route("/profiles")
def profiles(): 
    return "profiles"

