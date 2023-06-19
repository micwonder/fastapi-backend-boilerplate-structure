import re
# from typing import Optional, List

from sqlalchemy import select
# from api.shop.request.shop import CreateShopRequest
from app.seller.models.seller import Seller

from app.shop.models import Shop
from app.user.models.user import User
from core.db import Transactional, session
from core.exceptions import CustomException, DuplicateValueException, NotFoundException

# from core.utils.token_helper import TokenHelper


class ShopService:
    def __init__(self):
        ...

    @Transactional()
    async def create_shop(
        self,
        name: str,
        email: str,
        password: str,
        password_confirmation: str,
        shopname: str,
        address: str,
        country: str,
        city: str,
        area: str,
        postal_code: str,
        dial_code: str,
        phone: str,
    ) -> None:
        if password != password_confirmation:
            raise CustomException("Create_shop__PASSWORD_NOT_MATCH")
        
        is_email_valid = re.match(r"\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b", email)
        if not is_email_valid:
            raise CustomException("Create_shop__EMAIL_NOT_VALID")
        
        query = select(User).where(User.email == email)
        result = await session.execute(query)
        is_exist = result.scalars().first()
        if is_exist:
            raise DuplicateValueException("This email is exist")

        user = User(email=email, password=password, name=name, user_type="seller")
        session.add(user)

        query = select(User).where(User.email == email)
        result = await session.execute(query)
        user = result.scalars().first()

        if not user:
            raise NotFoundException("Create_shop__USER_NOT_FOUND")

        seller = Seller(user_id=user.id)
        session.add(seller)

        query = select(Shop).where(Shop.user_id == user.id)
        result = await session.execute(query)
        is_exist = result.scalars().first()
        if not is_exist:
            shop = Shop(
                user_id=user.id,
                name=shopname,
                country=country,
                city=city,
                postal_code=postal_code,
                area=area,
                address=address,
                phone=f'+{dial_code}{phone}',
                slug=re.sub('\s+', '-', shopname) + '-' + '123')
            
            session.add(shop)

        return {
            "name": name,
            "email": email,
        }
