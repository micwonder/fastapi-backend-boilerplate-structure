from pydantic import BaseModel, Field


class CreateProductStockResponse(BaseModel):
    name: str = Field(..., description="Name")