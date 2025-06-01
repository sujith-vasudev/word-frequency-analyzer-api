import os

DB_CLIENT = os.environ.get("DB_CLIENT", "postgresql+psycopg2")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASS = os.environ.get("DB_PASS", "root")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_NAME = os.environ.get("DB_NAME", "demo")
SECRET_KEY = os.environ.get("SECRET_KEY", "SECRET_KEY")
PASSWORD_SALT = os.environ.get("PASSWORD_SALT", b'$2b$12$dETsd4Az4kmHd4Plf8WeLOhHsv5k0ZtVRILphMAv.LArX4tU5H6eK')