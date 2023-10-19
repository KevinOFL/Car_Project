from sqlalchemy.orm import Session
from api.models import userModel
from api.schemas import userSchemas


def get_user(db: Session, user_id: int):
    return db.query(userModel.User).filter(userModel.User.id == user_id).first()

