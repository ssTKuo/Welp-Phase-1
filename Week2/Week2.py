#Tesk 4
#********************************************************************************************************************
#解題思路:
#透過觀察數列規律，數列從0開始，以+4，+4，+1的規律運算，且每次跌代的總和為7。
#index為索引值，將Index/3觀察餘數，配合+4，+4，-1的規律，餘數為1則該index對應的X值應該要+4；餘數為2則該index對應的X值應該要+8
#若index整除3，則不須另外處理。
#接著處理Index對應的數值，第一回跌代之數字為7，index/3得知跌代了幾次，X可以直接*7
def get_number(index):
    if index % 3 == 1:
        X = (index // 3) * 7
        print(X + 4)          #餘數為1的狀況下，對應初始數列關係應+4
    elif index % 3 == 2:
        X = (index // 3) * 7  
        print(X + 8)          #餘數為2的狀況下，對應初始數列關係應+8
    elif index == 0:
        print(0)
    else:
        print((index // 3) * 7)  #整除狀況下，則直接代表7循環了幾次
get_number(0)
get_number(1)
get_number(2)
get_number(3)
get_number(4)
get_number(5)
get_number(6)
get_number(10)
get_number(30)
#********************************************************************************************************************
#Tesk 3
#********************************************************************************************************************
def func(*data):
 #創建一List(namelist)，用來存放*data丟進來的資料
 namelist=[]
 for name in data:
     namelist.append(name)
#  print(namelist)
 #創建一個List(checkwordslist),檢查(namelist)內各元素字數，並紀錄於List(checkwordslist)
 checkwordslist=[]
 for words in namelist:
     checkwordslist.append(len(words))
#  print(checkwordslist)
 #判定List(checkwordslist)的元素要對應List(namelist)中的哪一項
 onewordslist=[]
 for index in range(len(checkwordslist)):
    if checkwordslist[index] == 2:
        onewordslist.append(namelist[index][1])
    elif checkwordslist[index] == 3:
        onewordslist.append(namelist[index][1])
    elif checkwordslist[index] == 4:
        onewordslist.append(namelist[index][2])
    elif checkwordslist[index] == 5:
        onewordslist.append(namelist[index][2])
    else:
        print("名字長度不符合規定")
#  print(onewordslist):出現['靜', '立', '靜', '立', '花']
 #比較List(onewordslist)中，是否有哪個元素與其他元素不一樣
 count_dict={}
 for word in onewordslist:
   #   print(word)
     if word in count_dict:  #假設word已經出現在count_dict字典中，則:
         count_dict[word]= count_dict[word]+1
     else: count_dict[word]= 1
#  print (count_dict) :出現{'靜': 2, '立': 2, '花': 1}
 #找出字典裡，哪個Key對應的數值是最小的,並把Key值丟到一個新的List(minvaule_word)
 unique_words = []
 for word, count in count_dict.items():  #使用兩個參數的方式，將字典的成對資料以Tuple方式丟回 unique_words = []
    if count == 1:
        unique_words.append(word)
#  print(unique_words):出現['花']
#將只出現一次的文字反推回namelist=[]，查詢完整字串，首先創立一List(unique_names)，用for迴圈把unique_words(這個陣列只會有一個字)，丟到新的List(unique_names)
 unique_names=[]
 for unique_word in unique_words:
        index = onewordslist.index(unique_word)  # 找到該字在onewordslist['靜', '立', '靜', '立', '花']中的索引，變數index=['靜', '立', '靜', '立', '花'].index['花']，這邊會跑出index=4
        unique_names.append(namelist[index])  # 使用該索引從namelist中找到完整名字,放到新建立的List(unique_names)中,因為在索引值為4，對應到第五個項次"林花花"
 #print出(unique_names)
#最後再判定，如果unique_names:沒有東西的狀況下，就是沒有單字只出現一次(有重複的意思)
 if not unique_names:  # 如果unique_names為空
    print("沒有")
 else:
    print(unique_names)  # 如果unique_names不為空，打印列表内容

func("彭大牆", "陳王明雅", "吳明") 
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花")    
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") 
func("郭宣雅", "夏曼藍波安", "郭宣恆") 
#********************************************************************************************************************
#Tesk 1
#********************************************************************************************************************
def find_and_print(messages, current_station):
    #將松山新店線上所有站名，裝進一個list
    # greenLine=["Songshan","Nanjing Sanmin","Taipei Arena","Nanjing Fuxing","Songjiang Nanjing","Zhongshan","Beimen","Ximen","Xiaonanmen","Chiang Kai-shek Memorial Hall","Guting","Taipower Building","Gongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xiaobitan","Xindian City Hall","Xindian"]
     
    #直接建立含有站點:索引值的字典，小碧潭站特別處理
    station_index={"Songshan": 0, "Nanjing Sanmin": 1, "Taipei Arena": 2, "Nanjing Fuxing": 3,
        "Songjiang Nanjing": 4, "Zhongshan": 5, "Beimen": 6, "Ximen": 7,
        "Xiaonanmen": 8, "Chiang Kai-shek Memorial Hall": 9, "Guting": 10,
        "Taipower Building": 11, "Gongguan": 12, "Wanlong": 13, "Jingmei": 14,
        "Dapinglin": 15, "Qizhang": 16, "Xiaobitan": 16.5,  
        "Xindian City Hall": 17, "Xindian": 18}

    #********棄用********
    # #創立一個空的字典，表示greenLine中各站點的索引值(小碧潭站及之後的站另外處理)
    # station_index={}
    # index=0 #索引編號初始值
    # for station in greenLine:
    #     station_index[station]=index
    #     index=index+1
    #     station_index['Xiaobitan']=16.1
    #     station_index['Xindian City Hall']=17
    #     station_index['Xindian']=18
    # print(station_index)  #這邊會print出station_index = {"Songshan": 0, "Nanjing Sanmin": 1,....}
    #********棄用********
    
    #剖析def函式外部messages，把它整理為人名:站點的形式。想法是將messages與greenLine比對
    #拆解messages~。創建一個空的字典，來存放最終剖析的結果，如:{Leslie: Xiaobitan,Bob: Ximen...}
    station_storage={}
    #首先用迴圈過一次messages，messages用.item()做成data = [("apple", 150), ("banana", 300), ("cherry", 75)]這種形式，再解包給變數person(對應到原字典的鍵)、message(對應到原字典的值)
    for member, message in messages.items():
        #逐一檢視 station_index 字典中的每一個站點名稱，並放進變數station中
        for station in station_index:  #如果不使用任何方法，如 .items(), .keys(), 或 .values(), 則預設情況下會迭代字典的鍵（keys）
            #如果station有出現在 message...
            if station in message:
                #則在station_storage字典中記錄下來
                station_storage[member]=station
    print(station_storage)  #{Leslie: Xiaobitan,Bob: Ximen...}

    #找到最近的人
    closest_person = None
    min_distance = None #暫定為none,用來保存以下每次疊代後發現的最小值
    for member, station in station_storage.items():
        #小碧潭站的距離要加上到七張站距離(0.5)，再與其他站點比較
        if station == 'Xiaobitan' or current_station == 'Xiaobitan':
            distance = (abs(station_index['Qizhang'] - station_index[station]) +
                    abs(station_index['Qizhang'] - station_index[current_station]))
        else:
            distance = abs(station_index[current_station] - station_index[station])

        if min_distance is None or distance < min_distance:
            min_distance = distance
            closest_person = member
    print(closest_person)


messages={"Leslie":"I'm at home near Xiaobitan station.","Bob":"I'm at Ximen MRT station.","Mary":"I have a drink near Jingmei MRT station.","Copper":"I just saw a concert at Taipei Arena.","Vivian":"I'm at Xindian station waiting for you."}
# find_and_print(messages, "Wanlong") # print Mary
# find_and_print(messages, "Songshan") # print Copper
# find_and_print(messages, "Qizhang") # print Leslie
# find_and_print(messages, "Ximen") # print Bob
# find_and_print(messages, "Xindian City Hall") # print Vivian 
find_and_print(messages, "Xiaobitan")# print Leslie
#********************************************************************************************************************
#Tesk 2
#********************************************************************************************************************
def book(consultants, hour, duration, criteria):
    #先在原始的consultants中給每個字典內添加新的鍵對值("schedule":空白)
    if "schedule" not in consultants[0]: #檢查第一個顧問中是否含有"schedule"，如果沒有即建立
        for everydic in consultants:     #每個字典都新增"schedule":[]
            everydic["schedule"]=[]        
    # print (consultants)
    
    start_time=hour
    end_time=hour+duration
    
    #哪個顧問有空
    available_consultants = []
    for consultant in consultants:
        overlap = False
        for (s, e) in consultant['schedule']:
            if s < end_time and start_time < e:  # 時間重疊條件
                overlap = True
                break
        if not overlap:
            available_consultants.append(consultant)

    if not available_consultants:
        print("No Service")
        return
    
    #根據criteria選擇顧問
    chosen_consultant = None
    if criteria == "price":
        # 找價格最低的人
        lowest_price = None
        for consultant in available_consultants:   #從有空的顧問來找
            if lowest_price is None or consultant['price'] < lowest_price:
                lowest_price = consultant['price']
                chosen_consultant = consultant
    elif criteria == "rate":
        # 找平方高的人
        highest_rate = None
        for consultant in available_consultants:
            if highest_rate is None or consultant['rate'] > highest_rate:
                highest_rate = consultant['rate']
                chosen_consultant = consultant
    
    #避免時間衝突，這邊更新時間
    chosen_consultant['schedule'].append((start_time, end_time))
    print(chosen_consultant["name"])

consultants = [
    {"name": "John", "rate": 4.5, "price": 1000},
    {"name": "Bob", "rate": 3, "price": 1200},
    {"name": "Jenny", "rate": 3.8, "price": 800}
]

book(consultants, 15, 1, "price")  # Jenny
book(consultants, 11, 2, "price")  # Jenny
book(consultants, 10, 2, "price")  # John
book(consultants, 20, 2, "rate")   # John
book(consultants, 11, 1, "rate")   # Bob (overlap with Jenny's booking)
book(consultants, 11, 2, "rate")   # No Service
book(consultants, 14, 3, "price")  # John (overlap with Jenny's booking)
#********************************************************************************************************************