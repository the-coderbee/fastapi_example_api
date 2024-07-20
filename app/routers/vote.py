from fastapi import Depends, status, HTTPException, APIRouter
from ..database import get_db
from .. import models, schemas, utils, oauth2
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Post not found')
    
    voted = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    
    if vote.dir == 1:
        if voted.first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="user has already voted")
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "successfully added vote"}
    if not voted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote doesn't exist")
    voted.delete(synchronize_session=False)
    db.commit()
    return {"message": "successfully removed vote"}
