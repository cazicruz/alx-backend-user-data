#!/usr/bin/env python3
"""SQLAlchemy model named User for a database table named users (by using the mapping declaration of SQLAlchemy)."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECFRET_KEY'] = 'hardtoguess'
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'database.db')
db = SQLAlchemy(app)


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
