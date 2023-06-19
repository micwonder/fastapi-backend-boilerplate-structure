from pydantic import BaseModel, Field


class CreateProductTaxRequest(BaseModel):
    name: str = Field(..., description="Name")
