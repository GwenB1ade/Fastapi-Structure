from typing import Generic, Optional, TypeVar
from abc import ABC, abstractmethod
from .entities import BaseEntity, UserEntity

Entity = TypeVar("Entity", bound=BaseEntity)


class IBaseRepository(ABC, Generic[Entity]):
    @abstractmethod
    async def get_one(self, id: str | int) -> Optional[Entity]:
        pass

    @abstractmethod
    async def add(self, entity: Entity) -> None:
        pass

    @abstractmethod
    async def delete(self, id: str | int) -> None:
        pass


class IUserRepository(IBaseRepository[UserEntity]): ...
