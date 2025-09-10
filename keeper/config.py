import os

# # Basic connection
FILE_PATH: str = os.getenv("FILE_PATH", "C:\podcasts")
TARGET_TOPIC_NAME: str = os.getenv("TARGET_TOPIC_NAME", "to_transcribing")
SOURCE_TOPIC_NAME: str = os.getenv("SOURCE_TOPIC_NAME", "to_saving")