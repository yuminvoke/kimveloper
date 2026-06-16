from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncConnection

from backend.app.db import project_repository
from backend.app.schema.project import ProjectResponse


async def create_project(project_name: str, connection: AsyncConnection) -> ProjectResponse:
    row = await project_repository.create_project(project_name, connection)

    if row is None:
        raise HTTPException(status_code=500, detail="Failed to create project")

    return ProjectResponse(**row)

async def get_project(project_id: int, connection: AsyncConnection) -> ProjectResponse:
    row = await project_repository.get_project(project_id, connection)

    if row is None:
        raise HTTPException(status_code=404, detail="Project not found")

    return ProjectResponse(**row)