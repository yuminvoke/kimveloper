CREATE SCHEMA IF NOT EXISTS chat;

CREATE TABLE IF NOT EXISTS chat.requirements (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    content TEXT NOT NULL CHECK (char_length(content) BETWEEN 10 AND 5000),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS chat.analysis_results (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    requirement_id INT NOT NULL REFERENCES chat.requirements(id) ON DELETE CASCADE,

    summary TEXT NOT NULL,
    user_types JSONB NOT NULL DEFAULT '[]'::jsonb CHECK (jsonb_typeof(user_types) = 'array'),
    core_features JSONB NOT NULL DEFAULT '[]'::jsonb CHECK (jsonb_typeof(core_features) = 'array'),
    api_candidates JSONB NOT NULL DEFAULT '[]'::jsonb CHECK (jsonb_typeof(api_candidates) = 'array'),
    data_model_candidates JSONB NOT NULL DEFAULT '[]'::jsonb CHECK (jsonb_typeof(data_model_candidates) = 'array'),
    develop_steps JSONB NOT NULL DEFAULT '[]'::jsonb CHECK (jsonb_typeof(develop_steps) = 'array'),
    edge_cases JSONB NOT NULL DEFAULT '[]'::jsonb CHECK (jsonb_typeof(edge_cases) = 'array'),
    model_name VARCHAR(128) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);