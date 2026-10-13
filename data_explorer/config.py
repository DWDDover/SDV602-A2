import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

DB_NAME = "data_explorer"
DATA_SOURCES_COLLECTION = "data_sources"
CHAT_MESSAGES_COLLECTION ="chat_messages"
POLL_RATE = 500