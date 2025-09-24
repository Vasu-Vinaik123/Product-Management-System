from fastapi import FastAPI, APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from apis.db import engine, SessionLocal, get_db
from apis import models
from typing import Optional, List
from apis import schemas
from passlib.context import CryptContext
import bcrypt
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

SECRET_KEY = 'b564578be74571be423d843f3a51db046ed6b7d9ff87e36f8c3f59a664845628'
ALGORITHM = 'HS256'
TOKEN_EXPIRE_MINUTES = 20

router = APIRouter()
pwd_cont = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")  # Changed to match your route

def token_generator(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_token

@router.post('/login')  # Removed response_model for now
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.Seller).filter(models.Seller.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User doesn't exist")
    
    if not pwd_cont.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Password is invalid")
    
    access_token = token_generator(data={"sub": user.username})
    
    return {"access_token": access_token, "token_type": "bearer"}

def get_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="Invalid credentials", 
        headers={'WWW-Authenticate': "Bearer"}
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception
        
        
        user = db.query(models.Seller).filter(models.Seller.username == username).first()
        if user is None:
            raise credentials_exception
            
        return user 
        
    except JWTError:
        raise credentials_exception


def get_current_user(user: models.Seller = Depends(get_user)):
    return user