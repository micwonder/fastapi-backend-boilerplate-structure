from typing import List

from fastapi import APIRouter

from api.flash_deal_product.request.flash_deal_product import CreateFlashDealProductRequest
from api.flash_deal_product.response.flash_deal_product import CreateFlashDealProductResponse
from app.flash_deal_product.schemas import ExceptionResponseSchema
from app.flash_deal_product.services.flash_deal_product import FlashDealProductService


flash_deal_product_router = APIRouter()


@flash_deal_product_router.post(
    "/flash_deal_product",
    response_model=CreateFlashDealProductResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def create_flash_deal_product(request: CreateFlashDealProductRequest):
    result = await FlashDealProductService().create_flash_deal_product(**request.dict())
    return result
