from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models.user_model import User
from models.login_log_model import LoginLog

from schemas.user_schema import UserCreate
from schemas.login_schema import LoginRequest

from utils.hash import hash_password, verify_password
from schemas.user_schema import UserCreate, UserUpdate

def register_user(user_data: UserCreate, db: Session):

    existing_user = db.query(User).filter(
        User.username == user_data.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    existing_email = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    new_user = User(
        username=user_data.username,
        email=user_data.email,
        password=hash_password(user_data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id,
        "username": new_user.username
    }


def login_user(login_data: LoginRequest, db: Session):

    user = db.query(User).filter(
        User.username == login_data.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    if not verify_password(login_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    log = LoginLog(user_id=user.id)

    db.add(log)
    db.commit()
    db.refresh(log)

    return {
        "message": "Login successful",
        "user_id": user.id,
        "username": user.username
    }


def get_all_users(db: Session):
    return db.query(User).all()


def get_all_login_logs(db: Session):
    return db.query(LoginLog).all()

def update_user(user_id: int, user_data: UserUpdate, db: Session):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    user.username = user_data.username
    user.email = user_data.email
    user.password = hash_password(user_data.password)

    db.commit()
    db.refresh(user)

    return {
        "message": "Profile updated successfully"
    }