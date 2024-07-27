from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import JSON, String
from typing import Union, Optional

from database import Base


class UserModel(Base):
    __tablename__ = 'User'
    id: Mapped[int] = mapped_column(primary_key = True)
    username: Mapped[str] = mapped_column(String(length = 25), unique = True)
    password: Mapped[str] = mapped_column(String(length = 25))
    email: Mapped[str] = mapped_column(unique = True)
    
    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = password
        self.email = email
        