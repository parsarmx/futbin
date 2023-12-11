from dotenv import load_dotenv
from os import getenv

load_dotenv(".env")


PLAYER_ROUTE = getenv("PLAYER_ROUTE")
BASE_URL = getenv("BASE_URL")
PLAYER_VERSION = getenv("PLAYER_VERSION")
