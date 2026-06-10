from fastapi import FastAPI

from backend.app.schema import AnalysisRequest, AnalysisResponse
from backend.app.service import AnalysisService


app = FastAPI()

@app.post("/analysis", response_model=AnalysisResponse)
async def request_analysis(request: AnalysisRequest) -> AnalysisResponse:
    response = await AnalysisService.create_analysis(request)
    return response