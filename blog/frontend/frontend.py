from flask import Blueprint

frontendBP = Blueprint('frontendBP', __name__)

@frontendBP.route("/home")
def home():
    return "This should be the home page"

@frontendBP.route("/aboutMe")
def aboutMe():
    return "About Me page"