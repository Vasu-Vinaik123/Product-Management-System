from fastapi import FastAPI, APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from apis.db import engine, SessionLocal, get_db
from apis import models
from typing import Optional, List
from apis import schemas
from apis.routers.signin import get_user

router = APIRouter(tags=['Products'], prefix="/product")





@router.post('/', response_model= schemas.ShowProduct, status_code=status.HTTP_201_CREATED)
def add_product(product: schemas.Product , db: Session = Depends(get_db)):
  product = models.Product(name= product.name, description=product.description, price=product.price, seller_id=product.seller_id)
  db.add(product)
  db.commit()
  db.refresh(product)
  return product


@router.get('/', response_model=List[schemas.ShowProduct])
def fetch_all(db:Session = Depends(get_db), current_user:schemas.Seller = Depends(get_user)):
  product = db.query(models.Product).all()
  return product


@router.get('/{id}', response_model= schemas.ShowProduct)
def product_by_id(id: int, db:Session = Depends(get_db)):
  product = db.query(models.Product).filter(models.Product.id == id).first()
  if not product:
    raise HTTPException(detail=f"product with this id {id} doesn't exist", status_code=status.HTTP_404_NOT_FOUND)
  return product



@router.put('/{id}')
def update_product(id: int, product: schemas.Update_Product, db:Session = Depends(get_db)):
  product_in_db = db.query(models.Product).filter(models.Product.id == id).first()
  if not product_in_db:
    raise HTTPException(detail=f"product with this id {id} doesn't exist", status_code=status.HTTP_404_NOT_FOUND)
  
  product_in_db.name = product.name
  product_in_db.description = product.description
  product_in_db.price = product.price

  db.commit()
  return{'Product has been updated successfully'}




@router.delete('/{id}')
def delete_product(id:int, db:Session = Depends(get_db)):
  product = db.query(models.Product).filter(models.Product.id == id).first()
  if not product:
    raise HTTPException(detail=f"product with this id {id} doesn't exist", status_code=status.HTTP_404_NOT_FOUND)
  
  db.delete(product)
  db.commit()
  return 'product has been deleted successfully'
 