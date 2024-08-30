from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, func
from sqlalchemy.orm import relationship
from app.db.base import Base

class Category(Base):
    __tablename__ = 'categories'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    slug = Column('slug', String, nullable=False)
    Products = relationship('Product', back_populates='category')

class Product(Base):
    __tablename__ = 'products'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    slug = Column('slug', String, nullable=False)
    price = Column('price', Float)
    stock = Column('stock', Integer)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, onupdate=func.now())
    category_id = Column('column_id', ForeignKey('categories.id'), nullable=False)
    category = relationship('Category', back_populates='products')

