import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(override=True)

BASE_URL = os.getenv('DRUGTARGETCOMMONS_BASE_URL')
API_ENDPOINT = os.getenv('DRUGTARGETCOMMONS_API_ENDPOINT')
API_LIMIT = os.getenv('DRUGTARGETCOMMONS_API_LIMIT')
DATABASE_URI = os.getenv('DATABASE_URI')
ENVIRONMENT = os.getenv('ENV')
LOG_LEVEL = os.getenv('LOG_LEVEL')
LOG_FILE = 'logging_' + str(datetime.now().date()) + '.log'