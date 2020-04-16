from models import Base
from datetime import datetime, timezone
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
)
import logging
from db.database import Database

log = logging.getLogger(__name__)


class BaseModel(Base):

    __abstract__ = True # declared to not be created by create_all

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), nullable=True)

    session = Database.session


    def save(self, commit=True):
        self.session.add(self)
        if commit:
            try:
                self.session.commit()
            except Exception as e:
                self.session.rollback()
                log.error(str(e))
            finally:
                self.session.close()


     

    @classmethod
    def get_or_create(cls, **kwargs):
        
        try:
            instance = cls.session.query(cls).filter_by(**kwargs).first()
            if instance:
                return instance
            else:
                instance = cls(**kwargs)
                cls.session.add(instance)
                cls.session.commit()
                return instance
        except Exception as e:
            log.error('Couid not save: ' + str(cls) + ': ' + str(e))
            cls.session.rollback()
        finally:
            cls.session.close

    @classmethod
    def get_by_id(cls, id):
        return cls.session.query(cls).filter(cls.id==id).first()


    @classmethod
    def get_by_attribute(cls, **kwargs):
        return cls.session.query(cls).filter_by(**kwargs).first()

    
    @classmethod
    def bulk_save(cls, iterable, *args, **kwargs):

        log.info('Initializing bulk save for: ' + str(len(iterable)) + ' ' + str(cls)+ ' models.')
        try:
            model_objs = []
            for data in iterable:
                if not isinstance(data, cls):
                    data = cls(**data)
                model_objs.append(data)

            cls.session.bulk_save_objects(model_objs)
            cls.session.commit()
            log.info('Bulk save for: ' + str(len(iterable)) + ' ' + str(cls)+ ' models.')
            return model_objs
        except Exception as e:
            log.error('Could not save models: ' + str(e))
            cls.session.rollback()
        finally:
            cls.session.close()