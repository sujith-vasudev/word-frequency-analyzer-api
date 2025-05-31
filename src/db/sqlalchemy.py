
from sqlalchemy import (Table, MetaData, Column, String, text,
                        DateTime, Boolean, ForeignKey)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import registry, relationship

from db.models.url_analyzer import UrlAnalyzer

from db.models.user import User

mapper_registry = registry()
metadata = MetaData()
DEFAULT_TIME = text('NOW()')

users = Table(
    "users",
    metadata,
    Column("user_id", String(255), nullable=False, primary_key=True),
    Column("username", String(255), nullable=False),
    Column("password", String(255), nullable=False),
    Column("is_active", Boolean, nullable=False, server_default=text('true')),
    Column("created_on", DateTime, server_default=DEFAULT_TIME),
    Column("modified_on", DateTime, server_default=DEFAULT_TIME),
    Column("created_by", String(255)),
    Column("modified_by", String(255)),
)

analyzer = Table(
    "analyzer",
    metadata,
    Column("analyzer_id", String(255), nullable=False, primary_key=True),
    Column("user_id", ForeignKey("users.user_id", ondelete="CASCADE")),
    Column("url", String(2048), nullable=False),
    Column("matches", JSONB, nullable=False),
    Column("created_on", DateTime, server_default=DEFAULT_TIME),
    Column("modified_on", DateTime, server_default=DEFAULT_TIME)
)


def bind_models():
    mapper_registry.map_imperatively(User, users, properties={
        "analysis_result": relationship(UrlAnalyzer,
                                        cascade="all, delete-orphan",
                                        order_by=analyzer.c.created_on.asc())
    })
    mapper_registry.map_imperatively(UrlAnalyzer, analyzer)
