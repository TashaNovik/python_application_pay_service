from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any


# Абстракция, которая удаляет из сервисной логики всю реализацию по общению с базой данных
class AbstractRepo(ABC):
    def add_new(self): ...
    def update(self): ...
    def get_all(self): ...


class BaseRepo(ABC):
    @abstractmethod
    async def get_all(self, session: AsyncSession) -> list[Any]: ...

    @abstractmethod
    async def get_by_id(self, id_: int, session: AsyncSession) -> Any: ...

    @abstractmethod
    async def add(self, batch: Any, session: AsyncSession) -> None: ...
