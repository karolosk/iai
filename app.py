import requests
from logger import log_conf # importing once to get the configuration
import logging
import pprint
from datetime import datetime
import settings
from models import Base, Author, Bioactivity, Compound, Target, Gene, BioActivityAuthor
from db.database import Database
from service.data_service import data_retrieve, hello

log = logging.getLogger(__name__)
    
# Setting verify to False due to SSL implementation on provider's end
# Used only for the assesement context since SSL seems to be expired
# https://www.ssllabs.com/ssltest/analyze.html?d=drugtargetcommons.fimm.fi&latest
response = requests.get(settings.BASE_ENDPOINT + settings.API_ENDPOINT, verify=False)

# pprint.pprint(response.json())

for item in response.json()['bioactivities'][1:2]:

    pprint.pprint(item)
    # log.info(item['authors'])


# print(response.json()['meta']['next'])
db = Database()
# Base.metadata.drop_all(db.engine)


if __name__ == '__main__':
    Base.metadata.create_all(db.engine, checkfirst=True)
    
