import sqlalchemy as db
import settings

class Database():

    engine = db.create_engine(settings.DATABASE_URL, echo=True if settings.ENVIRONMENT=='dev' else False)
    def __init__(self):
        self.connection = self.engine.connect()
