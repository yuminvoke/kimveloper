from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncConnection

from backend.app.db.requirement_table import requirements
from backend.app.db.analysis_table import analysis_results


async def create_requirement(project_id: int, content: str, connection: AsyncConnection) -> dict:
    statement = (
        insert(requirements)
        .values(project_id=project_id, content=content)
        .returning(
            requirements.c.id.label("requirement_id"),
            requirements.c.project_id,
            requirements.c.content,
        )
    )

    result = await connection.execute(statement)
    await connection.commit()
    row = result.mappings().first()

    return dict(row) if row else None

async def get_analysis(analysis_id: int, connection: AsyncConnection) -> dict | None:
    statement = (
        select(
            requirements.c.project_id,
            analysis_results.c.requirement_id,
            analysis_results.c.summary,
            analysis_results.c.user_types,
            analysis_results.c.core_features,
            analysis_results.c.api_candidates,
            analysis_results.c.data_model_candidates,
            analysis_results.c.develop_steps,
            analysis_results.c.edge_cases,
            analysis_results.c.questions,
            analysis_results.c.model_name,
        )
        .join(
            requirements,
            analysis_results.c.requirement_id == requirements.c.id,
        )
        .where(analysis_results.c.id == analysis_id)
    )

    result = await connection.execute(statement)
    row = result.mappings().first()

    return dict(row) if row else None