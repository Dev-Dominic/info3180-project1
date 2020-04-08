from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextAreaField, FileField, SubmitField, validators
from wtforms.validators import InputRequired, Email, Length

# User sign-up form
class SignUpForm(FlaskForm): 
    firstname = StringField('First Name', validators=[
           InputRequired(),
            Length(min=3,max=30)
        ])
    lastname = StringField('Last Name', validators=[
            InputRequired(),
            Length(min=3,max=30)
        ])
    gender = SelectField("Gender", choices=[ 
        ("M", "Male"), ("F","Female"), ("N-B","Non-Binary"), ("A-H","Attack-Helicopter")])
    email = StringField('Email', validators=[
            InputRequired(),
            Email()
        ])
    location = StringField('Location', validators=[
            InputRequired(),
            Length(min=3,max=256)
        ])
    biography = TextAreaField('Biography', validators=[InputRequired()])
    profilePicture = FileField("Profile Picture",validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Add Profile")
