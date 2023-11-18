from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message":"Hello World"}

@app.get("/shelters")
def get_shelters(shelter_name, lat, lng):
    return {"message": "Shelters",
            "shelter_name": shelter_name,
            "lat": lat,
            "lng": lng}


@app.post("/flags")
def create_flag(flag_name, lat, lng):
    return {"flag_name": flag_name,
            "lat": lat,
            "lng": lng}

#特定のflagがクリックされたとき、そのflag_idがリクエストで送られてくる
#そのflag_idを使って、そのflagに紐づいたコメントを取得する
@app.get("flags/{flag_id}")
def get_flag(flag_id):
    return {"flag_id": flag_id}


@app.post("/flags/{flag_id}/comments")
def create_comment(flag_id, comment):
    return {"flag_id": flag_id,
            "comment": comment}
