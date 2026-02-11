from flask import Blueprint, render_template
from blog.custom_forms import SubmitPost

backendBP = Blueprint(
    'backendBP', 
    __name__,
    url_prefix="/api")

@backendBP.route("/handle_post", methods=["POST"])
def handle_post():
    form = SubmitPost()
    if form.validate_on_submit():
        return "Form accepted"
    return render_template("frontend/dashboard.html", form = form)