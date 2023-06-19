from pydantic import BaseModel, Field


class CreateProductTaxResponse(BaseModel):
    name: str = Field(..., description="Name")