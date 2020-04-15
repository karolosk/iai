from models import Base
from datetime import datetime, timezone
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
)


class BaseModel(Base):

    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), nullable=True)


    def before_save(self, *args, **kwargs):
        pass

    def after_save(self, *args, **kwargs):
        pass
