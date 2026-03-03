import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")

    if API_ID is None or API_HASH is None:
        raise ValueError("API_ID or API_HASH nor found")