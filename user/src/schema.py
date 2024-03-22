from typing import Optional

from pydantic import BaseModel, constr, EmailStr, ConfigDict


class UserCreate(BaseModel):
    first_name: constr(min_length=2, max_length=50)
    last_name: constr(min_length=2, max_length=50)
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    first_name: constr(min_length=2, max_length=50)
    last_name: constr(min_length=2, max_length=50)
    email: EmailStr

