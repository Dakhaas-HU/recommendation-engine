from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from engine.migrations.create_terms_table import Terms
from engine.migrations.create_products_table import Products

Base = declarative_base()


class Trend(Base):
    __tablename__ = 'trend_recommendations'
    product_id = Column(String(255), ForeignKey(Products.product_id))
    term_id = Column(Integer(), ForeignKey(Terms.id))
    amount = Column(Integer())
    id = Column(Integer(), primary_key=True, autoincrement=True)

