from models.BaseModel import BaseModel
import datetime
from sqlalchemy import (
    Column,
    String,
)

class Author(BaseModel):

    __tablename__ = 'author'

    name = Column(String(50), unique=True)                                   
    