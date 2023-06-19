from typing import List, Optional

from fastapi import APIRouter, Depends, Query, Request, UploadFile, Header

from app.product.schemas import (
    ExceptionResponseSchema,
    AddProductRequestSchema,
    GetProductListResponseSchema,
    AddProductResponseSchema,
    UpdateProductRequestSchema
)
from app.product.services import ProductService
from core.fastapi.dependencies import (
    PermissionDependency,
    IsAdmin,
)
from starlette.authentication import requires

from core.fastapi.dependencies.permission import IsAuthenticated

import boto3

product_router = APIRouter()

############### get product list ###############
@product_router.get(
    "",
    response_model=List[GetProductListResponseSchema],
    response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def get_product_list(
    page: int = Query(0, description="Page Number"),
    size: int = Query(10, description="Size"),
    order_by: str = Query("added_by", description="Sort by spec field"),
    desc: bool = Query(False, description="Descending order"),
    accept_language: Optional[str] = Header(None),
):
    return await ProductService().get_product_list(page=page, size=size, order_by=order_by, desc=desc, accept_language=accept_language)

############### get product by id ###############
@product_router.get(
    "/{id}",
    response_model=GetProductListResponseSchema,
    response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def get_product(
    id: int,
    accept_language: Optional[str] = Header(None),
):
    return await ProductService().get_product(id, accept_language=accept_language)

############### add product ###############
@product_router.post(
    "/",
    response_model=AddProductResponseSchema,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def add_product(
    request: Request,
    body: AddProductRequestSchema,
    accept_language: Optional[str] = Header(None),
):
    await ProductService().add_product(**body.dict(), user_id=request.user.id, accept_language=accept_language)
    return {"name": body.name}

############### update product ###############
@product_router.put(
    "/{id}",
    response_model=None,
    responses={"404": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def update_product(
    id: int,
    body: UpdateProductRequestSchema,
    request: Request,
    accept_language: Optional[str] = Header(None),
):
    token = await ProductService().update_product(id=id, **body.dict(), user_id=request.user.id, accept_language=accept_language)
    return {"status": "success"}

############### delete product by id ###############
@product_router.delete(
    "/{id}",
    response_model=None,
    responses={"404": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def remove(
    id: int,
    accept_language: Optional[str] = Header(None),
):
    await ProductService().remove(id=id, accept_language=accept_language)
    return {"status": "success"}

############### update product image file to s3 ###############
@product_router.post(
    "/product-image",
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def upload_image_file_to_s3(
    file: UploadFile):
    s3_client = boto3.client('s3')
    s3_client.put_object(Body=file, Bucket='my-bucket',
                         Key=f"upload/{file.filename}", ContentType=file.content_type)
    url = s3_client.generate_presigned_url('get_object', Params={
                                           'Bucket': 'my-bucket', 'Key': f'upload/{file.filename}', })
    return url
