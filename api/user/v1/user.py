from typing import List, Optional

from fastapi import APIRouter, Depends, Query, Header

from api.user.v1.request.user import (
    ChangePasswordRequest,
    DeleteRequest,
    ForgotPasswordRequest,
    LoginRequest,
    SendVerifyCodeRequest,
    ValidateCodeRequest,
)
from api.user.v1.response.user import (
    ChangePasswordResponse,
    ForgotPasswordResponse,
    SendVerifyCodeResponse,
)
from app.user.schemas import (
    ExceptionResponseSchema,
    GetUserListResponseSchema,
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    LoginResponseSchema
)
from app.user.services import UserService
from core.fastapi.dependencies import (
    PermissionDependency,
    IsAdmin,
    IsAuthenticated,
)

user_router = APIRouter()

############### get user list ###############
@user_router.get(
    "",
    response_model=List[GetUserListResponseSchema],
    response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAdmin]))],
)
async def get_user_list(
    page: int = Query(0, description="Page Number"),    
    size: int = Query(10, description="Size"),
    order_by: str = Query("name", description="Sort by spec field"),
    desc: bool = Query(False, description="Descending order"),
    accept_language: Optional[str] = Header(None),
):
    return await UserService().get_user_list(page=page, size=size, order_by=order_by, desc=desc, accept_language=accept_language)

############### create user ###############
@user_router.post(
    "",
    response_model=CreateUserResponseSchema,
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def create_user(
    request: CreateUserRequestSchema,
    accept_language: Optional[str] = Header(None),
):
    await UserService().create_user(**request.dict(), accept_language=accept_language)
    return {"email": request.email, "name": request.name}

############### login ###############
@user_router.post(
    "/login",
    response_model=LoginResponseSchema,
    responses={"404": {"model": ExceptionResponseSchema}},
)
async def login(
    request: LoginRequest,
    accept_language: Optional[str] = Header(None),
):
    token = await UserService().login(**request.dict(), accept_language=accept_language)
    return {"token": token.token, "refresh_token": token.refresh_token}

############### forgot password ###############
@user_router.post(
    "/forgot-password",
    response_model=ForgotPasswordResponse,
    responses={"404": {"model": ExceptionResponseSchema}},
)
async def forgot_password(
    request: ForgotPasswordRequest,
    accept_language: Optional[str] = Header(None),
):
    reset_link = await UserService().forgot_password(**request.dict(), accept_language=accept_language)
    return {"reset_link": reset_link}

############### update user ###############
@user_router.put(
    "/change-password",
    response_model=ChangePasswordResponse,
    responses={"404": {"model": ExceptionResponseSchema}},
)
async def change_password(
    request: ChangePasswordRequest,
    accept_language: Optional[str] = Header(None),
):
    token = await UserService().change_password(email=request.email, password=request.password, new_password1=request.new_password1, new_password2=request.new_password2, accept_language=accept_language)
    return {"token": token.token, "refresh_token": token.refresh_token}

############### delete ###############
@user_router.delete(
    "",
    response_model=None,
    responses={"404": {"model": ExceptionResponseSchema}},
)
async def delete(
    request: DeleteRequest,
    accept_language: Optional[str] = Header(None),
):
    await UserService().delete(email=request.email, password=request.password, accept_language=accept_language)
    return {"status": "success"}

############### Phone Verify ###############
@user_router.post(
    "/send-verify-code",
    response_model=SendVerifyCodeResponse,
    responses={"404": {"model": ExceptionResponseSchema}},
    #dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def send_verify_code(
    request: SendVerifyCodeRequest,
    accept_language: Optional[str] = Header(None),
):
    response = await UserService().send_verify_code(phone=request.phone, accept_language=accept_language)
    return { "code": 200, "success": True, **response}

@user_router.post(
    "/validate-code",
    response_model=None,
    responses={"404": {"model": ExceptionResponseSchema}},
    # dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def validate_code(
    request: ValidateCodeRequest,
    accept_language: Optional[str] = Header(None),
):
    success = await UserService().validate_code(request_id=request.request_id, code=request.code, token=request.token, accept_language=accept_language)
    return success

