from models import Base
from models.Author import Author
from models.Compound import Compound
from models.BioActivityAuthor import BioActivityAuthor
from models.Gene import Gene
from models.Target import Target
from models.Bioactivity import BioActivity

from db.database import Database

import logging

log = logging.getLogger(__name__)
db = Database()

def store_data(results):
    
    bioActivities_to_insert = []
    bioActivities_to_update = []
    for result in results:

        bioActivity_to_save = BioActivity()
        bioActivity_to_save.authors = manage_authors(result['authors'])
        bioActivity_to_save.compound_id = manage_compound(dict((k, result[k]) for k in ['compound_concentration_value', 'compound_concentration_value_unit', 'compound_name'] if k in result))
        bioActivity_to_save.gene_id = manage_gene(result['gene_name'])
        bioActivity_to_save.publication = result['pubmed_id']
        bioActivity_to_save.target_id = manage_target(dict((k, result[k]) for k in ['pref_name', 'organism'] if k in result))
        bioActivity_to_save.native_id = retrieve_native_id(result['resource_uri'])
        
        if bioActivity_to_save.exists():
            bioActivities_to_update.append(bioActivity_to_save)
        else:
            bioActivities_to_insert.append(bioActivity_to_save)
        
    BioActivity.bulk_update(bioActivities_to_update)
    BioActivity.bulk_save(bioActivities_to_insert)    
    
        
    
def retrieve_native_id(resource_uri):
    
    '''
    Note: Based on assumption
    Assuming that the provider uses bioactivity's native id to provide
    the endpoint in the response, we get that and store it to our data store
    to avoid duplicate values
    '''
    id_from_url = resource_uri.split('/')
    return id_from_url[-2]


def manage_authors(authors):

    '''
    Converts the string with authors to a list of strings.
    Each item in the list is saved in the database or returned if exists already
    If there are no authors for the bioactivity returns default record
    '''
    bioActivity_authors = []
    if authors:
        
        for author in authors.split(','):
            author.replace('"', '')
            bioActivity_author = Author.get_or_create(name=author.strip())
            bioActivity_authors.append(bioActivity_author)
        return bioActivity_authors 

    default_author = Author.get_by_id(-1)    
    bioActivity_authors.append(default_author)
    return bioActivity_authors

def manage_compound(compound):

    '''
    For compound we are checking if all the values in the dict are None.
    If that is true then return default record
    Else return the record if exists or create it
    '''
    if all(value is None for value in compound.values()):
        compound_to_return = Compound.get_by_id(-1)
        return compound_to_return.id
    compound_to_return = Compound.get_or_create(name=compound['compound_name'], concentration_value=compound['compound_concentration_value'], 
                                  concentration_value_unit=compound['compound_concentration_value_unit'])
    return compound_to_return.id
    
def manage_gene(gene_name):

    '''
    Similar to the rest, if gene name does not exist return default,
    Else return the record if exists or create it
    '''
    if gene_name is None:
        gene_to_return = Gene.get_by_id(-1)
        return gene_to_return.id
    gene_to_return = Gene.get_or_create(name=gene_name)
    return gene_to_return.id

def manage_target(target):
    
    '''
    Similar to the rest, if gene name does not exist return default,
    Else return the record if exists or create it
    '''
    if all(value is None for value in target.values()):
        target_to_return = Target.get_by_id(-1)
        return target_to_return.id
    target_to_return = Target.get_or_create(organism=compound['target_organism'], pref_name=target['target_pref_name'])
    return target_to_return.id

def init_db():

    '''
    Initialiazing Database structure and adds default records to the tables.
    If the tables and the records exists simply logs it
    '''

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