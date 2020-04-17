from models import Base
from models.Author import Author
from models.Compound import Compound
from models.Gene import Gene
from models.Target import Target
from models.Bioactivity import BioActivity
from models.Publication import Publication
from models.PublicationAuthor import PublicationAuthor

from db.database import Database

import logging

log = logging.getLogger(__name__)
db = Database()

def init_db():

    '''
    Initialiazing Database structure and adds default records to the tables.
    If the tables and the records exists simply logs it
    '''

    # Base.metadata.drop_all(db.engine) # Uncomment to drop all tables and recreate them on next run

    Base.metadata.create_all(db.engine, checkfirst=True)
    create_default_records()


def create_default_records():

    if Author.get_by_id(-1) == None:
        log.info('Creating default Author')
        default_author=Author(id=-1, name='N/A')
        default_author.save()
    else: 
        log.info('Default author exists')

    if Gene.get_by_id(-1) == None:
        log.info('Creating default Gene')
        default_gene=Gene(id=-1, name='N/A')
        default_gene.save()
    else: 
        log.info('Default gene exists')

    if Target.get_by_id(-1) == None:
        log.info('Creating default Target')
        default_target=Target(id=-1, organism='N/A', pref_name='N/A')
        default_target.save()
    else: 
        log.info('Default gene exists')

    if Compound.get_by_id(-1) == None:
        log.info('Creating default Compound')
        default_compound=Compound(id=-1, name='N/A', concentration_value='N/A', concentration_value_unit='N/A')
        default_compound.save()
    else: 
        log.info('Default compound exists')

    if Publication.get_by_id(-1) == None:
        log.info('Creating default Publication')
        default_publication=Publication(id=-1, pubmed_id='N/A')
        default_publication.save()
    else: 
        log.info('Default publication exists')