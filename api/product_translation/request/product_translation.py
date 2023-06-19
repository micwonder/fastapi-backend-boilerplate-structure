from pydantic import BaseModel, Field


class CreateProductTranslationRequest(BaseModel):
    name: str = Field(..., description="Name")
