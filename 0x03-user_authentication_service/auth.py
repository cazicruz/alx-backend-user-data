#!/usr/bin/env python3
"""
designing the auth module
"""
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
