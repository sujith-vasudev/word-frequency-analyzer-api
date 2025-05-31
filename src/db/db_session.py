
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DB_CLIENT, DB_PASS, DB_USER, DB_HOST, DB_PORT, DB_NAME


def get_db_session():
    app_engine = create_engine(
        f"{DB_CLIENT}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
        pool_size=300,
        max_overflow=332,
        pool_recycle=100,
        echo_pool=True,
        pool_timeout=300,
        pool_pre_ping=True
    )
    return sessionmaker(autoflush=False, bind=app_engine)()
