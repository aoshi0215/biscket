from sqlalchemy import Column, Integer, String
from .database import Base

class Flag(Base):
    __tablename__ = "flags"

    id = Column(Integer, primary_key=True, index=True)
    lat = Column(String)
    lng = Column(String)
    comments = relationship("Comment", back_populates="flag")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)
    flag_id = Column(Integer, ForeignKey("flags.id"))

    flag = relationship("Flag", back_populates="comments")