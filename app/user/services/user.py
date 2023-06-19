import re

from typing import List, Optional

from sqlalchemy import select, and_, update

from app.user.models import User
from app.user.schemas.user import LoginResponseSchema
from core.db import Transactional, session

from core.exceptions import (
    NotFoundException,
    CustomException,
    BadRequestException,
    ForbiddenException,
    MethodNotAllowedException,
)
from core.exceptions.base import DuplicateValueException
from core.utils.token_helper import TokenHelper
from utils.opt_sms import send_verify_code, validate_code

class UserService:
    def __init__(self):
        ...

    async def send_verify_code(
        self,
        phone: str,
        accept_language: Optional[str],
    ) -> dict :
        response = send_verify_code(phone=phone)
        return response
    
    async def validate_code(
        self,
        request_id: str,
        code: str,
        token: str,
        accept_language: Optional[str],
    ) -> dict :
        status = validate_code(id=request_id, code=code, token=token)
        if status == 200:
            return { "code": 200, "success": True, "message": "OK" }
        elif status == 400:
            raise BadRequestException
        elif status == 403:
            raise ForbiddenException
        elif status == 404:
            raise NotFoundException
        else:
            raise MethodNotAllowedException

    async def get_user_list(
        self,
        page: int,
        size: int,    # optional[int]
        order_by: str,
        desc: bool,
        accept_language: Optional[str],
    ) -> List[User]:
        try:
            print (accept_language)
            if size > 100:
                size = 100
            offset = page*size
            if desc:
                query = select(User).order_by(getattr(User, order_by).desc())
            else:
                query = select(User).order_by(getattr(User, order_by))
            query = query.offset(offset).limit(size)
            result = await session.execute(query)
            result = result.scalars().all()
            for val in result:
                if not val.email:
                    val.email = "----------Not set----------"
            return result
        except CustomException("Order_by__WRONG_FIELD_INPUT") as exception:
            raise exception

    @Transactional()
    async def create_user(
        self,
        email: str, 
        password: str, 
        password_confirmation: str, 
        name: str,
        phone: str,
        accept_language: Optional[str],
    ) -> dict:
        
        if password != password_confirmation:
            raise CustomException("Create_user__PASSWORD_NOT_MATCH")
        
        is_email_valid = re.match(r"\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b", email)
        if not is_email_valid:
            raise CustomException("Create_user__EMAIL_NOT_VALID")
        query = select(User).where(User.email == email)
        result = await session.execute(query)
        is_exist = result.scalars().first()
        if is_exist:
            raise DuplicateValueException("Create_user__THIS_EMAIL_EXIST")

        user = User(email=email, password=password, name=name, user_type="seller", phone=phone)
        session.add(user)
        return None
        

    async def is_admin(self, user_id: int) -> bool:
        result = await session.execute(
            select(User).where(User.id == user_id)
        )
        user = result.scalars().first()
        if not user:
            return False
        
        if user.user_type != "admin":
            return False
        
        return True

    async def login(
        self,
        email: str,
        password: str,
        accept_language: Optional[str],
    ) -> LoginResponseSchema:
        # if request_id == None and sms_token == None:
        #     response = await send_verify_code(phone=phone)
        #     response = LoginResponseSchema(
        #         request_id=response['request_id'],
        #         otp_token=response['token']
        #     )
        #     return response
        # response = await validate_code(request_id, code, sms_token)
        # if response != 200:
        #     raise OTPCodeNotMatchException
        print ("login request")
        result = await session.execute(
            select(User).where(and_(User.email == email, User.password == password))
        )
        print ("database accessed")
        user = result.scalars().first()
        if not user:
            raise CustomException("Login__EMAIL_OR_PASSWORD_INCORRECT")
        print ("user found")
        response = LoginResponseSchema(
            token=TokenHelper.encode(payload={"user_id": user.id}),
            refresh_token=TokenHelper.encode(payload={"sub": "refresh"}),
        )
        return response
    
    async def forgot_password(
        self,
        email: str,
        accept_language: Optional[str],
    ) -> dict:
        result = await session.execute(
            select(User).where(User.email == email)
        )
        user = result.scalars().first()
        if not user:
            raise NotFoundException("Forgot_password__USER_NOT_FOUND")
    
        # We need to send reset link to user through mail system
        return None
    
    @Transactional()
    async def change_password(
        self,
        email: str,
        password: str,
        new_password1: str,
        new_password2: str,
        accept_language: Optional[str],
    ) -> LoginResponseSchema:
        if new_password1 != new_password2:
            raise CustomException("Change_password__PASSWORD_NOT_MATCH")
        
        result = await session.execute(
            select(User).where(and_(User.email == email, User.password == password))
        )
        user = result.scalars().first()
        if not user:
            raise NotFoundException("Change_password__USER_NOT_FOUND")
        
        print ("update password")
        user.password = new_password1
        await session.commit()
        await session.refresh(user)

        response = LoginResponseSchema(
            token=TokenHelper.encode(payload={"user_id": user.id}),
            refresh_token=TokenHelper.encode(payload={"sub": "refresh"}),
        )
        return response
    
    @Transactional()
    async def delete(
        self,
        email: str,
        password: str,
        accept_language: Optional[str],
    ) -> None:
        result = await session.execute(
            select(User).where(and_(User.email == email, User.password == password))
        )
        user = result.scalars().first()
        if user == None:
            raise NotFoundException("Delete_USER_NOT_FOUND")
        
        await session.delete(user)
        await session.commit()
