from sqlalchemy import Integer, String, Column, ForeignKey
from .db import Base
from sqlalchemy.orm import relationship


class Product(Base):
  __tablename__ = 'product'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  description = Column(String)
  price = Column(Integer)
  seller_id = Column(Integer, ForeignKey('seller.id'))
  seller = relationship("Seller", back_populates="product")


class Seller(Base):
  __tablename__ = 'seller'
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String)
  email = Column(String)
  password = Column(String)
  product = relationship("Product", back_populates="seller")
