from fastapi import FastAPI
from .posts.api import router as post_router

app = FastAPI(title="Government Job Form API")

# Register routes directly
app.include_router(post_router, prefix="/posts", tags=["Posts"])
