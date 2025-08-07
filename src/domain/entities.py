from dataclasses import dataclass


@dataclass
class BaseEntity:
    uid: str


@dataclass
class UserEntity(BaseEntity):
    username: str
    email: str
