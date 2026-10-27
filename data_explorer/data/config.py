import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

DB_NAME = "data_explorer"
USER_COLLECTION = "users"
DATA_SOURCES_COLLECTION = "data_sources"
CHAT_MESSAGES_COLLECTION ="chat_messages"
SESSION_COLLECTION = "sessions"
POLL_RATE = 500