import DBconnection
import mysql.connector
from mysql.connector import Error

db = DBconnection.DB(None)
db.linkinDB()
def qeuery_serviceitems(db):
    # 顯示目前使用的資料庫
    myCursor = db.connection.cursor()
    myCursor.execute("SELECT DATABASE();")
    record = myCursor.fetchone()
    print("目前使用的資料庫：", record)

    # 查詢資料庫
    myCursor.execute("select * from serviceitems;")

    # 取回全部的資料
    records = myCursor.fetchall()
    print("資料筆數：", myCursor.rowcount)

    ### 列出查詢的資料
    
    for x in records:
        print(x)

qeuery_serviceitems(db)