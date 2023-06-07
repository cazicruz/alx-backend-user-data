#!/usr/bin/env python3
"""SQLAlchemy model named User for a database table named users (by using the mapping declaration of SQLAlchemy)"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
)

Base = declarative_base()


class User(db.Model):
    """
    definition of the class user
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False)
    hashed_password = db.Column(db.String(250), nullable=False)
    session_id = db.Column(db.String(250), nullable=True)
    reset_token =  db.Column(db.String(250), nullable=True)
