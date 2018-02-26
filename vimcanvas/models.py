from .database import Model

from sqlalchemy import (Column, Integer, 
                        String, Boolean)

class Canvas(Model):
    """
    Model representing a saved canvas session.
    """
    __tablename__ = 'canvases'
    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    active = Column(Boolean())
    file_url = Column(String(200))

class User(Model):
    """
    Model representing a user.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(128))
    is_admin = Column(Boolean())