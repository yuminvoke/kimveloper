from sqlalchemy import (
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    Identity,
    Index,
    Integer,
    Table,
    Text,
    text,
)

from backend.app.db.connection import metadata


requirements = Table(
    "requirements",
    metadata,
    Column("id", Integer, Identity(always=True), primary_key=True),
    Column(
        "project_id",
        Integer,
        ForeignKey("chat.projects.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column("content", Text, nullable=False),
    Column(
        "created_at",
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    ),
    CheckConstraint("char_length(content) BETWEEN 10 AND 5000"),
)

Index("index_requirements_project_id", requirements.c.project_id)