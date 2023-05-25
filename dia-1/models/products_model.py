from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from db import db

class ProductsModel(db.Model):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45))
    stock = Column(Integer)
    price = Column(Float)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    status = Column(Boolean)