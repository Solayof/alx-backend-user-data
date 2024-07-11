#!/usr/bin/env python3
"""
API session db module
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from os import getenv


class SessionDBAuth(SessionExpAuth):
    """ Session DB Auth """

    def create_session(self, user_id: str = None) -> str:
        """ Creates a Session ID for user_id """
        session_id = super().create_session(user_id)
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns User ID based on Session ID """

        if session_id is None or isinstance(session_id, str) is False:
            return None
        else:
            user = UserSession.get(session_id=session_id)
            return user.user_id

    def destroy_session(self, request=None):
        """ Deletes user session to logout """
        pass
