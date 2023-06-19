from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    email: str = Field(..., description="Email")
    password: str = Field(..., description="Password")

class ForgotPasswordRequest(BaseModel):
    email: str = Field(..., description="Email")

class ChangePasswordRequest(BaseModel):
    email: str = Field(..., description="Email")
    password: str = Field(..., description="Password")
    new_password1: str = Field(..., description="New Password1")
    new_password2: str = Field(..., description="New Password2")

class DeleteRequest(BaseModel):
    email: str = Field(..., description="Email")
    password: str = Field(..., description="Password")

class SendVerifyCodeRequest(BaseModel):
    phone: str = Field(..., description="Phone number")

class ValidateCodeRequest(BaseModel):
    request_id: str = Field(..., description="RequestId")
    code: str = Field(..., description="SMS Code")
    token: str = Field(..., description="SMS Token")