from fastapi import FastAPI,Depends, HTTPException, status
from database import Base, engine, sessionLocal
from sqlalchemy.orm import Session
from schemas import Flag, Comment, AddComment
import models


app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def index():
    return {"message":"Hello World"}

@app.get("/shelters")
def get_shelters(shelter_name, lat, lng):
    return {"message": "Shelters",
            "shelter_name": shelter_name,
            "lat": lat,
            "lng": lng}


@app.post("/flag")
def create_flag(flag: Flag, db: Session = Depends(get_db)):
    new_flag = models.Flag(lat=flag.lat, lng=flag.lng)
    db.add(new_flag)
    db.commit()
    db.refresh(new_flag)
    return {"flag": new_flag}

#特定のflagがクリックされたとき、そのflag_idがリクエストで送られてくる
#そのflag_idを使って、そのflagに紐づいたコメントを取得する
@app.get("flags/{flag_lat}/{flag_lng}")
def get_flag(flag: Flag, db: Session = Depends(get_db)):
    comments = db.query(models.Comment).filter(models.Flag.lat == flag.lat, models.Flag.lng == flag.lng).all()
    return {"comments": comments}


@app.post("/flags/{flag_lat}/{flag_lng}")
def add_comment(comment: Comment, db: Session = Depends(get_db)):
    #latとlngが一致するflagを取得する
    flag = db.query(models.Flag).filter(models.Flag.lat == flag_lat, models.Flag.lng == flag_lng).first()
    #flagに紐づいたコメントを作成する
    new_comment = models.Comment(comment=comment.comment, flag_id=flag.id) 
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return {"message":"comment created",
            "comment": new_comment}




