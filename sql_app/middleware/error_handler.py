from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from sql_app.config.database import SessionLocal


class DBSessionMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        response = Response("Internal server error", status_code=500)
        try:
            request.state.db = SessionLocal()
            response = await call_next(request)
        finally:
            request.state.db.close()
        return response
