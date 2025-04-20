from motor.motor_asyncio import AsyncIOMotorCollection
from .schema import PostCreate
from .model import PostDBModel
from bson import ObjectId

async def create_post(collection: AsyncIOMotorCollection, data: PostCreate):
    post_dict = data.dict()
    result = await collection.insert_one(post_dict)
    new_post = await collection.find_one({"_id": result.inserted_id})
    return PostDBModel(**new_post)

async def get_post_by_id(collection: AsyncIOMotorCollection, post_id: str):
    post = await collection.find_one({"_id": ObjectId(post_id)})
    if post:
        return PostDBModel(**post)
    return None
