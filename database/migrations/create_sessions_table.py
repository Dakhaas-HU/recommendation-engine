from sqlalchemy import Column, Boolean, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from database.migrations.create_profiles_table import Profiles

Base = declarative_base()


class Sessions(Base):
    __tablename__ = "sessions"
    session_id = Column(String(255), primary_key=True)
    profile_id = Column(String(255), ForeignKey(Profiles.profile_id))
    session_start = Column(DateTime())
    session_end = Column(DateTime())
    os_family = Column(String(255))
    browser_family = Column(String(255))
    device_brand = Column(String(255))
    is_bot = Column(Boolean())
    is_email_client = Column(Boolean())
    is_mobile = Column(Boolean())
    is_pc = Column(Boolean())
    is_tablet = Column(Boolean())
    is_touch = Column(Boolean())

    def __repr__(self):
        return 'id: {}'.format(self.session_id)
