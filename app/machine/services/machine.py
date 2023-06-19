import json
import random
import string
from typing import List, Optional
from fastapi import BackgroundTasks

# Migrate to other file

from sqlalchemy import and_, select

from app.machine.models import Machine
# from core.exceptions import CustomException, ForbiddenException, NotFoundException
from core.db import Transactional, session
from utils.validator import validation


class MachineService:
    def __init__(self):
        ...

    async def get_machine_list(
        self,
    ) -> List[Machine]:
        ...

    @Transactional()
    async def add_machine(
        self,
        name: str,
        location: str,
        email: str,
        number: str,
        enum: bool,
        background_tasks: BackgroundTasks,
        accept_language: Optional[str],
    ) -> dict:
        validation(email=email)
        background_tasks.add_task(self.task_add_machine, name, location, email, number, enum)
        response = { "success": True, "message": "Machine has been updated successfully" }
        return response
    
    @Transactional()
    async def update_machine(
        self,
        id: int,
        name: str,
        location: str,
        background_tasks: BackgroundTasks,
        accept_language: Optional[str],
    ) -> dict:
        background_tasks.add_task(self.task_update_machine, name, location)
        response = { "success": True, "message": "Machine has been updated successfully" }
        return response
    
    async def task_add_machine(
        self,
        name: str,
        location: str,
        email: str,
        number: str,
        enum: bool,
    ):
        try:
            print ("Machine has been added successfully")
        except Exception as e:
            print (e.args[0])

    async def task_update_machine(
        self,
        name: str,
        location: str,
    ):
        try:
            print ("Machine has been updated successfully")
        except Exception as e:
            print (e.args[0])