from pydantic import BaseModel, Field


class CreateAddonRequest(BaseModel):
    name: str = Field(..., description="Name")
    unique_identifier: str = Field(..., description="unique_identifier")
    version: int = Field(..., description="version")
    activated: int = Field(..., description="activated")
    image: str = Field(..., description="image")