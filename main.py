from fastapi import FastAPI,Depends
from .models import Base
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .schemas import Flag, Comment

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
    return {"message":"flag created",
            "flag": new_flag}

#特定のflagがクリックされたとき、そのflag_idがリクエストで送られてくる
#そのflag_idを使って、そのflagに紐づいたコメントを取得する
@app.get("flags/{flag_lat}/{flag_lng}")
def get_flag(flag: Flag, db: Session = Depends(get_db)):
    comments = db.query(models.Comment).filter(models.Flag.lat == flag.lat, models.Flag.lng == flag.lng).all()
    return {"comments": comments}


@app.post("/flags/{flag_lat}/{flag_lng}")
def add_comment(flag: Flag, comment: Comment, db: Session = Depends(get_db)):
    new_comment = models.Comment(comment=comment.comment, flag_lat=flag.lat, flag_lng=flag.lng)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return {"message" :"comment created",
            "comment": comment}



