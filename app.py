import requests
from logger import log_conf # importing once to get the configuration
import logging
import pprint
from datetime import datetime
import settings
# from service.data_service import init_db
from service.etl_service import etl
log = logging.getLogger(__name__)


etl()
# pprint.pprint(response.json())

# for item in response.json()['bioactivities'][1:4]:

#     pprint.pprint(item)


# print(response.json()['meta']['next'])
# Base.metadata.drop_all(db.engine)

# init_db()
print("---------------------------------------------------------------------------------------------------------------------------------------")
