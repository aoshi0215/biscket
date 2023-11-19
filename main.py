from fastapi import FastAPI,Depends, HTTPException, status
from database import Base, engine, sessionLocal
from sqlalchemy.orm import Session
from schemas import Flag, Comment, AddComment, FlagCreate
import models
import shelter
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

#CORSを許可する
origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://localhost:8000",
    "localhost:8000",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

#ルートディレクトリにアクセスしたときの処理
@app.get("/")
def index():
    return {"message":"Hello World"}

#shelter.pyをつかって、shelter.dbの情報を返す
@app.get("/shelters/{left_down_latitude}/{left_down_longitude}/{right_up_latitude}/{right_up_longitude}}")
def get_shelters(left_down_latitude, left_down_longitude, right_up_latitude, right_up_longitude):
    return {"shelters":shelter.getShelterList(left_down_latitude, left_down_longitude, right_up_latitude, right_up_longitude)}


@app.post("/flag")
def create_flag(flag: FlagCreate, db: Session = Depends(get_db)):
    new_flag = models.Flag(lat=flag.lat, lng=flag.lng, comment=flag.comment)
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

#flagすべて取ってくる
#flagに紐づいたコメントも取ってくる
@app.get("/flags")
def get_flags(db: Session = Depends(get_db)):
    flags = db.query(models.Flag).all()
    flags_with_comments = []
    for flag in flags:
        comments = db.query(models.Comment).filter(models.Flag.lat == flag.lat, models.Flag.lng == flag.lng).all()
        flags_with_comments.append({"lat": flag.lat, "lng": flag.lng, "comments": comments})
    return {"flags": flags_with_comments}

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




