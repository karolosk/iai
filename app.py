import requests
import settings
from models import Base, Author, Bioactivity, Compound, Target, Gene, BioActivityAuthor
from db.database import Database

# Setting verify to False due to SSL implementation on provider's end
# Used only for the assesement context since SSL seems to be expired
# https://www.ssllabs.com/ssltest/analyze.html?d=drugtargetcommons.fimm.fi&latest

# response = requests.get(settings.BASE_ENDPOINT + settings.API_ENDPOINT, verify=False)

# print(response.json()['meta']['next'])
db = Database()
Base.metadata.drop_all(db.engine)
print(settings.DATABASE_URL)
Base.metadata.create_all(db.engine, checkfirst=True)
