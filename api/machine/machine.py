from typing import List, Optional

from fastapi import APIRouter, BackgroundTasks, Depends, Query, Request, UploadFile, Header

from app.machine.services import MachineService
from app.machine.schemas import (
    ExceptionResponseSchema,
    GetMachineListResponseSchema,
)
from .request.machine import (
    AddMachineRequest,
    UpdateMachineRequest,
)

# from core.fastapi.dependencies import (
#     PermissionDependency,
#     IsAuthenticated,
# )

import math
from datetime import datetime

machine_router = APIRouter()


############### Getting name, location, email, number, enum (active/not active), createat_at and edited_at ###############
@machine_router.post(
    "/create",
    response_model=None,
    responses={"400": {"model": ExceptionResponseSchema}},
    # dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def add_machine(
    request: AddMachineRequest,
    background_tasks: BackgroundTasks,
    accept_language: Optional[str] = Header(None),
):
    response = await MachineService().add_machine(**request.dict(), background_tasks=background_tasks, accept_language=accept_language)
    return response

############### update machine ###############
@machine_router.put(
    "/{id}",
    response_model=None,
    responses={"404": {"model": ExceptionResponseSchema}},
    # dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def update_product(
    id: int,
    request: UpdateMachineRequest,
    background_tasks: BackgroundTasks,
    accept_language: Optional[str] = Header(None),
):
    response = await MachineService().update_machine(id=id, **request.dict(), background_tasks=background_tasks, accept_language=accept_language)
    return response

@machine_router.get(
    "/get",
    response_model=List[GetMachineListResponseSchema],
    response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
    # dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def get_machine_list(
    id: int = Query(None, description="Machine Id"),
    email: str = Query(None, description="Email"),
    accept_language: Optional[str] = Header(None),
):
    ts = datetime.utcnow()
    response = await MachineService().get_machine_list(id=id, email=email, accept_language=accept_language)
    consumed = math.ceil((datetime.utcnow().timestamp()-ts.timestamp())*1000)
    response["consumed"] = f"Finished in {consumed}ms"
