import os
from dotenv import load_dotenv

BASE_DIR = os.path.split(__file__)[0]

ENV_PATH = os.path.join(BASE_DIR, '.env')
load_dotenv(ENV_PATH)

CSV_DIR = BASE_DIR + "/csv"