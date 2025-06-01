import uuid

from utils.password_hasher import get_hashed_password


class User:
    def __init__(self, username: str, password: str, created_by: str = "SYSTEM", is_active: bool = True):
        self.user_id: str = uuid.uuid4().hex
        self.username = username
        self.password = get_hashed_password(password)
        self.created_by = created_by
        self.is_active = is_active
        self.analysis_result = []

    def is_password_valid(self, password):
        return self.password == get_hashed_password(password)
