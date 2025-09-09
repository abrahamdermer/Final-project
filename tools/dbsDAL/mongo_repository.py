from typing import Any
from .i_repository import IRepository
from .mongo_connect import MongoConnect
# from tools import Logger

class MongoRepository(IRepository):
    """Concrete repository for MongoDB collections."""


    def __init__(self, collection_name:str = "test", conn: MongoConnect|None = None):
        self._conn = conn or MongoConnect()
        self.db = self._conn.connect()
        self.fs = None
        self.name = collection_name
        self.collection = self.db[self.name]
        # self.logger =Logger.get_logger()

    def insert(self, data: dict[str, Any]) -> Any:
        try:
            return self.collection.insert_one(data).inserted_id
        except Exception as exc:
            raise 
            # self.logger.error( f"Mongo insert failed: {exc}")
        
    def insert_gridfs(self, data: dict[str, Any]) -> Any:
        if self.fs is None:
            self.fs = self._conn.connect_gridfs(self.name)
        try:
            res = self.fs.put(data['file'],filename=data['name'], metadata=data['metadata'])
            print(res)
            return res
            # return self.fs.upload_from_stream(data['name'], data['file'])
        except Exception as exc:
            # self.logger.error(f"Mongo insert failed: {exc}")
            raise

    def find_gridfs(self, query: dict[str, Any]) -> list[Any]:
        if self.fs is None:
            self.fs = self._conn.connect_gridfs(self.name)
        try:
            file_content = b''
            grid_out_cursor  =  self.fs.find({"metadata": query})
            for grid_out_file in grid_out_cursor:
                file_content += grid_out_file.read()
                
            return file_content

        except Exception as exc:
            print (f"Mongo find failed: {exc}")





    def get_all(self):
        for grid_out in self.fs.find():
            print(f"File Name: {grid_out.filename}")
            print(f"File ID: {grid_out._id}")
            print(f"Content Type: {grid_out.content_type}")
            print(f"Length: {grid_out.length} bytes")
        





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
