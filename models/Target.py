from models.BaseModel import BaseModel

from sqlalchemy import (
    Column,
    String
)
from sqlalchemy.orm import relationship


class Target(BaseModel):

    __tablename__  = 'target'

    organism = Column(String(50))                                   
    pref_name = Column(String(50))
    bioActivity = relationship('BioActivity')