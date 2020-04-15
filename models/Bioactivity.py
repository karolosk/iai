from models.BaseModel import BaseModel
import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

class BioActivity(BaseModel):

    __tablename__  = 'bioActivity'
    compound_id = Column(Integer, ForeignKey('compound.id'))
    target_id = Column(Integer, ForeignKey('target.id'))
    gene_id = Column(Integer, ForeignKey('gene.id'))
    publication = Column(String(50)) # pubmed_id
    native_id = Column(String(50)) # resource_uri last path param

