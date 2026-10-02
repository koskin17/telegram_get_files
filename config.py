import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    _api_id = os.getenv("API_ID")
    _api_hash = os.getenv("API_HASH")

    if not _api_id or not _api_hash:
        raise ValueError("API_ID or API_HASH must be set in the environment variables.")

    API_ID: int = int(_api_id)
    API_HASH: str = _api_hash