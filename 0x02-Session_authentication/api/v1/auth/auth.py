#!/usr/bin/env python3
""" auth class"""
from flask import request
from typing import List, TypeVar
import os


class Auth():
    """Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require auth
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
        return True
    
    def authorization_header(self, request=None) -> str:
        """Authorization header
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')
    
    def current_user(self, request=None) -> str:
        """
        Returns a User instance from information from a request object
        """
        return None

    def session_cookie(self, request=None):
        """
        returns a cookie value from request
        """
        if request is None:
            return None
        session_name = os.getenv(SESSION_NAME, _my_session_id)
        return request.cookies.get(session_name)
