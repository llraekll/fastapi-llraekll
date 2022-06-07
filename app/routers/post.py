from unittest import result
from django.db import router
from fastapi import  FastAPI, Response, status, HTTPException, Depends, APIRouter
from requests import post
from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy import func
from app import oauth2
from .. import models, schemas, oauth2
from ..database import get_db

router=APIRouter(
    prefix="/posts", tags=['Posts'])



#@router.get('/', response_model= List[schemas.Post])
@router.get('/', response_model= List[schemas.PostOut]) 
def get_posts(db: Session = Depends(get_db), current_user: int= Depends(oauth2.get_current_user), 
                limit: int = 10, skip: int = 0, search: Optional[str]= ""):
    #posts= db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    posts= db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, 
                 models.Vote.post_id==models.Post.id, isouter=True).group_by(models.Post.id).filter(
                        models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    return posts
  
#(posts= db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()- this limits the user
#       to see only thier posts) this comes above return


@router.post('/', status_code=status.HTTP_201_CREATED, response_model= schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db),
                     current_user: int= Depends(oauth2.get_current_user)):
    print (current_user.id)
    new_post= models.Post(owner_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}", response_model= schemas.PostOut)
def get_post(id: int, db: Session = Depends(get_db), current_user: int= Depends(oauth2.get_current_user)):
    #post= db.query(models.Post).filter(models.Post.id == id).first()
    post= db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, 
                 models.Vote.post_id==models.Post.id, 
                 isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post id:{id} was not found")
    return post

#(if post.owner_id != current_user.id:
#   raise HTTPExcepetion(status_code=status.HTTP_404_NOT_FOUND,
#           detail="Not authorized to perform requested action")-this limits the user
#       to see only thier posts) this comes above return and below if condition


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db),
             current_user: int= Depends(oauth2.get_current_user)):
    post_query= db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f"post with id:{id} does not exist")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Not allowed to perform the requested action")
    
    post_query.delete(synchronize_session=False)
    db.commit()    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model= schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate,  db: Session = Depends(get_db),
                         current_user: int= Depends(oauth2.get_current_user)):
    post_query= db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f"post with id:{id} does not exist")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Not allowed to perform the requested action") 
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()