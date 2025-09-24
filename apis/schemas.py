from pydantic import BaseModel
from apis.models import Product
from typing import Optional


class Product(BaseModel):
  
  name: str
  description: str
  price: int
  seller_id: int

  class Config:
    from_attributes = True




class Update_Product(Product):
  pass 



class Seller(BaseModel):
  username: str
  email: str
  password: str


class ShowSeller(BaseModel):
  id: int
  username: str
  email:str

  class Config:
    from_attributes = True




class ShowProduct(Product):
  id: int
  seller: ShowSeller
  class Config:
    from_attributes = True



class Login_User(BaseModel):
  username: str
  password: str


class Token(BaseModel):
  token: str
  token_type: str


class Token_Data(BaseModel):
  username: Optional[str] = None
