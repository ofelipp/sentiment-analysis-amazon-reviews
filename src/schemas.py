from uuid import uuid1
from pydantic import BaseModel, UUID1, Field

class ModelInput(BaseModel):
    text: str
    model_config = {"extra": "forbid"}


class ModelPrediction(BaseModel):
    input_text: str
    value: int
    category: str
    description: str


class ModelResponse(BaseModel):
    id: UUID1 =  Field(default_factory=uuid1)
    input_text: str
    category: str
    description: str