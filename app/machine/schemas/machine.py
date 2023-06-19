from typing import Dict, List
from pydantic import BaseModel, Field


class GetMachineListResponseSchema(BaseModel):
    id: int = Field(..., description="Machine id")
    name: str = Field(..., description="Name")
    location: str = Field(..., description="location")
    email: str = Field(..., description="email")
    number: str = Field(..., description="number")
    enum: str = Field(..., description="enum")

    class Config:
        orm_mode = True
