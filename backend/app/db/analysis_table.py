from sqlalchemy import (
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    Identity,
    Index,
    Integer,
    String,
    Table,
    Text,
    text,
)
from sqlalchemy.dialects.postgresql import ARRAY, JSONB

from backend.app.db.connection import metadata


analysis_results = Table(
    "analysis_results",
    metadata,
    Column("id", Integer, Identity(always=True), primary_key=True),
    Column(
        "requirement_id",
        Integer,
        ForeignKey("chat.requirements.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column("summary", Text, nullable=False),
    Column(
        "user_types",
        JSONB,
        nullable=False,
        server_default=text("'[]'::jsonb"),
    ),
    Column(
        "core_features",
        JSONB,
        nullable=False,
        server_default=text("'[]'::jsonb"),
    ),
    Column(
        "api_candidates",
        JSONB,
        nullable=False,
        server_default=text("'[]'::jsonb"),
    ),
    Column(
        "data_model_candidates",
        JSONB,
        nullable=False,
        server_default=text("'[]'::jsonb"),
    ),
    Column(
        "develop_steps",
        JSONB,
        nullable=False,
        server_default=text("'[]'::jsonb"),
    ),
    Column(
        "edge_cases",
        JSONB,
        nullable=False,
        server_default=text("'[]'::jsonb"),
    ),
    Column(
        "questions",
        ARRAY(Text),
        nullable=False,
        server_default=text("ARRAY[]::TEXT[]"),
    ),
    Column("model_name", String(128), nullable=False),
    Column(
        "created_at",
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    ),
    CheckConstraint("jsonb_typeof(user_types) = 'array'"),
    CheckConstraint("jsonb_typeof(core_features) = 'array'"),
    CheckConstraint("jsonb_typeof(api_candidates) = 'array'"),
    CheckConstraint("jsonb_typeof(data_model_candidates) = 'array'"),
    CheckConstraint("jsonb_typeof(develop_steps) = 'array'"),
    CheckConstraint("jsonb_typeof(edge_cases) = 'array'"),
)

Index("index_analysis_results_requirement_id", analysis_results.c.requirement_id)