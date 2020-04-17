from models.BaseModel import BaseModel
from datetime import datetime, timezone
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.orm import relationship
import logging

log = logging.getLogger(__name__)

class BioActivity(BaseModel):

    __tablename__  = 'bioActivity'
    compound_id = Column(Integer, ForeignKey('compound.id'))
    target_id = Column(Integer, ForeignKey('target.id'))
    gene_id = Column(Integer, ForeignKey('gene.id'))
    publication_id = Column(Integer, ForeignKey('publication.id')) # pubmed_id
    native_id = Column(String(50)) # resource_uri last path param


    def exists(self):
        return self.session.query(BioActivity.id).filter_by(native_id=self.native_id).scalar() is not None


    @classmethod
    def bulk_update(cls, iterable):
        
        log.info('Initializing bulk update for: ' + str(len(iterable)) + ' ' + str(cls)+ ' models.')
        for bioactivity in iterable:
            try:
                bioactivity.update_at = datetime.now(timezone.utc)
                bioactivity_to_update = cls.session.query(cls).filter_by(native_id = bioactivity.native_id).first()
                bioactivity_to_update = bioactivity
                cls.session.commit()
            except Exception as e:
                log.error('Could not update Bioactivities: ' + str(e))
                cls.session.rollback()
            finally:
                cls.session.close()


                    
     