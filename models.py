from sqlalchemy import Column, Integer, String, ForeignKey,Date,Float,DateTime
from database import Base
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta, timezone, tzinfo, date, time



class Flag(Base):
    __tablename__ = "flags"

    id = Column(Integer, primary_key=True, index=True)
    lat = Column(Float)
    lng = Column(Float)
    comments = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    @staticmethod
    def current_time():
        return datetime.utcnow()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = self.current_time()



'''
class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)
    flag_id = Column(Integer, ForeignKey("flags.id"))

    flag = relationship("Flag", back_populates="comments")
'''