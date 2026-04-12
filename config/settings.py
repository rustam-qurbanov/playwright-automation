import os
import json
from pathlib import Path
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

ENV = os.getenv("ENV", "local")
config_path = Path(__file__).parent / "environments" / f"{ENV}.json"

with open(config_path, "r") as f:
    config = json.load(f)

BASE_URL = config.get("BASE_URL", "https://www.saucedemo.com")
