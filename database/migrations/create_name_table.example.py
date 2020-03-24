from sqlalchemy import Column, Boolean, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Products(Base):
    __tablename__ = "name"

    def __repr__(self):
        return 'id: {}'.format(self.pk)