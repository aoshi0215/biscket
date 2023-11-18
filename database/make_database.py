import sqlite3
import csv

open_csv = open("shelter.csv")
read_csv = csv.reader(open_csv)
next_row = next(read_csv)

rows = []
for row in read_csv:
    rows.append(row)

dbname = 'shelter.db'
con = sqlite3.connect(dbname)
cur = con.cursor()
#テーブル作成
sql = u"""CREATE TABLE IF NOT EXISTS shelters (施設・場所名 text, 緯度 double, 経度 double);"""
cur.execute(sql)
for row in rows:
    inp = 'INSERT INTO shelters (施設・場所名, 緯度, 経度) values (?,?,?)'
    if '東京都' in row[1]: 
        data = [row[3], row[14], row[15]]
        cur.execute(inp, data)

con.commit()
con.close()
open_csv.close()