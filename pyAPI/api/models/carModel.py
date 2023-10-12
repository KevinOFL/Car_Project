from sqlalchemy import Column, Integer, String, Float
from _db.database import Base

class Car(Base):
    __tablename__ = "cars"

    # Aqui declamaros cada coluna do DB e seus atributos
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    model = Column(String, nullable=False, index=True)
    brand = Column(String, nullable=False, index=True)
    year = Column(Integer, nullable=False)
    value = Column(Float, nullable=False)
    owners = Column(Integer, nullable=False)

