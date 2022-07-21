from pydantic import BaseModel, conint

class PetModel(BaseModel):
    name: str

class PetModelIn(PetModel):
    ...

class PetModelOut(PetModel):
    id: conint(ge=1)

    class Config:
        arm_mode: True

