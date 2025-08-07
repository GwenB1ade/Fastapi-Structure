import uuid
import json
from typing import Optional, Self, Sequence

from pydantic import BaseModel
from sqlalchemy import select, Column, Uuid
from sqlalchemy.ext.asyncio import AsyncAttrs, AsyncSession
from sqlalchemy.orm import DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    @property
    def fields(self) -> tuple:
        return tuple()

    def to_dict(self):
        _ = getattr
        return {
            f: _(self, f) if not isinstance(_(self, f), uuid.UUID) else str(_(self, f))
            for f in self.fields
        }

    def to_schema(self, schema: BaseModel):
        dict_data = self.to_dict()
        return schema.model_validate_json(json.dumps(dict_data))

    @classmethod
    async def get(cls, session: AsyncSession, **kwargs) -> Optional[Self]:
        result = await session.execute(select(cls).filter_by(**kwargs))
        result = result.scalar_one_or_none()
        if result is None:
            return None

        return result

    @classmethod
    async def list(cls, session: AsyncSession, **kwargs) -> Sequence[Self]:
        result = await session.execute(select(cls).filter_by(**kwargs))
        return result.scalars().all()

    @classmethod
    async def list_where(cls, session: AsyncSession, **kwargs) -> Sequence[Self]:
        result = await session.execute(select(cls).filter(**kwargs))
        return result.scalars().all()


class BaseId(Base):
    __abstract__ = True  # Указываем, что это абстрактный класс
    id = Column(Uuid, primary_key=True, index=True, default=uuid.uuid4)

    @property
    def fields(self):
        return super().fields + ("id",)
