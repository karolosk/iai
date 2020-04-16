from models.BaseModel import BaseModel
import datetime
from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import relationship

class Author(BaseModel):

    __tablename__ = 'author'

    name = Column(String(150), unique=True)                                   
    bioActivity = relationship('BioActivity', secondary='bioActivity_author')