#!/usr/bin/env python3
""" basic http authentication class"""
from .auth import Auth
from flask import request
from typing import List, TypeVar
import base64

from moddels.user import User


class BasicAuth(Auth):
    """BasicAuth class
    """
    def __init__(self) -> None:
        """init
        """
        pass


    def extract_base64_authorization_header(self,
                                            authorization_header:
                                            str) -> str:
        """extract base64 authorization header
        """
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]


    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """decode base64 authorization header
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            sample_string_bytes = base64.b64decode(base64_bytes)
            sample_string = sample_string_bytes.decode('utf-8')
            return sample_string
        except Exception:
            return None


    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """extract user credentials
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) != str:
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        user = decoded_base64_authorization_header.split(':', 1)[0]
        password = decoded_base64_authorization_header.split(':', 1)[1]
        return (user, password)

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """user object from credentials
        """
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None
        try:
            user = User()
            user.email = user_email
            user._password = user_pwd
            return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user
        """
        if request is None:
            return None
        if self.authorization_header(request) is None:
            return None
