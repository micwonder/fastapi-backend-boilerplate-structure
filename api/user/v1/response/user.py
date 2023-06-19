from pydantic import BaseModel, Field


class LoginResponse(BaseModel):
    token: str = Field(..., description="Token")
    refresh_token: str = Field(..., description="Refresh token")

class ForgotPasswordResponse(BaseModel):
    reset_link: str = Field(..., description="Reset Link")

class ChangePasswordResponse(BaseModel):
    token: str = Field(..., description="Token")
    refresh_token: str = Field(..., description="Refresh token")

class SendVerifyCodeResponse(BaseModel):
    code: int = Field(..., description="Response Status")
    success: bool = Field(..., description="Success or not")
    token: str = Field(..., description="Token")
    request_id: str = Field(..., description="Request Id")