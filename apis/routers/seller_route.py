from fastapi import FastAPI, APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from apis.db import engine, SessionLocal, get_db
from apis import models
from typing import Optional, List
from apis import schemas
from passlib.context import CryptContext
import bcrypt

router = APIRouter(tags=['Sellers'], prefix='/seller')

pwd_cont = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get('', response_model= List[schemas.ShowSeller])
def sellers(db:Session = Depends(get_db)):
  seller = db.query(models.Seller).all()
  return seller

@router.post('', response_model=schemas.ShowSeller, status_code=status.HTTP_201_CREATED)
def create(seller: schemas.Seller, db:Session = Depends(get_db)):
  hashed_pwd = pwd_cont.hash(seller.password)
  new_seller = models.Seller(username=seller.username, email=seller.email, password=hashed_pwd)
  db.add(new_seller)
  db.commit()
  db.refresh(new_seller)
  return new_seller
