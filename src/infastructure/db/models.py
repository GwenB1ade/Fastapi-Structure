from .base import BaseId
from sqlalchemy.orm import Mapped, mapped_column


class UserModel(BaseId):
    __tablename__ = "User"
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)

    @property
    def fields(self) -> tuple[str, ...]:  # pyright: ignore
        return super().fields + (
            "username",
            "email",
        )
