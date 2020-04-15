import sqlalchemy as db
import settings
import logging

log = logging.getLogger(__name__)

class Database():

    engine = db.create_engine(settings.DATABASE_URL, echo=True if settings.ENVIRONMENT=='dev' else False)
    def __init__(self):
        try:
            self.connection = self.engine.connect()
            log.info('Connection successfull at:' + settings.DATABASE_URL)
        except Exception as e:
            log.critical('Cannot connect to database. Error:' + e)
