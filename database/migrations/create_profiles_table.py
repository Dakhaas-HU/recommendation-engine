from sqlalchemy import Column, Boolean, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Profiles(Base):
    __tablename__ = "profiles"
    profile_id = Column(String(255), primary_key=True)
    segment = Column(String(255))

    def __repr__(self):
        return 'id: {}'.format(self.profile_id)