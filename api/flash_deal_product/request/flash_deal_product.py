from pydantic import BaseModel, Field


class CreateFlashDealProductRequest(BaseModel):
    name: str = Field(..., description="Name")
