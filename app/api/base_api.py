import logging

logger = logging.getLogger(__name__)


class BaseApi:
    def __init__(self, base_url: str):
        self.base_url = base_url

    # In a real project, this would use a library like requests or httpx.
    # We leave this as a stub for now.
    def get(self, endpoint: str):
        logger.info(f"GET {self.base_url}{endpoint}")
        pass

    def post(self, endpoint: str, data: dict):
        logger.info(f"POST {self.base_url}{endpoint}")
        pass
