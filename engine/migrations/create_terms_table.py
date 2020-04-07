from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Terms(Base):
    __tablename__ = 'trend_terms'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    term_date = Column(DateTime())
