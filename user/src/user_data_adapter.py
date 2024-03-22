from sqlalchemy.orm import Session
from typing import Optional, List

from user.base_repository import BaseRepository
from . import schema
from . import models


class UserRepository(BaseRepository):
    """ Repository for managing users. """
    def __init__(self, database: Session):
        super().__init__(models.User)
        self.database = database

    def get_user_by_email(self, email: str) -> Optional[schema.User]:
        return self.database.query(self.model).filter(self.model.email == email).first()

    def get_user_by_id(self, user_id: int) -> Optional[schema.User]:
        return super().get_obj_by_id(self.database, user_id)

    def get_all_users(self, skip: int = 0, limit: int = 100) -> List[schema.User]:
        return super().get_all_objs(self.database, skip, limit)

    def create_user(self, user: schema.UserCreate) -> schema.User:
        return super().create_obj(self.database, user)

    def update_user(self, user_id: int, payload: schema.UserUpdate) -> schema.User:
        return super().update(self.database, user_id, payload)

    def delete_user(self, user_id: int):
        return super().delete(self.database, user_id)
