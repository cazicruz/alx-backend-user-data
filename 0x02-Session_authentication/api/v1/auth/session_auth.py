#!/usr/bin/env python3
""" session_authentication"""
from .auth import Auth
import os
import uuid


class SessionAuth(Auth):
    """ implementation of session authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a session id for the user"""
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
