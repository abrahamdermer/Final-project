from typing import Any
from .i_repository import IRepository
from .es_connect import ESConnect
from tools import Logger

class ESRepository(IRepository):
    """Concrete repository for Elasticsearch indices."""
    def __init__(self, index_name:str = 'pod', conn: ESConnect|None = None):
        self._conn = conn or ESConnect()
        self.client = self._conn.connect()
        self.logger = Logger.get_logger()
        self.index = index_name 
        if not self.client.indices.exists(index=self.index,):
            self.client.indices.create(index=self.index)
            self.logger.info(f"index {self.index} created")



    def insert(self, data: dict[str, Any]) -> Any:
        # print(data)
        try:
            return self.client.index(index=self.index, document=data)
        except Exception as exc:
            print(f"ES index (insert) failed: {exc}")
            self.logger.error(f"ES index (insert) failed: {exc}")

    # def find(self, query:dict[str, Any]) ->Any:
    #     try:
    #         # ES expects a 'query' body for search
    #         return self.client.search(index=self.index, query=query)
    #     except Exception as exc:
    #         raise f"ES search failed: {exc}"

    def update(self, query: dict[str, Any], new_values:dict[str, Any]) -> Any:
        # Bulk update via update_by_query with a painless script
        try:
            script = {
                "source": "; ".join([f"ctx._source.{k} = params.{k}" for k in new_values.keys()]),
                "params": new_values,
            }
            body = {"query": query, "script": script}
            return self.client.update_by_query(index=self.index, body=body)
        except Exception as exc:
            self.logger.error(f"ES update_by_query failed: {exc}")
            print(f"ES update_by_query failed: {exc}")


    def update_by_script(self, script: dict[str, Any]) -> Any:
        try:
            return self.client.update_by_query(index=self.index, body=script)
        except Exception as exc:
            self.logger.error(f"ES update_by_query failed: {exc}")
            print(f"ES update_by_query failed: {exc}")

    # def delete(self, query: dict[str, Any]) -> Any:
    #     try:
    #         return self.client.delete_by_query(index=self.index, body={"query": dict(query)})
    #     except Exception as exc:
    #         raise f"ES delete_by_query failed: {exc}"
