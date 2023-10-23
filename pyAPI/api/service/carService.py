from sqlalchemy.orm import Session
from api.models import carModel
from api.schemas import carSchemas

# Query para consulta um carro pelo ID
def get_car(db: Session, car_id: int):
    return db.query(carModel.Car).filter(carModel.Car.id == car_id).first()

# Query de para consultar todos os carros
def get_cars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(carModel.Car).offset(skip).limit(limit).all()

# Query para adicionar um novo carro 
def create_car(db: Session, car: carSchemas.Car_Create, user_id: int):
# Utilizamos o Schema CarCreate que é baseado no Schema Base

    # Em vez de passar cada um dos argumentos de palavra-chave Car ler cada um deles do modelo Pydantic, estamos gerando um dict com os dados do modelo Pydantic com:
    db_car = carModel.Car(**car.dict(), buyer_id=user_id)
    # e então estamos passando os dict pares de chave-valores como argumentos de palavra-chave para oSQLAlquimia Car, com:
    #
    # Car(**car.dict())

    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

# Query para deletar um carro pelo ID
def delete_car(db: Session, car_id: int):
    car_to_delete = db.query(carModel.Car).filter(carModel.Car.id == car_id).first()

    if car_to_delete:
        db.delete(car_to_delete)
        db.commit()
        return True
    else:
        return False

# Query para atualizar um dado pelo ID
def update_car(db: Session, car_id: int, update_car: carSchemas.Car_Create):
    db_car = db.query(carModel.Car).filter(carModel.Car.id == car_id).first()

    if db_car:
        db_car.value = update_car.value
        db_car.owners = update_car.owners
        db.commit()
        db.refresh(db_car)
        return db_car
    else:
        return None


