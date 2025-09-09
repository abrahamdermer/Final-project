from elasticsearch import Elasticsearch
from .i_connect import IConnect
# from tools import Logger


class ESConnect(IConnect):
    """Elasticsearch connection manager."""
    def __init__(self, host: str = "http://localhost:9200"):
        self.host = host 
        self.client = None
        # self.logger = Logger.get_logger()

    def connect(self):
        try:
            if self.client is None:
                self.client = Elasticsearch(self.host)
                # self.logger.info(f"ES connected")
            return self.client
        except Exception as exc:
            print(f"Failed connecting to Elasticsearch at {self.host}: {exc}")
            # self.logger.error(f"Failed connecting to Elasticsearch at {self.host}: {exc}")
        
    def close(self) -> None:
        if self.client is not None:
            try:
                self.client.transport.close()
            finally:
                self.client = None
