from fastapi import APIRouter

from api.user.v1.user import user_router as user_v1_router
from api.auth.auth import auth_router
from api.shop.shop import shop_router
from api.product.product import product_router

router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(user_v1_router, prefix="/user", tags=["User"])
router.include_router(shop_router, prefix="/shop", tags=["Shop"])
router.include_router(product_router, prefix="/product", tags=["Product"])

__all__ = ["router"]
