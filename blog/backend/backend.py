from flask import Blueprint

backendBP = Blueprint(
    'backendBP', 
    __name__,
    url_prefix="/api")

@backendBP.route("/getPosts", methods=["GET"])
def getPosts():
    return "posts should be returned here"