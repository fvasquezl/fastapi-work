from sqlalchemy.orm import Session

from sql_app.schemas import itemSchema

from ..models import itemModel


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(itemModel.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: itemSchema.ItemCreate, user_id: int):
    db_item = itemModel.Item(**item.model_dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
