from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from database.migrations.create_sessions_table import Sessions

Base = declarative_base()


class Viewed_promos(Base):
    __tablename__ = "viewed_promos"
    session_id = Column(String(255), ForeignKey(Sessions.profile_id), primary_key=True)
    views = Column(Integer())
    promos_name = Column(String(255))
