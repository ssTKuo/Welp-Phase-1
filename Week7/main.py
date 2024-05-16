import uvicorn                                               #(類別0)導入uvicorn，不用終端機執行用

from fastapi import FastAPI, Request ,Form                     #導入FastAPI主模塊，Form是給HTML文件用的

from fastapi.staticfiles import StaticFiles                  #(類別1)FastAPI的一个模块，用于服务静态文件(HTML、CSS),这些文件可以通过 HTTP 被访问。使用 StaticFiles 模块时，你会指定一个目录作为静态文件的根目录。FastAPI 会自动服务这个目录下的所有文件。这样，你就不需要为目录下的每个文件编写单独的路由。
from fastapi.templating import Jinja2Templates               #(類別2)導入模板
from fastapi.responses import HTMLResponse #JSONResponse     #(類別3)FastAPI内建的一个响应类，用于直接返回HTML内容。如果你的API需要返回 HTML（那就導入HTMLResponse），如果想要回傳字典（那就導入JSONResponse），本題目兩者皆用不到
from fastapi.responses import RedirectResponse, JSONResponse #(類別4)這題目應該用這個就好，重新導向一個地址的意思
from typing import Optional                                  #導入可選參數的模組，這邊應用在流程2裡面，讓帳號密碼是可選輸入
from starlette.middleware.sessions import SessionMiddleware  #(類別5)導入中間件模組
import mysql.connector                                       #(類別6)連線到MySQL資料庫


#(類別6)連線到MySQL資料庫&處理資料庫資料      *****這段程式碼不須用了，都寫在def中調用即可*****
#***************************************************************************************************************
#導入mysql
import mysql.connector
#連線到資料庫
# con=mysql.connector.connect(
#     user="root",
#     password="Qoo9898t@",
#     host="localhost",
#     database="website"
# )
# print("資料庫連線成功")

#建立Cursor物件，用來對資料庫下SQL指令(這邊的con是上面的連線內容變數)
# cursor=con.cursor()
#取得資料庫內資料(取得使用者名稱(name)、帳號(username)、密碼(password))
# cursor = con.cursor()
# cursor.execute("SELECT name, username, password FROM member")
# data = cursor.fetchall()
# print(data)
#把data中的資料轉換丟進字典中
# user_dict={}
# for i in data:
#     name=i[0]
#     username=i[1]
#     password=i[2]
#     user_dict[username] = (name, password)  #帳號(username)當作鍵，值則用元祖Tuple包裝起來 (使用者名稱(name),密碼(password))
# print(user_dict)
#關閉連線(暫時先關閉)
# con.close()
#***************************************************************************************************************



app=FastAPI() #FastAPI 物件
app.mount("/static", StaticFiles(directory="static"), name="static")    #(類別1)
templates = Jinja2Templates(directory="templates")                      #(類別2)

app.add_middleware(
    SessionMiddleware,
    secret_key="WEEK4TASK3",
    session_cookie="session",
    max_age=172800,  # 持續持間，單位為秒
    https_only=False,
    same_site="lax"
)


#流程1，用戶訪問以下網址時，用戶瀏覽器會發送一個HTTP GET請求到後端伺服器。這邊我定義了一個名為login_form函數，當收到GET請求後，函數會返回login.html內容作為HTTP響應。
@app.get("/")
def login_form(request:Request):
    return templates.TemplateResponse("signin.html",{"request":request})

#流程5，註冊表單(先連線到SQL，再撰寫程式邏輯)
@app.post("/signup")
def signup(request: Request,name: Optional[str] = Form(None) ,username: Optional[str] = Form(None), password: Optional[str] = Form(None)):
    try:
        #連接到數據庫
        conn=mysql.connector.connect(
        user="root",
        password="Qoo9898t@",
        host="localhost",
        database="website"
        )
        #建立Cursor物件，用來對資料庫下SQL指令(這邊的con是上面的連線內容變數)
        cursor = conn.cursor()
        
        #檢查是否有空值輸入
        if not name or not username or not password:
            return RedirectResponse(url="/", status_code=303)
        
        #檢查SQL中username是否存在
        cursor.execute("SELECT username FROM member where username=%s", (username,))
        if cursor.fetchone():
            return RedirectResponse(url="/error?message=Repeated username", status_code=303)
        
        #創建新用戶
        cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)", (name, username, password))
        conn.commit()

        #登錄用戶(紀錄登入狀態)，如果沒紀錄，會停留在/頁面
        cursor.execute("SELECT id, name FROM member WHERE username = %s", (username,))
        user_record = cursor.fetchone()
        if user_record:
            request.session['SIGNED-IN'] = True
            request.session['user_id'] = user_record[0]
            request.session['name'] = user_record[1]
        return RedirectResponse(url="/member", status_code=303)
    
    #發生錯誤的處理方式(如資料庫不存在等...)
    except Exception as e:
            conn.rollback()  
            print(f"Database Error: {e}")
            return RedirectResponse(url="/error?message=Failed to register", status_code=500)
    #無論try的內容，都會執行(關閉資料庫)
    #這裡採用if語句來執行關閉連線的做法，先檢查cursor、conn是否存在。再關閉
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
     

#(不同於Week4，新增連接資料庫的程式碼)流程2，用戶填寫帳號密碼後，點擊登入按鈕，瀏覽器發送HTTP POST請求到/signin路徑。login函數會合對用戶輸入的帳密，如果匹配成功，則回傳登入成功的JSON響應。
@app.post("/signin")
def login(request: Request,username: Optional[str] = Form(None), password: Optional[str] = Form(None)):
    #這邊亦要連結到資料庫，用以更新資料庫(如果有使用者新註冊，才抓地到資料)
    try:
        conn = mysql.connector.connect(
            user="root",
            password="Qoo9898t@",
            host="localhost",
            database="website"
        )
        cursor = conn.cursor()
        #檢查是否有確實輸入帳號密碼
        if not username and not password:
            return RedirectResponse(url="/error?message=Please enter username and password", status_code=303)
        elif not username:
            return RedirectResponse(url="/error?message=Please enter username", status_code=303)
        elif not password:
            return RedirectResponse(url="/error?message=Please enter password", status_code=303)

        #檢查數據庫是否有對應的帳號密碼
        cursor.execute("SELECT id, name, password FROM member WHERE username = %s", (username,))
        user_record = cursor.fetchone()
        if user_record and user_record[2] == password:
            #用中間件儲存登入狀態
            request.session['SIGNED-IN'] = True
            #用中間件儲存使用者id(******作為辨識用的唯一值******)
            request.session['user_id'] = user_record[0]
            #用中間件儲存用戶名
            request.session['name'] = user_record[1]
            return RedirectResponse(url="/member", status_code=303)
        else:
            return RedirectResponse(url="/error?message=Username or password is not correct", status_code=303)

    except mysql.connector.Error as e:
        print(f"Database Error: {e}")
        return RedirectResponse(url="/error?message=Database error", status_code=500)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

#/createMessage頁面推送post請求，新增留言功能，再回傳給/member
@app.post("/createMessage")
def member_page(request: Request,content: Optional[str] = Form(None)): 
    #先確保使用者為登入狀態，避免使用者直接輸入網址來留言
    if 'SIGNED-IN' not in request.session or not request.session['SIGNED-IN']:
        return RedirectResponse(url="/member", status_code=303)
    
    #從中間件獲取目前登入的用戶ID(因為ID具有唯一性)，剛剛於/signin，已經有定義過了，直接拿來用
    #使用者id(member資料表中)會作為外鍵約束，連結到message資料表，連接對應的content。就可以記錄到對應的輸入內容
    user_id = request.session.get('user_id')
    if not user_id:
        return RedirectResponse(url="/error?message=Database error", status_code=400)
    
    try:
        #連接到檔案數據庫
        conn = mysql.connector.connect(
             user="root",
            password="Qoo9898t@",
            host="localhost",
            database="website"
        )
        cursor = conn.cursor()
        #重點!!!!將新的留言推送至MYSQL資料庫message資料表。
        cursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)", (user_id, content))
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Database Error: {e}")
        conn.rollback()
        return RedirectResponse(url="/error?message=Database error", status_code=500)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    #成功後重新導向至/member，看新增的留言
    return RedirectResponse(url="/member", status_code=303)    

#(與Week4不同,/member新增顯示動態留言板)流程3，定義member與error頁面導向
@app.get("/member")
def member_page(request: Request):
    #定義對話登入狀態
    if 'SIGNED-IN' not in request.session or not request.session['SIGNED-IN']:
        #如果使用者未登入，則導回首頁(避免未登入的使用者直接輸入網址闖關)
        return RedirectResponse(url="/", status_code=303)
    #連接資料庫(獲取messege訊息)
    try:
        conn = mysql.connector.connect(
            user="root",
            password="Qoo9898t@",
            host="localhost",
            database="website"
        )
        cursor = conn.cursor()
        #查詢message資料表內content的資料，並關聯到member資料表name
        cursor.execute("select member.name, message.content from message inner join member on message.member_id = member.id ORDER BY message.time DESC;")
        messages = cursor.fetchall()
        #擷取用戶名稱
        name = request.session.get('name')
        # 返回带有消息数据的会员页面
        return templates.TemplateResponse("member.html", {
            "request": request,
            "name": name,  # 传递用户名到模板
            "messages": messages  # 传递消息数据到模板
        })
    except mysql.connector.Error as e:
        print(f"Database Error: {e}")
        return templates.TemplateResponse("error.html", {
            "request": request,
            "message": "Database error."
        })
    finally:
        cursor.close()
        conn.close()

#Week 7，新增會員查詢API
@app.get("/api/member")
def get_member(request: Request, username: Optional[str]=None ):
#定義對話登入狀態
    if 'SIGNED-IN' not in request.session or not request.session['SIGNED-IN']:
        #如果使用者未登入，則導回首頁(避免未登入的使用者直接輸入網址闖關)
        return RedirectResponse(url="/", status_code=303)
    #如果使用者沒有輸入資料就送出請求，直接返為原介面
    if not username:
        return RedirectResponse(url="/", status_code=303)
    
    try:
        #連接到資料庫
        conn=mysql.connector.connect(
            user="root",
            password="Qoo9898t@",
            host="localhost",
            database="website"
        )
        cursor = conn.cursor(dictionary=True)
    
    #查詢會員資料
        cursor.execute("SELECT id, name, username FROM member WHERE username = %s", (username,))
        member = cursor.fetchone()

        if member is not None:
            response = {"data": member}
        else:
            response = {"data": None}
        
        return JSONResponse(content=response)
    
    except mysql.connector.Error as e:
        print(f"Database Error: {e}")
        return templates.TemplateResponse("error.html", {
            "request": request,
            "message": "Database error."
        })
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.patch("/api/member")
async def update_member_name(request: Request):
    if 'SIGNED-IN' not in request.session or not request.session['SIGNED-IN']:
        return JSONResponse(content={"error": True}, status_code=403)

    user_id = request.session.get('user_id')
    
    try:
        data = await request.json()  # 读取并解析请求体为JSON (await是一種異步處理的方法)
        new_name = data.get("name")  # 获取新的姓名字段
        if not new_name:
            return JSONResponse(content={"error": True}, status_code=400)
    
        conn = mysql.connector.connect(
            user="root",
            password="Qoo9898t@",
            host="localhost",
            database="website"
        )
        cursor = conn.cursor()
        
        cursor.execute("UPDATE member SET name = %s WHERE id = %s", (new_name, user_id))
        conn.commit()

        return JSONResponse(content={"ok": True}, status_code=200)
    
    except mysql.connector.Error as e:
        print(f"Database Error: {e}")
        return JSONResponse(content={"error": True}, status_code=500)
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()            

@app.get("/error")
def error_page(request: Request, message: str):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

#(與Week4不同，完全刪除登入的狀態)流程4，signout處理
@app.get("/signout")
def signout(request: Request):
    #完全清空登入的狀態(确保在用户登出时不留下任何可用的会话数据)
    #request.session['SIGNED-IN'] = False
    request.session.clear()
    return RedirectResponse(url="/", status_code=303)


#(類別0)打下面這串，可比不用透過終端機執行
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)



# 状态码 500 用于数据库操作失败的情况。如果执行数据库查询或更新时出现异常（如 SQL 错误、数据库连接问题等），这通常是服务器端的错误，客户端无法通过修改请求来解决，因此返回 500。
# 状态码 400 用于当请求中缺少必需的数据或数据格式不正确时。例如，如果用户未提供必需的表单数据或会话中缺失关键信息（如 user_id），则表明请求是不合适的，因此返回 400。
# 状态码 303 用于在操作成功后，需要将用户重定向到另一个页面时。例如，在用户成功登录、注册或提交表单后，为了防止用户刷新页面导致重复提交，服务器会发送一个 303 状态码，并在响应头中指定一个新的 URL，客户端浏览器会自动重定向到这个新 URL。



