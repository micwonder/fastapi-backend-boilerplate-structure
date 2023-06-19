from pydantic import BaseModel, Field


class CreateFlashDealProductResponse(BaseModel):
    name: str = Field(..., description="Name")