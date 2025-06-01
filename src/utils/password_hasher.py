import bcrypt

from config import PASSWORD_SALT


def get_hashed_password(password: str, salt: bytes = PASSWORD_SALT):
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, salt)
    return hashed.decode("utf-8")
