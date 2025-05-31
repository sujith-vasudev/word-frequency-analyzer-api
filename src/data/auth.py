from typing import TYPE_CHECKING

from db.models.user import User
from exceptions import ValidationError

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


class UserData:

    @staticmethod
    def validate_username(session: 'Session', username: str):
        user_obj: User | None = session.query(User).filter_by(username=username).first()
        return user_obj

    @staticmethod
    def create_user(session: 'Session', username: str, password: str) -> User:
        user_obj = UserData.validate_username(session=session, username=username)
        if user_obj: raise ValidationError(f"User '{username}' already exists")
        user_obj: User = User(username=username, password=password)
        session.add(user_obj)
        return user_obj
