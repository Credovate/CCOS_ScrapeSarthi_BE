from fastapi import APIRouter, Depends, HTTPException
from .schema import PostCreate, PostOut
from .service import create_post, get_post_by_id
from app.dependencies import get_post_collection

router = APIRouter()

@router.post("/", response_model=PostOut)
async def submit_form(post: PostCreate, collection=Depends(get_post_collection)):
    return await create_post(collection, post)

@router.get("/{post_id}", response_model=PostOut)
async def read_post(post_id: str, collection=Depends(get_post_collection)):
    result = await get_post_by_id(collection, post_id)
    if not result:
        raise HTTPException(status_code=404, detail="Form not found")
    return result
