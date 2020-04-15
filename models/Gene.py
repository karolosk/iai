from models.BaseModel import BaseModel

from sqlalchemy import (
    Column,
    String
)
from sqlalchemy.orm import relationship


class Gene(BaseModel):

    __tablename__  = 'gene'

    name = Column(String(50))                                   
    bioActivity = relationship('BioActivity')