from .database import db

def get_post_collection():
    return db.get_collection("posts")
