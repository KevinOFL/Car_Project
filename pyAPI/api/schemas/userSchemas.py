from pydantic import BaseModel
from typing import Optional, List
from api.models.carModel import Car
from datetime import datetime


# Schema base
class user_base(BaseModel):
    #id: Optional[int] = None
    name: str
    surname: str
    year: int

    class Config:
        from_attributes = True


# Schema de visualização de usuário
class user_view(user_base):
    id: Optional[int] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
