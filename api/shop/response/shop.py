from pydantic import BaseModel, Field


class CreateShopResponse(BaseModel):
    name: str = Field(..., description="Name")
    email: str = Field(..., description="Email")