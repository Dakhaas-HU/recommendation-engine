from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from recommendation_engine.database.migrations.create_sessions_table import Sessions

Base = declarative_base()


class User_agent(Base):
    __tablename__ = "user_agent"
    session_id = Column(String(255), ForeignKey(Sessions.profile_id), primary_key=True)
    os_family = Column(String(255))
    browser_family = Column(String(255))
    device_brandutel = Column(String(255))
    is_botutel = Column(Boolean())
    is_email_clientutel = Column(Boolean())
    is_mobileutel = Column(Boolean())
    is_pcutel = Column(Boolean())
    is_tableutel = Column(Boolean())
    istouchutel = Column(Boolean())
