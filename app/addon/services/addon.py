# from typing import Optional, List

# from sqlalchemy import select
# from api.addon.request.addon import CreateAddonRequest
# from app.seller.models.seller import Seller

# from app.addon.models import Addon
# from app.user.models.user import User
from core.db import Transactional
# from core.exceptions import (
# )
# from core.utils.token_helper import TokenHelper


class AddonService:
    def __init__(self):
        ...

    @Transactional()
    async def create_addon(
        self,
        name: str,
        unique_identifier: str,
        version: int,
        activated: int,
        image: str,
    ) -> str:
        pass
