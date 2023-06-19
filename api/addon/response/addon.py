from pydantic import BaseModel, Field


class CreateAddonResponse(BaseModel):
    name: str = Field(..., description="Name")