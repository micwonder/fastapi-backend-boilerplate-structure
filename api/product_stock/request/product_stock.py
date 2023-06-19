from pydantic import BaseModel, Field


class CreateProductStockRequest(BaseModel):
    name: str = Field(..., description="Name")
    