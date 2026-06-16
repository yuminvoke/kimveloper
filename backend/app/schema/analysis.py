from pydantic import BaseModel, Field


class AnalysisRequest(BaseModel):
    project_id: int = Field(gt=0)
    content: str = Field(min_length=10, max_length=5000)

class RequirementResponse(BaseModel):
    requirement_id: int = Field(gt=0)
    project_id: int = Field(gt=0)
    content: str

class UserType(BaseModel):
    name: str
    description: str

class Feature(BaseModel):
    name: str
    description: str

class ApiCandidate(BaseModel):
    method: str
    path: str
    description: str

class DataModelField(BaseModel):
    name: str
    type: str
    description: str

class DataModelCandidate(BaseModel):
    name: str
    description: str
    fields: list[DataModelField] = Field(default_factory=list)

class DevelopStep(BaseModel):
    step: int
    title: str
    description: str

class EdgeCase(BaseModel):
    case: str
    handling: str

class AnalysisResponse(BaseModel):
    project_id: int = Field(gt=0)
    requirement_id: int = Field(gt=0)
    summary: str
    user_types: list[UserType]
    core_features: list[Feature]
    api_candidates: list[ApiCandidate]
    data_model_candidates: list[DataModelCandidate]
    develop_steps: list[DevelopStep]
    edge_cases: list[EdgeCase]
    questions: list[str] = Field(default_factory=list)
    model_name: str