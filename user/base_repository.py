from sqlalchemy.orm import Session
from typing import List, TypeVar, Generic
from fastapi import HTTPException, status

ModelType = TypeVar('ModelType')
CreateSchemaType = TypeVar('CreateSchemaType')
UpdateSchemaType = TypeVar('UpdateSchemaType')


class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: ModelType):
        self.model = model

    def get_obj_by_id(self, database: Session, obj_id: int) -> ModelType:
        return database.query(self.model).filter(self.model.id == obj_id).first()

    def get_all_objs(self, database: Session, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return database.query(self.model).offset(skip).limit(limit).all()

    def create_obj(self, database: Session, payload: CreateSchemaType) -> ModelType:
        database_obj = self.model(**payload.dict())
        database.add(database_obj)
        database.commit()
        database.refresh(database_obj)
        return database_obj

    def update(self, database: Session, obj_id: int, payload: UpdateSchemaType) -> ModelType:
        database_obj = database.query(self.model).filter(self.model.id == obj_id).first()
        if database_obj:
            for key, value in payload.dict().items():
                setattr(database_obj, key, value)
            database.commit()
            database.refresh(database_obj)
            return database_obj
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found")

    def delete(self, database: Session, obj_id: int):
        database_obj = database.query(self.model).filter(self.model.id == obj_id).first()
        if database_obj:
            database.delete(database_obj)
            database.commit()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found")
