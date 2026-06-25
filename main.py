from fastapi import FastAPI

from database.connection import Base, engine
from routers.auth_router import router

from models.user_model import User
from models.login_log_model import LoginLog

app = FastAPI(
    title="Authentication API"
)

Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Authentication API is Running"
    }