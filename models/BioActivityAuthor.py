from models.BaseModel import BaseModel
import datetime
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey
)

class BioActivityAuthor(BaseModel):

    __tablename__  = 'bioActivity_author'
    
    bioActivity_id = Column(Integer, ForeignKey('bioActivity.id'))
    author_id = Column(Integer, ForeignKey('author.id'))
    