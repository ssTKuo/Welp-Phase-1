#********************************************************************************************************

#處理景點、行政區，經緯度、url的任務(spot.csv任務)

#第一步驟:用網路連線的方式，分別對src1,src2連線並打開
import urllib.request as request

src1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
src2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

# 讀取第一個資源
with request.urlopen(src1) as response1:
    data1 = response1.read().decode('utf-8') 

# 讀取第二個資源
with request.urlopen(src2) as response2:
    data2 = response2.read().decode('utf-8') 

# print(data1)
# print(data2)
#檢查後發現為JSON格式的資料(用大括號 {} 包裹的數據結構，這裡的對象包含一個名為 data 的鍵。)

#**************************************************

#第二步驟，透過impor json來導入網路資料，到IDE上進行分析；此處使用json.loads(data1,2)，注意!!是有s的load
import json
data_read1=json.loads(data1) 
data_read2=json.loads(data2) 


#data_read2分析
#創建一個空的字典來存放'SERIAL_NO'與'address'
serial_to_address = {}
#遍歷data_read2['data']中的項目
for item in data_read2['data']:
    #將每個 SERIAL_NO 做為key，address作為value，存放到字典裡
    serial_to_address[item['SERIAL_NO']] = item['address']
    # print(serial_to_address)



#data_read1分析
#檢查並print出景點名稱，確認一下資料的格式 字典-字典-List當中的第0項(也是個字典)-字典
# print(data_read1["data"]["results"][0]["stitle"]) 得到"新北投溫泉區"

#看一下總共有多少站點()，用len檢查["results"]
list_length=len(data_read1["data"]["results"])
# print(list_length)  答案是58個景點(可以用來做最終確認)
#用迴圈遍歷出data_read1我們要的資料(stitle,longitude,latitude,filelist)
list1=[]
for item in data_read1["data"]["results"]:
    #item["filelist"]內的東西是一串相連的url網址,但是有些中間有空格或沒空格的狀況，先處理空格(用replace替代)，讓他們連再一起
    filelist_no_spaces = item["filelist"].replace(" ", "")
    #此時filelist_no_spaces內已經是一串相連的url網址，都以.jpg(有大寫，有小寫)作為結尾，先轉換為全小寫，再透過.split("jpg")將牠們分開
    urls=filelist_no_spaces.lower().split(".jpg")
    #print(urls) 這邊print的資料如下:

    # urls = [
    # 'https://www.travel.taipei/d_upload_ttn/sceneadmin/pic/11000848',
    # 'https://www.travel.taipei/d_upload_ttn/sceneadmin/pic/11002891',
    # 'https://www.travel.taipei/d_upload_ttn/sceneadmin/image/a0/b0/c0/d315/e70/f65/1e0951fb-069f-4b13-b5ca-2d09df1d3d90',
    # 'https://www.travel.taipei/d_upload_ttn/sceneadmin/image/a0/b0/c0/d260/e538/f274/e7d482ba-e3c0-40c3-87ef-3f2a1c93edfa',
    # 'https://www.travel.taipei/d_upload_ttn/sceneadmin/image/a0/b0/c0/d919/e767/f581/9ddde70e-55c2-4cf0-bd3d-7a8450582e55',
    # 'https://www.travel.taipei/d_upload_ttn/sceneadmin/image/a0/b0/c1/d28/e891/f188/77a58890-7711-4ca2-aebe-4aa379726575',
    # '' ] #最後一個元素是空的，下一個步驟是把.jpg加回去，但不理會這個空值
    
    #把urls列表中的每個元素都加上.jpg，除了最後一個不用
    re_urls=[]
    for i in range(len(urls) - 1):
        re_urls.append(urls[i] + ".jpg")
    # print(re_urls)
     

    #尋找第一個以.jpg結尾的url
    first_jpg_url = None
    for url in re_urls:
        if url.endswith('.jpg'):
            first_jpg_url=url
            break

    #把剛剛data_read2分析的結果(鍵:值)
    address = serial_to_address.get(item["SERIAL_NO"], "Address not found")
    #提取address內的行政區字串，先處理空值，用replace把address內的空值補起來
    re_address=address.replace(" ","")
    # print(re_address)
    cutcity_address=re_address.split("臺北市")
    # print(cutcity_address)
    #把['', '北投區中山路2號']合起來變成['北投區中山路2號']
    combined_cutcity_address=" ".join(cutcity_address)
    #print(combined_cutcity_address)
    district_name =combined_cutcity_address[0:4] 
    # print(district_name)

    list1.append([item["stitle"],district_name,item["longitude"],item["latitude"],first_jpg_url])

# print(list1)
# list1_length=len(list1)
# print(list1_length)  #確認處理了58組!!!

#**************************************************

import csv
with open("spot.csv", mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)  

    #加入自訂表頭 
    headers = ["SpotTitle", "District", "Longitude", "Latitude", "ImageURL"]
    writer.writerow(headers)

    for item in list1:
        writer.writerow(item)

#********************************************************************************************************

#處理捷運站對應的景點(mrt.csv任務)

#第一步:從data_read1中提取SERIAL_NO和stitle
serial_to_stitle = {}
for item in data_read1["data"]["results"]:
    serial_no = item["SERIAL_NO"]
    stitle = item["stitle"]
    serial_to_stitle[serial_no] = stitle

#第二步:從data_read2中提取SERIAL_NO和對應的MTR站
serial_to_mrt = {}
for item in data_read2["data"]:
    serial_no = item["SERIAL_NO"]
    mrt = item["MRT"]
    serial_to_mrt[serial_no] = mrt

#第三部:構建MRT到stitle對應的關係
mrt_to_stitle_list = {}
for serial_no, stitle in serial_to_stitle.items():
    if serial_no in serial_to_mrt:
        mrt_station = serial_to_mrt[serial_no]
        if mrt_station in mrt_to_stitle_list:
            mrt_to_stitle_list[mrt_station].append(stitle)
        else:
            mrt_to_stitle_list[mrt_station] = [stitle]

#print出，檢查結果
# for mrt, titles in mrt_to_stitle_list.items():
#     print(f"{mrt},{','.join(titles)}")
    

#**************************************************

import csv
with open("mrt.csv", mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)  

    # 加入自訂表頭 
    headers = ["MRT", "stitle"]
    writer.writerow(headers)

    #因為mrt_result 字典內包含兩種東西: 捷運站、景點(數量不定)，所以將每個MRT對應的多個stitle合併為一個字串(中間用逗號格咖)
    for mrt, titles in mrt_to_stitle_list.items():
        #使用逗號將所有 stitle 合併成一單一儲存格內的字符串
        stitle_combined = ', '.join(titles)
        #寫入同一行數據
        writer.writerow([mrt, stitle_combined])



import csv

with open("mrt.csv", mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)  
    
    #確定最大的景點數量以創建足夠的列  
    max_titles = max(len(titles) for titles in mrt_to_stitle_list.values())
    #加入自訂表頭
    headers = ["MRT"] + [f"stitle_{i+1}" for i in range(max_titles)]
    writer.writerow(headers)

    #寫入CSV，每個景點在單獨的列
    for mrt, titles in mrt_to_stitle_list.items():
        #空格符號替代空值填
        row = [mrt] + titles + [''] * (max_titles - len(titles))
        writer.writerow(row)
#********************************************************************************************************