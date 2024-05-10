#導入mysql
import mysql.connector
#連線到資料庫
con=mysql.connector.connect(
    user="root",
    password="Qoo9898t@",
    host="localhost",
    database="website"
)
print("資料庫連線成功")
#建立Cursor物件，用來對資料庫下SQL指令(這邊的con是上面的連線內容變數)
cursor=con.cursor()
#取得一筆資料
cursor.execute("select * from member")
data=cursor.fetchall()
print(data)
#逐一取得(迴圈)
for i in data:
    print(i)

#關閉連線(暫時先關閉)
con.close()

