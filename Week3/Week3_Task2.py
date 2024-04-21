#抓取PTT彩票版的網頁原始碼(HTML)
import urllib.request as req

#寫入CSV檔案
import csv
#呼叫結果的函示，把results寫進CSV
def write_results_to_csv_manual(results):
    with open("article.csv", mode='w', newline='', encoding='utf-8-sig') as file:
        # 寫入標題行
        file.write("article_title,number_text,article_date\n")
        # 寫入數據
        for article_title, number_text, article_date in results:
            # 將每個值之間用逗號分隔，並在每行的結尾加上換行符
            file.write(f"{article_title},{number_text},{article_date}\n")

#第一組函式用來處理原始ptt彩票版每個標題內連結的網頁，並且爬取"時間"文字內span的文字
def get_article_date(article_url):
    #建立一個Request物件，附件Request Headers 的資訊
    #"cookie": "over18=1"用來攜帶該cookie值，解決18禁頁面阻擋的問題
    request = req.Request(article_url, headers={
        "cookie": "over18=1",     
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    #解析網頁原始碼，取得該頁面下特定的文字訊息
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser") 
    meta_tags = root.find_all("span", class_="article-meta-tag")
    #因為"article-meta-tag"底下包含作者與時間兩種資料，我只要保留"時間"的就好，所以用迴圈搜尋剛剛爬出來的資料裡面....
    for meta_tag in meta_tags:
        if meta_tag.text == "時間":
            date_span = meta_tag.find_next_sibling("span", class_="article-meta-value")
            return date_span.text if date_span else "Date not found"
    
    return "Date not found"


def getData(url):
    #建立一個Request物件，附件Request Headers 的資訊
    #"cookie": "over18=1"用來攜帶該cookie值，解決18禁頁面阻擋的問題
    request = req.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    #解析網頁原始碼，取得該頁面下的標題與按讚數
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser") 
    titles = root.find_all("div", class_="title")    #title於HTML中的位置
    goodnumbers=root.find_all("div", class_="nrec")  #按讚數(變數名稱取名叫做goodnumbers)於HTML中的位置
    
    #這裡用zip函式，可以套用在迴圈中，把資訊以tuple型態記錄起來
    results=[] #創立空的list，用來裝入結果，這是最後加的
    for title,number in zip(titles,goodnumbers):
        #先找title,假設title的<a>標籤內不為空值None，則:輸出標題(article_title = title.a.string)
        if title.a is not None:
            article_title = title.a.string
            #伴隨題目要求要進一步爬蟲title頁面內時間的資訊，於外部撰寫了另一個函式(get_article_date)，於此迴圈呼叫進來，以遍歷時間的資料
            article_url = "https://www.ptt.cc" + title.a['href']
            article_date = get_article_date(article_url)
            #印出檢查標題、時間
            # print(article_title)
            # print(article_date)
        #觀察原始程式碼，如果title標籤內沒有<a標籤>，則直接列印title標籤內所含的文字，使用title.get_text(strip=True)抓取文字段。(這段程式碼是針對網頁內顯示:(本文已被刪除) [saquchhh])
        else:
            article_title =title.get_text(strip=True)
            # print(title.get_text(strip=True))

        #處理按讚數
        if number.span is not None:
            number_text=number.get_text(strip=True)
        else:
            number_text="0"
        # #印出檢查
        # print(number_text)    
        results.append((article_title,number_text,article_date))



    # 爬取下一頁的連結
    next_link = root.find("a", string="‹ 上頁")
    return results,"https://www.ptt.cc" + next_link["href"] if next_link else None

# 主程式
page_url = "https://www.ptt.cc/bbs/Lottery/index.html"
all_results = []
count = 0
while count < 3 and page_url:
    new_results, page_url = getData(page_url)
    # page_url = getData(page_url)
    all_results.extend(new_results)
    count += 1
# 最後將所有累積的結果寫入 CSV 檔案
write_results_to_csv_manual(all_results)

