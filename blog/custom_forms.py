from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, TextAreaField, MultipleFileField, FileField
from flask_wtf.file import FileAllowed


class SubmitPost(FlaskForm):
    title = StringField("Title", [validators.Length(min=4, max=26)])
    content = TextAreaField("Content", validators=[validators.Length(min=4)])
    media = FileField("Upload Images/Videos (.mp4, .png, .jpeg, .jpg)", validators=[
            FileAllowed(['mp4', 'png', 'jpeg', 'jpg'], 'File Type not accepted'),
            validators.Optional()
        ])
    submit = SubmitField("Submit")