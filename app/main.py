from fastapi import FastAPI
from app.posts.api import router as posts_router

app = FastAPI()

app.include_router(posts_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the CCOS Scrapesarthi API"}