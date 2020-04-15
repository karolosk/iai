from models import Base
from datetime import datetime, timezone
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
)
import logging


class BaseModel(Base):

    __abstract__ = True # declared to not be created by create_all

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), nullable=True)


    @classmethod
    def get_or_create(cls, session, **kwargs):
        instance = session.query(cls).filter_by(**kwargs).first()
        if instance:
            return instance
        else:
            instance = cls(**kwargs)
            session.add(instance)
            session.commit()
            return instance


    @classmethod
    def get_by_id(cls, session, id):
        return session.query(cls).filter(cls.id==id).first()

    
    @classmethod
    def bulk_create(cls, iterable, *args, **kwargs):
        # Logger Here
        # cls.before_bulk_create(iterable, *args, **kwargs)
        model_objs = []
        for data in iterable:
            if not isinstance(data, cls):
                data = cls(**data)
            model_objs.append(data)

        db.session.bulk_save_objects(model_objs)
        if kwargs.get('commit', True) is True:
            db.session.commit()
        # Logger Here
        cls.after_bulk_create(model_objs, *args, **kwargs)
        return model_objs
