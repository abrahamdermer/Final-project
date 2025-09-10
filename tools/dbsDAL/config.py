import os

# # Basic connection
MONGO_URL: str = os.getenv("MONGO_URL", "mongodb://localhost:27000")
MONGO_DB_NAME: str = os.getenv("MONGO_DB_NAME", "data")
MONGO_COLLECTION_NAME: str = os.getenv("MONGO_COLLECTION_NAME", "test")

ES_HOST = os.getenv("ES_HOST", "http://localhost:9200")
