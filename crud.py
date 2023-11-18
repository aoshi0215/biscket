
#データベースの操作
from sqlalchemy.orm import Session
from . import models, schemas

def get_flag(db: Session, flag_id: int):
    return db.query(models.Flag).filter(models.Flag.id == flag_id).first()

def get_flags(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Flag).offset(skip).limit(limit).all()

def create_flag(db: Session, flag: schemas.Flag):
    db_flag = models.Flag(lat=flag.lat, lng=flag.lng)
    db.add(db_flag)
    db.commit()
    db.refresh(db_flag)
    return db_flag

def get_comments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Comment).offset(skip).limit(limit).all()

def create_comment(db: Session, comment: schemas.Comment, flag_id: int):
    db_comment = models.Comment(comment=comment.comment, flag_id=flag_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments_by_flag_id(db: Session, flag_id: int):
    return db.query(models.Comment).filter(models.Comment.flag_id == flag_id).all()

def get_flags_by_flag_name(db: Session, flag_name: str):
    return db.query(models.Flag).filter(models.Flag.flag_name == flag_name).all()

def get_flags_by_lat_lng(db: Session, lat: float, lng: float):
    return db.query(models.Flag).filter(models.Flag.lat == lat, models.Flag.lng == lng).all()

def get_flags_by_flag_name_and_lat_lng(db: Session, flag_name: str, lat: float, lng: float):
    return db.query(models.Flag).filter(models.Flag.flag_name == flag_name, models.Flag.lat == lat, models.Flag.lng == lng).all()

def get_flags_by_flag_name_and_lat(db: Session, flag_name: str, lat: float):
    return db.query(models.Flag).filter(models.Flag.flag_name == flag_name, models.Flag.lat == lat).all()
