from fastapi import HTTPException, status
from typing import List

from . import schema
from .user_data_adapter import UserRepository


class UserApiLogic:
    """ This class implements the Order endpoints business logic layer. """
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def create_user(self, payload: schema.UserCreate) -> schema.User:
        user = self.repository.get_user_by_email(payload.email)

        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The user with that email already exists in the system."
            )

        return self.repository.create_user(payload)

    async def get_all_users(self, skip=0, limit=100) -> List[schema.User]:
        return self.repository.get_all_users(skip, limit)

    async def get_user_by_id(self, user_id: int) -> schema.User:
        user = self.repository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found."
            )
        return user

    async def get_user_by_email(self, email: str) -> schema.User:
        user = self.repository.get_user_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found."
            )
        return user

    async def update_user(self, user_id: int, payload: schema.UserUpdate) -> schema.User:
        try:
            return self.repository.update_user(user_id, payload)
        except HTTPException as e:
            if e.status_code == status.HTTP_404_NOT_FOUND:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found."
                )
            else:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="An error occurs"
                )

    async def delete_user(self, user_id: int):
        try:
            return self.repository.delete_user(user_id)
        except HTTPException as e:
            if e.status_code == status.HTTP_404_NOT_FOUND:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found."
                )
            else:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="An error occurs"
                )
