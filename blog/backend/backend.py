from flask import Blueprint

backendBP = Blueprint(
    'backendBP', 
    __name__,
    url_prefix="/api")

@backendBP.route("/handle_post", methods=["POST"])
def handle_post():
    return "posts should be handled here"