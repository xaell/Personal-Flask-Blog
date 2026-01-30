from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField, MultipleFileField

class SubmitPost(FlaskForm):
    title = StringField("Title", [validators.Length(min=4, max=26)])
    visuals = MultipleFileField("Upload Images/Videos (.mp4, .png, .jpeg)")
    content = TextAreaField("Content", [validators.Length(min=4)])