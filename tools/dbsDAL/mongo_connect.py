from pymongo import MongoClient
from .i_connect import IConnect

class MongoConnect(IConnect):
    """MongoDB connection manager (singleton per instance)."""
    def __init__(self, uri:str = "mongodb://localhost:27017", db_name:str = "data"):
        self.uri = uri
        self.db_name = db_name
        self._client = None
        self.db = None

    def connect(self):
        try:
            if self._client is None:
                self._client = MongoClient(self.uri)
            self.db = self._client[self.db_name]
            return self.db
        except Exception as exc:
            raise f"MongoDB connection failed: {exc}"
        
    def close(self) -> None:
        if self._client is not None:
            self._client.close()
            self._client = None
            self.db = None
