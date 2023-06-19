from pydantic import BaseModel, Field


class CreateShopRequest(BaseModel):
    name: str = Field(..., description="Name")
    email: str = Field(..., description="Email")
    password: str = Field(..., description="Password")
    password_confirmation: str = Field(..., description="Password Confirmation")
    shopname: str = Field(..., description="Shop Name")
    address: str = Field(..., description="Address")
    country: str = Field(..., description="Country")
    city: str = Field(..., description="City")
    area: str = Field(..., description="Area")
    postal_code: str = Field(..., description="Postal Code")
    dial_code: str = Field(..., description="Dial Code")
    phone: str = Field(..., description="Phone")