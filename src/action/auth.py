from typing import TYPE_CHECKING

from data.auth import UserData
from exceptions import ValidationError

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


class UserAction:

    def __init__(self, session: 'Session'):
        self.session = session

    def validate_username(self, username):
        user_obj = UserData.validate_username(session=self.session, username=username)
        if user_obj is None: raise ValidationError(f"Invalid User '{username}'")
        return user_obj

    def validate_user(self, username, password):
        user_obj = UserData.validate_username(session=self.session, username=username)
        if user_obj is None: raise ValidationError(f"Invalid User '{username}'")
        if not user_obj.is_password_valid(password=password):
            raise ValidationError("Invalid credentials")

    def create_user(self, username: str, password: str):
        UserData.validate_username(session=self.session, username=username)
        user_obj = UserData.create_user(session=self.session, username=username, password=password)
        return user_obj
