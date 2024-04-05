from http.client import HTTPException
from typing import List

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from sql_app.schemas import userSchema

from sql_app.crud import userCrud

user_router = APIRouter()


def get_db(request: Request):
    return request.state.db


@user_router.post("/users/", response_model=userSchema.User)
def create_user(user: userSchema.UserCreate, db: Session = Depends(get_db)):
    db_user = userCrud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return userCrud.create_user(db=db, user=user)


@user_router.get("/users/", response_model=List[userSchema.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = userCrud.get_users(db, skip=skip, limit=limit)
    return users


@user_router.get("/users/{user_id}", response_model=userSchema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = userCrud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
