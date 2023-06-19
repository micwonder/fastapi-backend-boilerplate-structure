from pydantic import BaseModel, Field


class AddProductRequest(BaseModel):
    name: str = Field(..., description="Product Name")
    added_by: str = Field(..., description="Added by seller or admin")
    user_id: str = Field(..., description="Owner's id")
    price: float = Field(..., description="Price")


class UpdateProductRequest(BaseModel):
    id: int = Field(..., description="Product id")
    name: str = Field(..., description="Product Name")
    added_by: str = Field(..., description="Added by seller or admin")
    user_id: int = Field(..., description="Owner's id")
    price: float = Field(..., description="Price")
