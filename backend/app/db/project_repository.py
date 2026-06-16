from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncConnection

from backend.app.db.project_table import projects


async def create_project(project_name: str, connection: AsyncConnection) -> dict | None :
    statement = (
        insert(projects)
        .values(name=project_name)
        .returning(projects.c.id, projects.c.name)
    )

    result = await connection.execute(statement)
    await connection.commit()
    row = result.mappings().first()

    return dict(row) if row else None

async def get_project(project_id: int, connection: AsyncConnection) -> dict | None :
    statement = (
        select(projects.c.id, projects.c.name)
        .where(projects.c.id == project_id)
    )

    result = await connection.execute(statement)
    row = result.mappings().first()

    return dict(row) if row else None