import os
from dotenv import load_dotenv

ENV = os.getenv("ENV", "dev")

if ENV == "prod":
    load_dotenv(".env.prod", override=False)
else:
    load_dotenv(".env.dev", override=False)

HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.environ.get("PORT", 8000))  # <-- important change

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

if not MONGO_URI:
    raise ValueError("MONGO_URI is not set in environment variables")

if not DATABASE_NAME:
    raise ValueError("DATABASE_NAME is not set in environment variables")
