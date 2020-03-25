from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextAreaField, FileField, SubmitField
from wtforms.validators import InputRequired, Email, Length

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
    profilePicture = FileField("Profile Picture", validators=[FileRequired(), FileAllowed(['jpg', 'png']), 'Only jpg and png images allowed!'])
    submit = SubmitField("Add Profile")

