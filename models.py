from sqlalchemy import Column, Integer, String, ForeignKey,Date,Float
from database import Base
from sqlalchemy.orm import relationship


class Flag(Base):
    __tablename__ = "flags"

    id = Column(Integer, primary_key=True, index=True)
    lat = Column(Float)
    lng = Column(Float)
    comments = relationship("Comment", back_populates="flag")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)
    flag_id = Column(Integer, ForeignKey("flags.id"))

    flag = relationship("Flag", back_populates="comments")