from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from engine.migrations.create_products_table import Products

Base = declarative_base()


class Collaborative(Base):
    __tablename__ = 'collaborative_recommendations'
    profile_id = Column(String(255))
    product_id = Column(String(255), ForeignKey(Products.product_id))
    id = Column(Integer(), primary_key=True)
