from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Text, DateTime, func

class Base(DeclarativeBase):
  pass

class Post(Base):
  __tablename__ = "posts"
  # Columns
  id = Column(Integer, autoincrement=True, primary_key=True)
  title = Column(String(50), nullable=False)
  body = Column(Text)
  mediaURL = Column(Text)
  created_at = Column(DateTime (timezone=True), server_default=func.now())
