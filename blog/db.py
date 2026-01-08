from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import current_app

# Function to create a session to connect to postgres
def create_session():
    engine = create_engine(current_app.config["SQLALCHEMY_DATABASE_URI"], echo=True)
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    return SessionLocal()