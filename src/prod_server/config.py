import os
from dotenv import load_dotenv

# detect environment
ENV = os.getenv("ENV", "dev")

# load correct env file
if ENV == "prod":
    load_dotenv(".env.prod")
else:
    load_dotenv(".env.dev")

# server config
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))

# database config
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# validation
if not MONGO_URI:
    raise ValueError("MONGO_URI is not set in environment variables")

if not DATABASE_NAME:
    raise ValueError("DATABASE_NAME is not set in environment variables")