import sqlite3

# 最小緯度、最小経度、最大緯度、最大経度
def getShelterList(left_down_latitude, left_down_longitude, right_up_latitude, right_up_longitude):
    dbname = 'shelter.db'
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    req = f"SELECT 施設・場所名, 緯度, 経度 FROM shelters WHERE 緯度 >= {left_down_latitude} AND 緯度 <= {right_up_latitude} AND 経度 >= {left_down_longitude} AND 経度 <= {right_up_longitude};"
    cur.execute(req)
    return cur.fetchall()

left_down_latitude = 35.6
left_down_longitude = 139.7
right_up_latitude = 35.65
right_up_longitude = 139.8
print((left_down_latitude, left_down_longitude))
print((right_up_latitude, right_up_longitude))
lists = getShelterList(left_down_latitude, left_down_longitude, right_up_latitude, right_up_longitude)
for row in lists:
    print(row)