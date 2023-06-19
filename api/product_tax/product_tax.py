from typing import List

from fastapi import APIRouter

from api.product_tax.request.product_tax import CreateProductTaxRequest
from api.product_tax.response.product_tax import CreateProductTaxResponse
from app.product_tax.schemas import ExceptionResponseSchema
from app.product_tax.services.product_tax import ProductTaxService


product_tax_router = APIRouter()


@product_tax_router.post(
    "/product_tax",
    response_model=CreateProductTaxResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def create_product_tax(request: CreateProductTaxRequest):
    result = await ProductTaxService().create_product_tax(**request.dict())
    return result
