from flask import Blueprint

frontendBP = Blueprint(
    'frontendBP', 
    __name__,
    template_folder="templates",
    static_folder="static")