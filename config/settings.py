import json
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", "local")
_config_path = Path(__file__).parent / "environments" / f"{ENV}.json"

with open(_config_path) as f:
    _config = json.load(f)

BASE_URL: str = _config["BASE_URL"]
TIMEOUT: int = _config.get("TIMEOUT", 30000)
BROWSER: str = _config.get("BROWSER", "chromium")
