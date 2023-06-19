# import re
# from typing import Optional, List

# # from sqlalchemy import select
# from api.product_translation.request.product_translation import CreateProductTranslationRequest
# from app.seller.models.seller import Seller

# from app.product_translation.models import ProductTranslation
# from app.user.models.user import User
from core.db import Transactional, session

# from core.utils.token_helper import TokenHelper


class ProductTranslationService:
    def __init__(self):
        ...

    @Transactional()
    async def create_product_translation(
        self,
        product_id: str,
        name: str,
        unit: int,
        description: int,
        lang: str,
    ) -> str:
        pass
