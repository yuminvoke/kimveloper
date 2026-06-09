CREATE SCHEMA IF NOT EXISTS chat;

CREATE TABLE IF NOT EXISTS chat.requirements (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS chat.analysis_results (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    requirement_id INT NOT NULL REFERENCES chat.requirements(id) ON DELETE CASCADE,

    summary TEXT NOT NULL,
    user_types JSONB NOT NULL DEFAULT '[]'::jsonb,
    features JSONB NOT NULL DEFAULT '[]'::jsonb,
    apis JSONB NOT NULL DEFAULT '[]'::jsonb,
    data_models JSONB NOT NULL DEFAULT '[]'::jsonb,
    develop_order JSONB NOT NULL DEFAULT '[]'::jsonb,
    edge_cases JSONB NOT NULL DEFAULT '[]'::jsonb,
    model_name VARCHAR(128),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);