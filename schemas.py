from pydantic import BaseModel

#Flagにはflag_name, lat, lngと、それに紐づいたコメントがある
# 例えば、flag_nameが「コンビニ」で、latが35.123456, lngが135.123456のとき、
# そのコンビニに対するコメントを取得するときは、
# GET /flags?flag_name=コンビニ&lat=35.123456&lng=135.123456

class Flag(BaseModel):
    flag_id: int
    lat: float
    lng: float

class Comment(BaseModel):
    flag_id: int
    comment: str



    