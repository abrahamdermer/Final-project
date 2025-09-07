from elasticsearch import Elasticsearch
from .i_connect import IConnect

class ESConnect(IConnect):
    """Elasticsearch connection manager."""
    def __init__(self, host: str = "http://localhost:9200"):
        self.host = host 
        self.client = None

    def connect(self):
        try:
            if self.client is None:
                self.client = Elasticsearch(self.host)
            return self.client
        except Exception as exc:
            raise f"Failed connecting to Elasticsearch at {self.host}: {exc}"
        
    def build_index(self)->None:
        if self.es.indices.exists(index=self.index_name):
            self.es.indices.delete(index=self.index_name, ignore_unavailable=True)

    def close(self) -> None:
        if self.client is not None:
            try:
                self.client.transport.close()
            finally:
                self.client = None
