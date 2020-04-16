import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(override=True)

BASE_ENDPOINT = os.getenv('DRUGTARGETCOMMONS_BASE_ENDPOINT')
API_ENDPOINT = os.getenv('DRUGTARGETCOMMONS_API_ENDPOINT')
DATABASE_URI = os.getenv('DATABASE_URI')
ENVIRONMENT = os.getenv('ENV')
LOG_LEVEL = os.getenv('LOG_LEVEL')
LOG_FILE = 'logging_' + str(datetime.now().date()) + '.log'