from pydantic import BaseModel, Field
from datetime import datetime


class LoginRequest(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    password: str = Field(min_length=6, max_length=20)


class LoginLogResponse(BaseModel):
    log_id: int
    user_id: int
    login_time: datetime

    class Config:
        from_attributes = True