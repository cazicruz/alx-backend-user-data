#!/usr/bin/env python3
"""
designing the auth module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    password = password.encode("utf-8") #converts password to bytes
    salt = bcrpyt.gensalt() #creates salt to hash password with
    hashedpwd = bcrypt.hashpw(password, salt)
    return hashedpwd
