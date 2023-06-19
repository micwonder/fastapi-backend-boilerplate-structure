from typing import List

from fastapi import APIRouter

from api.product_stock.request.product_stock import CreateProductStockRequest
from api.product_stock.response.product_stock import CreateProductStockResponse
from app.product_stock.schemas import ExceptionResponseSchema
from app.product_stock.services.product_stock import ProductStockService


product_stock_router = APIRouter()


@product_stock_router.post(
    "/product_stock",
    response_model=CreateProductStockResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def create_product_stock(request: CreateProductStockRequest):
    result = await ProductStockService().create_product_stock(**request.dict())
    return result
