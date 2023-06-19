from typing import List

from fastapi import APIRouter

from api.addon.request.addon import CreateAddonRequest
from api.addon.response.addon import CreateAddonResponse
from app.addon.schemas import ExceptionResponseSchema
from app.addon.services.addon import AddonService


addon_router = APIRouter()


@addon_router.post(
    "/addon",
    response_model=CreateAddonResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def create_addon(request: CreateAddonRequest):
    result = await AddonService().create_addon(**request.dict())
    return result
