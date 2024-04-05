from sql_app.middleware.error_handler import DBSessionMiddleware
from fastapi import FastAPI
from sql_app.routes.userRouter import user_router
from sql_app.routes.itemRouter import item_router


app = FastAPI()
app.add_middleware(DBSessionMiddleware)
app.include_router(user_router)
app.include_router(item_router)
