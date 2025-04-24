from pymongo import MongoClient

# MongoDB connection (synchronous)
client = MongoClient("mongodb://localhost:27017")
db = client["ccos_scrapesarthi"]