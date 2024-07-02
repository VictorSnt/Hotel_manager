# std
from typing import Callable, Dict, List, Optional, Type, Union
# ext
from fastapi import HTTPException, status
from sqlmodel import select
#app
from api.database.db_connector import SessionMaker, AsyncSession
from api.model.base import BaseModel


class BaseRepository:
    """
    Base repository class providing CRUD operations.
    """

    def __init__(self, session_maker: Type[SessionMaker], model: Type[BaseModel]) -> None:
        self.session_maker = session_maker
        self.model = model

    async def find(self, obj_id: Optional[int] = None) -> Union[BaseModel, List[BaseModel]]:
        async with self.session_maker.get_session_async() as session:
            if obj_id:
                statement = select(self.model).where(
                    (self.model.id == obj_id) & (self.model.active == True)
                )
                result = await session.exec(statement)
                response = result.one_or_none()
            else:
                statement = select(self.model).where(self.model.active == True)
                result = await session.exec(statement)
                response = list(result.all())

            if not response:
                raise HTTPException(status_code=404, detail=f"No {self.model.__name__} found")
            return response

    async def create(self, data: dict) -> BaseModel:
        new_obj = self.model(**data)
        async with self.session_maker.get_session_async() as session:
            session.add(new_obj)
            await session.commit()
            await session.refresh(new_obj)
            return new_obj

    async def find_and_update(
            self, obj_id: int, updated_obj: Dict,
            usecase: Union[Callable, None] = None
        ) -> BaseModel:

        async with self.session_maker.get_session_async() as session:
            obj = await self.__get_obj(obj_id, session)
            if not obj:
                raise HTTPException(status_code=404, detail=f"No {self.model.__name__} found")
            if usecase:
                obj = usecase(obj, updated_obj)
            else:
                for key, value in updated_obj.items():
                    setattr(obj, key, value)

            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj

    async def find_and_delete(self, obj_id: int) -> Dict:
        async with self.session_maker.get_session_async() as session:
            obj = await self.__get_obj(obj_id, session)
            setattr(obj, 'active', False)
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return {"detail": f"{self.model.__name__} deleted successfully"}

    async def __get_obj(self, obj_id: int, session: AsyncSession):
        query = select(self.model).where(
            (self.model.id == obj_id) & (self.model.active == True)
        )
        result = await session.exec(query)
        obj = result.first()
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No {self.model.__name__} found"
            )
        return obj
