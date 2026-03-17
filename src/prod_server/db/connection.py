from pymongo import MongoClient
from prod_server.config import MONGO_URI, DATABASE_NAME

# Create client with timeout
client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=5000  # 5 seconds timeout
)

# Verify connection immediately
try:
    client.server_info()  # forces connection
    print("✅ MongoDB connected successfully")
except Exception as e:
    raise RuntimeError(f"❌ MongoDB connection failed: {e}")

# Get database
db = client[DATABASE_NAME]