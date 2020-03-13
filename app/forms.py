
# Script Imports
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, FileField, SubmitField
from wtfforms.validators import InputRequired, Email, Length, RegExp

# User sign-up form
class NewUserForm(FlaskForm): 
    firstName = StringField('First Name', validators=[
            InputRequired(),
            Length(min=3,max=30)
        ])
    lastName = StringField('Last Name', validators=[
            InputRequired(),
            Length(min=3,max=30)
        ])
    gender = SelectField("Gender", choices=[ 
        ("Male", "Female", "Non-Binary", "Attack-Helicopter")])
    email = StringField('Email', validators=[
            InputRequired(),
            Email()
        ])
    location = StringField('Last Name', validators=[
            InputRequired(),
            Length(min=3,max=30)
        ])
    biography = TextAreaField('Biography', validators=[InputRequired()])
    profilePicture = FileField("Profile Picture", [
            Regexp(u"^[^/\\]\.(jpg|png)$", message="Incorrect file format, jpg or png needed")
        ])
    submit = SubmitField("Add Profile")

