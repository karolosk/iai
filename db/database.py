import sqlalchemy as db
import settings

class Database():

    engine = db.create_engine(settings.DATABASE)
    def __init__(self):
        self.connection = self.engine.connect()
        print("DB Instance created")