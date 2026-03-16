from flask import Blueprint, render_template, request
from blog.custom_forms import SubmitPost
from blog.db import create_session

backendBP = Blueprint(
    'backendBP', 
    __name__,
    url_prefix="/api")

@backendBP.route("/handle_post", methods=["POST"])
def handle_post():
    form = SubmitPost()

    print("Request method:", request.method)
    print("Form submitted?", form.is_submitted())
    print("Form valid?", form.validate())
    
    if form.validate_on_submit():
        #Use model and insert post into database here
        session = create_session()

        try:
            print("Form submitted!")
            print("Title:", form.title.data, flush=True)
            print("Content:", form.content.data, flush=True)

            # Or print all data as a dict
            print("All form data:", form.data, flush=True)
        except:
            print("Error")
        
        return "Form accepted"
    return render_template("frontend/makePost.html", form = form)