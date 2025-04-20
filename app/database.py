from motor.motor_asyncio import AsyncIOMotorClient
from .config import MONGO_DETAILS, DATABASE_NAME

client = AsyncIOMotorClient(MONGO_DETAILS)
db = client[DATABASE_NAME]
