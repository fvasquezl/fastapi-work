from sqlalchemy.orm import Session

from sql_app.schemas import userSchema

from ..models import userModel


def get_user(db: Session, user_id: int):
    return db.query(userModel.User).filter(userModel.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(userModel.User).filter(userModel.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(userModel.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: userSchema.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = userModel.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
