import os
from dotenv import load_dotenv

load_dotenv()

ENDPOINT = os.getenv('DRUGTARGETCOMMONS_ENDPOINT')
DATABASE = os.getenv('DATABASE_URL')