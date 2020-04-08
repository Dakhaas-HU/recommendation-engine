from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from engine.migrations.create_products_table import Products
from engine.migrations.create_terms_table import Terms

Base = declarative_base()


class Homepage(Base):
    __tablename__ = 'homepage_recommendations'
    term_id = Column(Integer(), ForeignKey(Terms.id))
    category = Column(String(255))
    product_ids = Column(String(255))
    id = Column(Integer(), primary_key=True)
