from typing import List

from fastapi import APIRouter

from api.shop.request.shop import CreateShopRequest
from api.shop.response.shop import CreateShopResponse
from app.shop.schemas import ExceptionResponseSchema
from app.shop.services.shop import ShopService


shop_router = APIRouter()


@shop_router.post(
    "",
    response_model=CreateShopResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def create_shop(request: CreateShopRequest):
    result = await ShopService().create_shop(**request.dict())
    return result
