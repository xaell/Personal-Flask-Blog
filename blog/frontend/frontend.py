from flask import render_template
from . import frontendBP

@frontendBP.route("/")
@frontendBP.route("/home")
def home():
    return render_template("frontend/home.html")

@frontendBP.route("/aboutMe")
def aboutMe():
    return "About Me page"