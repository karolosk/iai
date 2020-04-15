from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import settings
import logging

log = logging.getLogger(__name__)

class Database():

    engine = create_engine(settings.DATABASE_URI, echo=True if settings.ENVIRONMENT=='dev' else False)
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        try:
            self.connection = self.engine.connect()
            log.info('Connection successfull at:' + settings.DATABASE_URI)
        except Exception as e:
            log.critical('Cannot connect to database. Exception:' + str(e))
    
    

    