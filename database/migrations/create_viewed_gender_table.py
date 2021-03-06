from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from database.migrations.create_sessions_table import Sessions

Base = declarative_base()


class Viewed_gender(Base):
    __tablename__ = "viewed_gender"
    session_id = Column(String(255), ForeignKey(Sessions.session_id), primary_key=True)
    views = Column(Integer())
    gender_name = Column(String(255))
