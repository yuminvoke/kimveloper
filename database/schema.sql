CREATE SCHEMA IF NOT EXISTS chat;

CREATE TABLE IF NOT EXISTS chat.projects (
	id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS chat.requirements (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    project_id INT NOT NULL REFERENCES chat.projects(id) ON DELETE CASCADE,

    content TEXT NOT NULL CHECK (char_length(content) BETWEEN 10 AND 5000),
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
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
    questions TEXT[] NOT NULL DEFAULT ARRAY[]::TEXT[],
    model_name VARCHAR(128) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS index_requirements_project_id
    ON chat.requirements(project_id);

CREATE INDEX IF NOT EXISTS index_analysis_results_requirement_id
    ON chat.analysis_results(requirement_id);