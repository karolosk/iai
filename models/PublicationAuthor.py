from models.BaseModel import BaseModel
import datetime
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey
)
from sqlalchemy.orm import relationship, backref

class PublicationAuthor(BaseModel):

    __tablename__  = 'publication_author'
    
    publication_id = Column(Integer, ForeignKey('publication.id'))
    author_id = Column(Integer, ForeignKey('author.id'))
    

    publication = relationship('Publication', backref=backref('publication', cascade="all, delete-orphan"))
    author = relationship('Author', backref=backref('author', cascade="all, delete-orphan"))