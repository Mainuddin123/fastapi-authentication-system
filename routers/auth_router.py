from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db

from schemas.user_schema import UserCreate, UserResponse
from schemas.login_schema import LoginRequest, LoginLogResponse

from services.auth_service import (
    register_user,
    login_user,
    get_all_users,
    get_all_login_logs
)

router = APIRouter()


@router.post("/register")
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    return register_user(user_data, db)


@router.post("/login")
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    return login_user(login_data, db)


@router.get("/users", response_model=list[UserResponse])
def users(db: Session = Depends(get_db)):
    return get_all_users(db)


@router.get("/login-logs", response_model=list[LoginLogResponse])
def login_logs(db: Session = Depends(get_db)):
    return get_all_login_logs(db)