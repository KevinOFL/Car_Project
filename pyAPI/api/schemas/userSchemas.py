from pydantic import BaseModel
from typing import Optional
from api.models.carModel import Car


# Schema base
class user_base(BaseModel):
    name: str
    surname: str
    year: int

    class Config:
        orm_mode = True


# Schema de visualização de usuário
class user_view(user_base):
    id: int
    is_active: Optional[bool] = True
    created_at: str
    cars = list[Car] = []

    class Config:
        orm_mode = True
