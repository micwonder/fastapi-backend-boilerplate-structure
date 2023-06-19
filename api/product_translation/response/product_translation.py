from pydantic import BaseModel, Field


class CreateProductTranslationResponse(BaseModel):
    name: str = Field(..., description="Name")