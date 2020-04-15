import os
from dotenv import load_dotenv

load_dotenv()

BASE_ENDPOINT = os.getenv('DRUGTARGETCOMMONS_BASE_ENDPOINT')
API_ENDPOINT = os.getenv('DRUGTARGETCOMMONS_API_ENDPOINT')
DATABASE_URL = os.getenv('DATABASE')
ENVIRONMENT = os.getenv('ENV')
