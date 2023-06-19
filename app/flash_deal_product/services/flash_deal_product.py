# import re
# from typing import Optional, List

# from sqlalchemy import select
# from api.flash_deal_product.request.flash_deal_product import CreateFlashDealProductRequest
# from app.seller.models.seller import Seller

# from app.flash_deal_product.models import FlashDealProduct
# from app.user.models.user import User
from core.db import Transactional, session

# from core.utils.token_helper import TokenHelper


class FlashDealProductService:
    def __init__(self):
        ...

    @Transactional()
    async def create_flash_deal_product(
        self,
        flash_deal_id: int,
        product_id: int,
        discount: float,
        discount_type: str,
        image: str,
    ) -> str:
        pass
