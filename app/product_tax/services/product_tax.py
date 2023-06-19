# import re
# from typing import Optional, List

# from sqlalchemy import or_, select, and_
# from api.product_tax.request.product_tax import CreateProductTaxRequest
# from app.seller.models.seller import Seller

# from app.product_tax.models import product_tax
# from app.user.models.user import User
from core.db import Transactional, session

# from core.utils.token_helper import TokenHelper


class ProductTaxService:
    def __init__(self):
        ...

    @Transactional()
    async def create_product_tax(
        self,
        product_id: int,
        tax_id: int,
        tax: float,
        tax_type: str,
    ) -> str:
        pass
