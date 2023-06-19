from pydantic import BaseModel, Field


class GetUserListResponseSchema(BaseModel):
    id: int = Field(..., description="ID")
    email: str = Field(..., description="Email")
    name: str = Field(..., description="Name")

    class Config:
        orm_mode = True


class CreateUserRequestSchema(BaseModel):
    email: str = Field(..., description="Email")
    password: str = Field(..., description="Password")
    password_confirmation: str = Field(..., description="Password Confirmation")
    name: str = Field(..., description="Name")
    phone: str = Field(..., desription="Phone Number")


class CreateUserResponseSchema(BaseModel):
    email: str = Field(..., description="Email")
    name: str = Field(..., description="Name")

    class Config:
        orm_mode = True


class LoginResponseSchema(BaseModel):
    token: str = Field(..., description="Token")
    refresh_token: str = Field(..., description="Refresh token")
