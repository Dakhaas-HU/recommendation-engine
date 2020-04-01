from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from database.migrations.create_profiles_table import Profiles
from database.migrations.create_products_table import Products

Base = declarative_base()


class Previously_recommended(Base):
    __tablename__ = "previously_recommended"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    profile_id = Column(String(255), ForeignKey(Profiles.profile_id), nullable=False)
    product_id = Column(String(255), ForeignKey(Products.product_id))
