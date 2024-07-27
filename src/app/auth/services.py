from service.base import BaseServices, get_db, session_creater

from . import models
from .schemas import UserSchemas

class UserServices(BaseServices):
    
    model = models.UserModel
    
    @classmethod
    def create_user(cls, data: UserSchemas):
        with session_creater() as s:
            try:
                user = cls.model(
                    username = data.username,
                    email = data.email,
                    password = data.password
                )
            
            except Exception as exc:
                print(exc)
                return False
            
            s.add(user)
            s.commit()
            
            return True
            