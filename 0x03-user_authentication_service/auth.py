#!/usr/bin/env python3
"""
designing the auth module
"""
from db import DB
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    taskes a string argument and encrypt it with bcrypt
    steps:
        encode the arg into a utf-8 string
        then generates the salt of that argument with bcrypt.gensalt()
        then hash or encrypt the paasword with bcrypt.hashpw method-
        which takes two args the word to hash and the salt to hash it with
    """
    password = password.encode("utf-8") #converts password to bytes
    salt = bcrpyt.gensalt() #creates salt to hash password with
    hashedpwd = bcrypt.hashpw(password, salt)
    return hashedpwd

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> dict:
        """ a class to register new users with the methods from DB
        and raise error if user already exist"""
        try:
            usr = self_db.find_user_by(email=email)
        except NoResultFound:
            hashpwd = _hash_password(password)
            user = self._db.add_user(email, hashpwd)
            return user
        raise ValueError(f"user {email} already exists")
