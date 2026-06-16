from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncConnection

from backend.app.db import analysis_repository
from backend.app.schema.analysis import (
    AnalysisRequest,
    RequirementResponse,
    UserType,
    Feature,
    ApiCandidate,
    DataModelField,
    DataModelCandidate,
    DevelopStep,
    EdgeCase,
    AnalysisResponse
)


async def create_analysis(analysis_request: AnalysisRequest, connection: AsyncConnection) -> RequirementResponse:
    project_id = analysis_request.project_id
    content = analysis_request.content

    row = await analysis_repository.create_requirement(project_id, content, connection)

    if row is None:
        raise HTTPException(status_code=500, detail="Failed to create requirement")

    # Forward analysis_result to LangGraph

    return RequirementResponse(**row)

async def get_analysis(analysis_id: int, connection: AsyncConnection) -> AnalysisResponse:
    row = await analysis_repository.get_analysis(analysis_id, connection)

    if row is None:
        raise HTTPException(status_code=404, detail="Analysis not found")

    return AnalysisResponse(**row)