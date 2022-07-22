from pydantic import BaseModel, conint


class PetModel(BaseModel):
    name: str



class PetModelIn(PetModel):
    breed_id = int


class PetModelOut(PetModel):
    id: conint(ge=1)

    class Config:
        arm_mode: True


class BreedModel(BaseModel):
    name: str


class BreedModelIn(BreedModel):
    ...


class BreedModelOut(BreedModel):
    id: conint(ge=1)
