from flask import render_template, Blueprint
from blog.models import Post
from blog.db import create_session
from blog.custom_forms import SubmitPost

frontendBP = Blueprint(
    'frontendBP', 
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/frontend_static")

@frontendBP.route("/", methods = ["GET"])
@frontendBP.route("/home", methods = ["GET"])
def home():
    session = create_session()
    try:
        #This will order the post by date and frontend displays them in order
        data = session.query(Post).order_by(Post.created_at.desc()).all()
        print("Connection succeeded: ")
        print(data)
    finally:
        session.close()
    return render_template("frontend/home.html", data = data)

@frontendBP.route("/aboutMe", methods = ["GET"])
def aboutMe():
    return render_template("frontend/aboutMe.html")

@frontendBP.route("/dashboard", methods = ["GET"])
def dashboard():
    form = SubmitPost()
    return render_template("frontend/dashboard.html", form = form)