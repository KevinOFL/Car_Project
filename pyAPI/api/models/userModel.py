import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from _db.database import Base

class User(Base):
    __tablename__ = "users"

    #Declaração das collum do DB
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    surname = Column(String, index=True, nullable=False)
    year = Column(Integer, index=True,  nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relacionamento entre car e user
    car_purchased = relationship("Car", back_populates="buyer")
