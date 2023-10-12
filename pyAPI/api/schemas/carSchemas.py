from pydantic import BaseModel
from typing import Optional

# Schema Base de um carro
class Car_Base(BaseModel):
    # id: int | None = None
    model: str
    brand: str
    year: int

    class Config:
        orm_mode = True

# Schema para ultilizar na criação de um carro
class Car_Create(Car_Base):
    owners: int
    value: float

    class Config:
        orm_mode = True

# Schema utilizado para visualização
class Car_Id(Car_Create):
    id: int

# Schema para efetuar uma alteração na quantidade de donos
class Car_Owners(Car_Create):
    owners: int

    class Config:
        orm_mode = True

# Schema para efetuar uma alteração no valor de um carro
class Car_Price(Car_Create):
    value: float

    class Config:
        orm_mode = True





