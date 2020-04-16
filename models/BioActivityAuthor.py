from models.BaseModel import BaseModel
import datetime
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey
)
from sqlalchemy.orm import relationship, backref

class BioActivityAuthor(BaseModel):

    __tablename__  = 'bioActivity_author'
    
    bioActivity_id = Column(Integer, ForeignKey('bioActivity.id'))
    author_id = Column(Integer, ForeignKey('author.id'))
    

    bioActivity = relationship('BioActivity', backref=backref('bioActivity', cascade="all, delete-orphan"))
    auhtor = relationship('Author', backref=backref('author', cascade="all, delete-orphan"))