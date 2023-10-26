from pydantic import BaseModel
from typing import Optional, List

# Schema Base
class Car_Base(BaseModel):
    #id: Optional[int] = None
    model: str 
    brand: str 
    year: int 

    class Config:
        from_attributes = True


# Schema para utilização na criação de um carro
class Car_Create(Car_Base):
    owners: int
    value: float
    sold: Optional[bool] = False

    class Config:
        from_attributes = True
        

    
# Schema utilizado para visualização
class Car_view(Car_Create):
    id: int
    buyer_id: Optional[int] = None

    class Config:
        from_attributes = True
        