from pymongo import MongoClient
import gridfs
from .i_connect import IConnect
from . import config
# from tools import Logger

class MongoConnect(IConnect):
    """MongoDB connection manager (singleton per instance)."""
    def __init__(self, uri:str = config.MONGO_URL, db_name:str =config.MONGO_DB_NAME):
        self.uri = uri
        self.db_name = db_name
        self._client = None
        self.db = None
        self.fs = None
        # self.logger = Logger.get_logger()

    def connect(self):
        try:
            if self._client is None:
                self._client = MongoClient(self.uri)
                # self.logger.info(f"connected to mongoDB")
                self.db = self._client[self.db_name]
            return self.db
        
        except Exception as exc:
            # self.logger.error( f"MongoDB connection failed: {exc}")
            raise


    def connect_gridfs(self,col_name):

        try:
            if self.db is None:
                self.connect()
            if self.fs is None:
                self.fs = gridfs.GridFS(self.db , collection=col_name)
            return self.fs
        except :
            # self.logger.error("MongoDB connection failed")
            raise

    def close(self) -> None:
        if self._client is not None:
            self._client.close()
            self._client = None
            self.db = None
