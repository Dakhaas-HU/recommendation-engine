from sqlalchemy import Column, Boolean, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from recommendation_engine.database.migrations.create_profiles_table import Profiles

Base = declarative_base()


class Sessions(Base):
    __tablename__ = "sessions"
    session_id = Column(String(255), primary_key=True)
    profile_id = Column(String(255), ForeignKey(Profiles.profile_id))
    session_start = Column(DateTime())
    session_end = Column(DateTime())

    def __repr__(self):
        return 'id: {}'.format(self.session_id)