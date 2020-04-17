import requests
from logger import log_conf # importing once to get the configuration
import logging
import pprint
from datetime import datetime
import settings
from service.database_service import init_db
from service.fetch_service import etl


# init_db()
etl()

