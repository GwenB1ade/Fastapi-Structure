from pydantic import BaseModel, EmailStr
from typing import Union, Optional


class UserSchemas(BaseModel):
    id: Optional[int]
    username: str
    password: Optional[str]
    email: EmailStr
    

    