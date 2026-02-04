from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, TextAreaField, MultipleFileField, FileField
from flask_wtf.file import FileAllowed


class SubmitPost(FlaskForm):
    title = StringField("Title", [validators.Length(min=4, max=26)])
    content = TextAreaField("Content", [validators.Length(min=4)])
    #This is not fucking working
    media = FileField("Upload Images/Videos (.mp4, .png, .jpeg)", validators=[
            FileAllowed(['mp4', 'png', 'jpeg'], 'File Type not accepted')
        ])
    submit = SubmitField("Submit")