#!/usr/bin/env pyhton3
""" session_authentication"""
from .auth import Auth
import os


class SessionAuth(Auth):
    def __init__(self):
        super().__init__()


 use_session_auth = os.getenv("USE_SESSION_AUTH", False)
    if use_session_auth:
        # Use SessionAuth
        auth = SessionAuth()
    else:
        # Use default Auth
        auth = Auth()
