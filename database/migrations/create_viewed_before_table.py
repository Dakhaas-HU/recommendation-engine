from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from recommendation_engine.database.migrations.create_profiles_table import Profiles
from recommendation_engine.database.migrations.create_products_table import Products

Base = declarative_base()


class Viewed_before(Base):
    __tablename__ = "viewed_before"
    profile_id = Column(String(255), ForeignKey(Profiles.profile_id), primary_key=True)
    product_id = Column(String(255), ForeignKey(Products.product_id))
