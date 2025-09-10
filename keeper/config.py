import os

# # Basic connection
TARGET_TOPIC_NAME: str = os.getenv("TARGET_TOPIC_NAME", "to_transcribing")
SOURCE_TOPIC_NAME: str = os.getenv("SOURCE_TOPIC_NAME", "to_saving")