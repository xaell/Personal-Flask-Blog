import os
from flask import Flask, Blueprint
from config import DevelopmentConfig, ProductionConfig, Config
from .frontend.frontend import frontendBP

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    #register blueprints
    app.register_blueprint(frontendBP)

    #config
    app.config.from_object(Config)

    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello World'
    
    return app