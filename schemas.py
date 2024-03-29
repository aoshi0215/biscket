from pydantic import BaseModel
from typing import Optional

#Flagにはflag_name, lat, lngと、それに紐づいたコメントがある
# 例えば、flag_nameが「コンビニ」で、latが35.123456, lngが135.123456のとき、
# そのコンビニに対するコメントを取得するときは、
# GET /flags?flag_name=コンビニ&lat=35.123456&lng=135.123456

class Flag(BaseModel):
    lat: float
    lng: float

class FlagCreate(BaseModel):
    lat: float
    lng: float
    comment: str

class FlagResponse(BaseModel):
    lat: float
    lng: float
    #commentをリスト形式で返す
    comments: list

class Comment(BaseModel):
    comment: str

class AddComment(BaseModel):
    comment: str
    lat: float
    lng: float

    