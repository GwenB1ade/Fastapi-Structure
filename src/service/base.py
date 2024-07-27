from database import get_db, session_creater


class BaseServices:
    
    model = None
    
    @classmethod
    def get_object_by_id(cls, id: int):
        with session_creater() as s:
            object = s.query(cls.model).filter_by(id = id).one()
            return object
    
    
    @classmethod
    def delete_object_by_id(cls, id: int):
        with session_creater() as s:
            s.query(cls.model).filter_by(id = id).delete()
            s.commit()
    
    