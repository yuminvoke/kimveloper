from pydantic import BaseModel, Field


class ProjectRequest(BaseModel):
    name: str = Field(min_length=1, max_length=255)

class ProjectResponse(BaseModel):
    id: int
    name: str = Field(min_length=1, max_length=255)