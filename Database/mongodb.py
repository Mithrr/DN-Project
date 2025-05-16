from pymongo import MongoClient
import os

# You can replace this with a MongoDB Atlas connection string later
MONGO_URL = "mongodb://localhost:27017/"

client = MongoClient(MONGO_URL)
db = client["The_DN_project"]
user_collection = db["users"]
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# You can replace this with a MongoDB Atlas connection string later
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

try:
    client = MongoClient(MONGO_URL)
    db = client["networking_app"]
    user_collection = db["users"]
    logger.info("Connected to MongoDB")
except Exception as e:
    logger.error(f"Failed to connect to MongoDB: {e}")