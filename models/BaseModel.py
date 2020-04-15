from models import Base
from datetime import datetime, timezone
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
)


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
