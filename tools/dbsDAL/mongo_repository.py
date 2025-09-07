from typing import Any
from .i_repository import IRepository
from .mongo_connect import MongoConnect

class MongoRepository(IRepository):
    """Concrete repository for MongoDB collections."""


    def __init__(self, collection_name:str = "", conn: MongoConnect|None = None):
        self._conn = conn or MongoConnect()
        self.db = self._conn.connect()
        name = collection_name
        self.collection = self.db[name]

    def insert(self, data: dict[str, Any]) -> Any:
        try:
            return self.collection.insert_one(data).inserted_id
        except Exception as exc:
            raise f"Mongo insert failed: {exc}"

    # def find(self, query: dict[str, Any]) -> list[Any]:
    #     try:
    #         return self.collection.find(query)
    #     except Exception as exc:
    #         raise (f"Mongo find failed: {exc}")

    # def update(self, query: dict[str, Any], new_values: dict[str, Any]) -> Any:
    #     try:
    #         return self.collection.update_many(query, {"$set": new_values})
    #     except Exception as exc:
    #         raise (f"Mongo update failed: {exc}")

    # def delete(self, query: dict[str, Any]) -> Any:
    #     try:
    #         return self.collection.delete_many(query)
    #     except Exception as exc:
    #         raise (f"Mongo delete failed: {exc}")
