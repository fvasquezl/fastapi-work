from typing import List

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from sql_app.schemas import itemSchema

from sql_app.crud import itemCrud

item_router = APIRouter()


def get_db(request: Request):
    return request.state.db


@item_router.post("/users/{user_id}/items/", response_model=itemSchema.Item)
def create_item_for_user(
    user_id: int, item: itemSchema.ItemCreate, db: Session = Depends(get_db)
):
    return itemCrud.create_user_item(db=db, item=item, user_id=user_id)


@item_router.get("/items/", response_model=List[itemSchema.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = itemCrud.get_items(db, skip=skip, limit=limit)
    return items
