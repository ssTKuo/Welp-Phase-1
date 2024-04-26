import uvicorn                                               #(類別0)導入uvicorn，不用終端機執行用

from fastapi import FastAPI, Request ,Form                     #導入FastAPI主模塊，Form是給HTML文件用的

from fastapi.staticfiles import StaticFiles                  #(類別1)FastAPI的一个模块，用于服务静态文件(HTML、CSS),这些文件可以通过 HTTP 被访问。使用 StaticFiles 模块时，你会指定一个目录作为静态文件的根目录。FastAPI 会自动服务这个目录下的所有文件。这样，你就不需要为目录下的每个文件编写单独的路由。
from fastapi.templating import Jinja2Templates               #(類別2)導入模板
from fastapi.responses import HTMLResponse #JSONResponse     #(類別3)FastAPI内建的一个响应类，用于直接返回HTML内容。如果你的API需要返回 HTML（那就導入HTMLResponse），如果想要回傳字典（那就導入JSONResponse），本題目兩者皆用不到
from fastapi.responses import RedirectResponse               #(類別4)這題目應該用這個就好，重新導向一個地址的意思
from typing import Optional                                  #導入可選參數的模組，這邊應用在流程2裡面，讓帳號密碼是可選輸入
from starlette.middleware.sessions import SessionMiddleware  #(類別5)導入中間件模組

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

#流程2，用戶填寫帳號密碼後，點擊登入按鈕，瀏覽器發送HTTP POST請求到/signin路徑。login函數會合對用戶輸入的帳密，如果匹配成功，則回傳登入成功的JSON響應。
@app.post("/signin")
def login(request: Request,username: Optional[str] = Form(None), password: Optional[str] = Form(None)):
    if not username and not password:
        return RedirectResponse(url="/error?message=Please enter username and password", status_code=303)
    elif not username:
        return RedirectResponse(url="/error?message=Please enter username", status_code=303)
    elif not password:
        return RedirectResponse(url="/error?message=Please enter password", status_code=303)
    elif username != "test" or password != "test":
        return RedirectResponse(url="/error?message=Username or password is not correct", status_code=303)
    else:
        #如果用戶名和密碼驗證成功，設置對話狀態為以登入
        request.session['SIGNED-IN'] = True
        return RedirectResponse(url="/member", status_code=303)
    


#流程3，定義member與error頁面導向
@app.get("/member")
def member_page(request: Request):
    #定義會話為登入的狀態
    if request.session.get('SIGNED-IN'):
        return templates.TemplateResponse("member.html", {"request": request})
    else:
        return RedirectResponse(url="/", status_code=303)

@app.get("/error")
def error_page(request: Request, message: str):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

#流程4，signout處理
@app.get("/signout")
def signout(request: Request):
    #減除登入狀態，導向回url="/"路徑
    request.session['SIGNED-IN'] = False
    return RedirectResponse(url="/", status_code=303)

# 如果是要回傳json資料，可以這樣寫
#***************************************************************************
# @app.post("/login")
# def login(username: str = Form(...), password: str = Form(...)):
#     if username == "test" and password == "test":
#         # 登录成功，可能会返回一个重定向到另一个页面的响应
#         return {"message": "登录成功"}
#     else:
#         # 登录失败，返回登录页面和错误信息
#         return {"message": "登录失敗"}
#*************************************************************************** 

#如果是要回傳json與HTML 則可這樣寫
#***************************************************************************
# from fastapi import FastAPI, Form
# from fastapi.responses import HTMLResponse, JSONResponse
# app = FastAPI()
# @app.post("/login")
# def login(username: str = Form(...), password: str = Form(...)):
#     if username == "test" and password == "test":
#         # 登录成功，返回 JSON 响应
#         return JSONResponse(content={"message": "登录成功"}, status_code=200)
#     else:
#         # 登录失败，返回 HTML 响应
#         return HTMLResponse(content="<p>Login Failed</p>", status_code=200)
#***************************************************************************

#(類別0)打下面這串，可比不用透過終端機執行
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)







