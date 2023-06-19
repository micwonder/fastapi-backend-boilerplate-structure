from pydantic import BaseModel, Field


class AddMachineRequest(BaseModel):
    name: str = Field(..., description="Machine name")
    location: str = Field(..., description="Machine location")
    email: str = Field(..., description="Machine email")
    number: str = Field(..., description="Machine number")
    enum: bool = Field(..., description="Machine enum")

class UpdateMachineRequest(BaseModel):
    name: str = Field(..., description="Machine Name")
    location: str = Field(..., description="Machine location")
