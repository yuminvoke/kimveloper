from sqlalchemy import Column, Identity, Integer, String, Table

from backend.app.db.connection import metadata


projects = Table(
    "projects",
    metadata,
    Column("id", Integer, Identity(always=True), primary_key=True),
    Column("name", String(255), nullable=False),
)