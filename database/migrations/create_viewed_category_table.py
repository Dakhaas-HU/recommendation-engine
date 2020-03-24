from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from recommendation_engine.database.migrations.create_sessions_table import Sessions

Base = declarative_base()


class Viewed_category(Base):
    __tablename__ = "viewed_category"
    session_id = Column(String(255), ForeignKey(Sessions.profile_id), primary_key=True)
    views = Column(Integer())
    category_name = Column(String(255))
