from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncConnection

from backend.app.service import project_service
from backend.app.service import analysis_service
from backend.app.schema.project import ProjectRequest, ProjectResponse
from backend.app.schema.analysis import AnalysisRequest, AnalysisResponse
from backend.app.db.connection import get_db_connection


app = FastAPI()

@app.post("/project/create", response_model=ProjectResponse)
async def create_project(
        project: ProjectRequest,
        db: AsyncConnection = Depends(get_db_connection)
) -> ProjectResponse:
    response = await project_service.create_project(project, db)
    return response

@app.get("/project/{project_id}")
async def get_project(
        project_id: int,
        db: AsyncConnection = Depends(get_db_connection)
) -> ProjectResponse:
    response = await project_service.get_project(project_id, db)
    return response

@app.get("/analysis/{analysis_id}")
async def get_analysis(
        analysis_id: int,
        db: AsyncConnection = Depends(get_db_connection)
) -> AnalysisResponse:
    response = await analysis_service.get_analysis(analysis_id=analysis_id, connection=db)
    return response