from backend.app.schema import AnalysisRequest, AnalysisResponse


class AnalysisService:
    @staticmethod
    async def create_analysis(request: AnalysisRequest) -> AnalysisResponse:
        return AnalysisResponse(
            summary=f"'{request.content}'에 대한 프로젝트 분석 결과입니다.",
            user_types=[],
            core_features=[],
            api_candidates=[],
            data_model_candidates=[],
            develop_steps=[],
            edge_cases=[],
            model_name="gpt-4.1-mini",
        )
