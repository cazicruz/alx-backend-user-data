#!/usr/bin/env pyhton3
""" session_authentication"""
from .auth import Auth
import os


class SessionAuth(Auth):
    """ implementation of session authentication"""
    def __init__(self):
        super().__init__()
