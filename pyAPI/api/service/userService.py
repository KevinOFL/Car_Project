from sqlalchemy.orm import Session
from api.models import userModel
from api.schemas import userSchemas

# Query para consultar um usuário pelo ID
def get_user(db: Session, user_id: int):
    return db.query(userModel.User).filter(userModel.User.id == user_id).first()

#Query para consultar todos os usuários
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(userModel.User).offset(skip).limit(limit).all()

#Query para criar um novo usuário
def create_user(db: Session, user: userSchemas.user_view):
    db_user = userModel.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user