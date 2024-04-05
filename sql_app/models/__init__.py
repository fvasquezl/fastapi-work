from ..config.database import Base, engine

from . import itemModel, userModel

Base.metadata.create_all(bind=engine)
