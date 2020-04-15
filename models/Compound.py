from models.BaseModel import BaseModel

from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import relationship


class Compound(BaseModel):

    __tablename__  = 'compound'

    name = Column(String(50))                                   
    concentration_value = Column(String(50))
    concentration_value_unit = Column(String(50))
    bioActivity = relationship('BioActivity')
