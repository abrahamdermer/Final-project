import os

# # Basic connection
KAFKA_HOST: str = os.getenv("KAFKA_HOST", "localhost:9092")
KAFKA_GROP: str = os.getenv("KAFKA_GROP", "mygroup")
KAFKA_ID: str = os.getenv("KAFKA_ID", "kafka-dal-client")