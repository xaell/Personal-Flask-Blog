import os
from flask import Flask
from blog.config import DevelopmentConfig, ProductionConfig, Config
from .frontend.frontend import frontendBP
from .backend.backend import backendBP
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
from sqlalchemy import text

db = SQLAlchemy()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    #register blueprints
    app.register_blueprint(frontendBP)
    app.register_blueprint(backendBP)

    #config
    app.config.from_object(Config)

    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)
    
    #database config
    db.init_app(app)

    # --- DB connection check on startup ---
    def check_db_connection():
        try:
            # Just execute a simple query
            with db.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print("Database connection OK")
        except OperationalError as e:
            print("Database connection failed:", e)
    
    with app.app_context():
        check_db_connection()
    
    return app