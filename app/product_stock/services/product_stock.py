# import re
# from typing import Optional, List

# from sqlalchemy import select
# from api.product_stock.request.product_stock import CreateProductStockRequest
# from app.seller.models.seller import Seller

# from app.product_stock.models import ProductStock
# from app.user.models.user import User
from core.db import Transactional, session

# from core.utils.token_helper import TokenHelper


class ProductStockService:
    def __init__(self):
        ...

    @Transactional()
    async def create_product_stock(
        self,
        product_id: int,
        variant: str,
        sku: str,
        price: float,
        qty: int,
        image: str,
    ) -> str:
        pass
