from fastapi import Depends, HTTPException, FastAPI
from typing import Dict
from sqlalchemy.orm import Session
from api.schemas import carSchemas
from api.models import carModel
from api.service import carService
from _db.database import SessionLocal, engine

carModel.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency com yield
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Post criar carro
@app.post("/carCreate/", response_model=carSchemas.Car_Id)
def create_car(car: carSchemas.Car_Create, db: Session = Depends(get_db)):
    db_car = carService.create_car(db=db, car=car)
    return db_car

# Lista carros
@app.get("/cars/", response_model=list[carSchemas.Car_Id])
def car_views(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cars = carService.get_cars(db, skip=skip, limit=limit)
    return cars

# Mostra um carro pelo ID
@app.get("/cars/{car_id}", response_model=carSchemas.Car_Id)
def car_views_by_id(car_id: int, db: Session = Depends(get_db)):
    # verifica se o carro existe no DBe
    db_car = carService.get_car(db, car_id=car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="This Car Not Exist!")
    return db_car

# Deleta um carro pelo ID
@app.delete("/deleteCar/{car_id}")
def car_delete(car_id: int, db: Session = Depends(get_db)):
    # Verifica se o Id inserido existe no DB
    db_car = carService.get_car(db, car_id=car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="This Car Does Not Exist!")

    # Caso exista vai ser deletado
    carService.delete_car(db, car_id=car_id)
    return {"message": f"Car with ID {car_id} has been deleted"}

# Altera o valor e quantos donos de um carro
@app.put("/updateCar/{car_id}", response_model=carSchemas.Car_Id)
def car_update(car_id: int,updated_car: carSchemas.Car_Create, db: Session = Depends(get_db), ):
    db_car = carService.update_car(db, car_id, updated_car)

    if db_car is None:
        raise HTTPException(status_code=404, detail="This Car Does Not Exist!")
    return db_car


