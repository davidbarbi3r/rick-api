import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

USER_NAME = os.getenv('POSTGRES_USER')
USER_PASSWORD = os.getenv('POSTGRES_PASSWORD')