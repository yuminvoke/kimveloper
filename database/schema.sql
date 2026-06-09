CREATE SCHEMA IF NOT EXISTS chat;

CREATE TABLE IF NOT EXISTS chat.requirements (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS chat.analysis_results (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    summary TEXT NOT NULL,
    user_types JSONB NOT NULL,
    features JSONB NOT NULL,
    api JSONB NOT NULL,
    data_models JSONB NOT NULL,
    develop_order JSONB NOT NULL,
    edge_cases JSONB NOT NULL,
    model_name VARCHAR(128),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    requirement_id INT REFERENCES chat.requirements(id)
);