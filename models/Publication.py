from models.BaseModel import BaseModel

from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import relationship


class Publication(BaseModel):

    __tablename__  = 'publication'

    pubmed_id = Column(String(50), unique=True)                                   
    
    authors = relationship('Author', secondary='publication_author')


    @classmethod
    def get_or_create(cls, pubmed_id, authors):
        
        '''
        Overwritting to handled the authors relationship
        '''        
        try:
            instance = cls.session.query(cls).filter_by(pubmed_id=pubmed_id).first()
            if instance:
                return instance
            else:
                instance = cls(pubmed_id=pubmed_id, authors=authors)
                cls.session.add(instance)
                cls.session.commit()
                return instance
        except Exception as e:
            log.error('Couid not save: ' + str(cls) + ': ' + str(e))
            cls.session.rollback()
        finally:
            cls.session.close