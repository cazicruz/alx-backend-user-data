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


    def user_id_for_session_id(self, session_id: str = None) -> str:
        """retrieves the value (user id) stored in 
        user_id_by_session_id with the key (session id)
        and returns it
        """
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)
