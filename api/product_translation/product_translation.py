from typing import List

from fastapi import APIRouter

from api.product_translation.request.product_translation import CreateProductTranslationRequest
from api.product_translation.response.product_translation import CreateProductTranslationResponse
from app.product_translation.schemas import ExceptionResponseSchema
from app.product_translation.services.product_translation import ProductTranslationService


product_translation_router = APIRouter()


@product_translation_router.post(
    "/product_translation",
    response_model=CreateProductTranslationResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def create_product_translation(request: CreateProductTranslationRequest):
    result = await ProductTranslationService().create_product_translation(**request.dict())
    return result
