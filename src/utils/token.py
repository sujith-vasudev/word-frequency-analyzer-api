import jwt
import datetime

from starlette.requests import Request

from config import SECRET_KEY
from exceptions import AccessExpired


def create_access_token(data: dict, algorithm: str = "HS256", expires_in_minutes: int = 30,
                        secret_key: str = SECRET_KEY):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_in_minutes)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt


def decode_token(token: str, algorithm: str = "HS256", secret_key: str = SECRET_KEY):
    decoded_info = {}
    try:
        decoded_info = jwt.decode(jwt=token, key=secret_key, algorithm=algorithm, options={"verify_signature": False})
    except jwt.ExpiredSignatureError:
        raise AccessExpired("Your Access has expired")
    except jwt.InvalidTokenError:
        print("Invalid token.")
        raise AccessExpired("Invalid Token")
    return decoded_info


def get_user(request: Request):
    token = request.headers.get("Authorization")
    return decode_token(token)
