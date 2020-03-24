from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from recommendation_engine.database.migrations.create_products_table import Products
from recommendation_engine.database.migrations.create_sessions_table import Sessions

Base = declarative_base()


class Order(Base):
    __tablename__ = "order"
    session_id = Column(String(255), ForeignKey(Sessions.profile_id), primary_key=True)
    product_id = Column(String(255), ForeignKey(Products.product_id))
