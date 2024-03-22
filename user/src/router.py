from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from typing import List

from user import db
from . import schema
from .services import UserApiLogic
from .user_data_adapter import UserRepository

router = APIRouter(
    tags=["Users"],
    prefix='/api/v1/users'
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.User)
async def create_user_registration(payload: schema.UserCreate, database: Session = Depends(db.get_db)):
    return await UserApiLogic(UserRepository(database)).create_user(payload)


@router.get("/", response_model=List[schema.User])
async def get_all_users(skip: int = 0, limit: int = 100, database: Session = Depends(db.get_db)): #, current_user: schema.User = Depends(get_current_user)):
    return await UserApiLogic(UserRepository(database)).get_all_users(skip, limit)


@router.get("/{user_id}", response_model=schema.User)
async def get_user(user_id: int, database: Session = Depends(db.get_db)): #, current_user: schema.User = Depends(get_current_user)):
    return await UserApiLogic(UserRepository(database)).get_user_by_id(user_id)


@router.put("/{user_id}", response_model=schema.User)
async def update_user(user_id: int, payload: schema.UserUpdate, database: Session = Depends(db.get_db)):
    return await UserApiLogic(UserRepository(database)).update_user(user_id, payload)


@router.delete("/{user_id}", status_code = status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_user_by_id(user_id: int, database: Session = Depends(db.get_db)): #, current_user: schema.User = Depends(get_current_user)):
    return await UserApiLogic(UserRepository(database)).delete_user(user_id)
