from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from ..schemas import Post, TokenData
from datetime import datetime
from .. import models, hashing, oauth2
from .. database import get_db


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.post("/")
def create_posts(post: Post, db: Session = Depends(get_db), token_data: TokenData = Depends(oauth2.get_current_user)):
    user_id = token_data.id
    new_post = models.Post(**post.dict(), owner_id=user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
    
    
