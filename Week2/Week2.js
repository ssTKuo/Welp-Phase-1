// Tesk 4
// *********************************************************************************************************************************
// #透過觀察數列規律，數列從0開始，以+4，+4，+1的規律運算，且每次跌代的總和為7。
// #index為索引值，將Index/3觀察餘數，配合+4，+4，-1的規律，餘數為1則該index對應的X值應該要+4；餘數為2則該index對應的X值應該要+8
// #若index整除3，則不須另外處理。
// #接著處理Index對應的數值，第一回跌代之數字為7，index/3得知跌代了幾次，X可以直接*7
// math.floor函數將一個浮點數向下取整至最接近的整數
function getNumber(index) {
  if (index % 3 === 1) {
    let X = Math.floor(index / 3) * 7;
    console.log(X + 4);
  } else if (index % 3 === 2) {
    let X = Math.floor(index / 3) * 7;
    console.log(X + 8);
  } else if (index === 0) {
    console.log(0);
  } else {
    console.log(Math.floor(index / 3) * 7);
  }
}
getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70
// *********************************************************************************************************************************

// Tesk 3
// *********************************************************************************************************************************
function func(...data) {
  // 創建一List(namelist)，用來存放*data丟進來的資料
  let namelist = [];
  data.forEach((name) => {
    namelist.push(name);
  });

  // 創建一個List(checkwordslist),檢查(namelist)內各元素字數，並紀錄於List(checkwordslist)
  let checkwordslist = [];
  namelist.forEach((name) => {
    checkwordslist.push(name.length);
  });

  // 判定List(checkwordslist)的元素要對應List(namelist)中的哪一項
  let onewordslist = [];
  checkwordslist.forEach((length, index) => {
    if (length === 2 || length === 3) {
      onewordslist.push(namelist[index][1]);
    } else if (length === 4 || length === 5) {
      onewordslist.push(namelist[index][2]);
    } else {
      console.log("名字長度不符合規定");
    }
  });

  // 比較List(onewordslist)中，是否有哪個元素與其他元素不一樣
  let countDict = {};
  onewordslist.forEach((word) => {
    if (countDict[word]) {
      countDict[word] += 1;
    } else {
      countDict[word] = 1;
    }
  });

  // 找出字典裡，哪個Key對應的數值是最小的,並把Key值丟到一個新的List(minvaule_word)
  let uniqueWords = [];
  for (let [word, count] of Object.entries(countDict)) {
    if (count === 1) {
      uniqueWords.push(word);
    }
  }

  // 將只出現一次的文字反推回namelist=[]，查詢完整字串
  let uniqueNames = [];
  uniqueWords.forEach((uniqueWord) => {
    let index = onewordslist.indexOf(uniqueWord);
    uniqueNames.push(namelist[index]);
  });

  // 最後再判定，如果unique_names:沒有東西的狀況下，就是沒有單字只出現一次(有重複的意思)
  if (uniqueNames.length === 0) {
    console.log("沒有");
  } else {
    console.log(uniqueNames);
  }
}
func("彭大牆", "陳王明雅", "吳明");
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花");
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花");
func("郭宣雅", "夏曼藍波安", "郭宣恆");
// *********************************************************************************************************************************
// Tesk 1
// *********************************************************************************************************************************
function findAndPrint(messages, currentStation) {
  // 直接建立包含站點與索引值的字典，小碧潭站特別處理，這邊用 const命名，
  const stationIndex = {
    Songshan: 0,
    "Nanjing Sanmin": 1,
    "Taipei Arena": 2,
    "Nanjing Fuxing": 3,
    "Songjiang Nanjing": 4,
    Zhongshan: 5,
    Beimen: 6,
    Ximen: 7,
    Xiaonanmen: 8,
    "Chiang Kai-shek Memorial Hall": 9,
    Guting: 10,
    "Taipower Building": 11,
    Gongguan: 12,
    Wanlong: 13,
    Jingmei: 14,
    Dapinglin: 15,
    Qizhang: 16,
    Xiaobitan: 16.5,
    "Xindian City Hall": 17,
    Xindian: 18,
  };

  // 剖析 messages，將其整理為人名:所在站點的形式
  const stationStorage = {};
  //   Object.entries() 來遍歷對象的鍵值對
  for (const [member, message] of Object.entries(messages)) {
    for (const station in stationIndex) {
      if (message.includes(station)) {
        stationStorage[member] = station;
      }
    }
  }
  //   console.log(stationStorage);

  // 找到最近的人
  let closestPerson = null;
  let minDistance = null;
  for (const [member, station] of Object.entries(stationStorage)) {
    let distance;
    if (station === "Xiaobitan" || currentStation === "Xiaobitan") {
      distance =
        Math.abs(stationIndex["Qizhang"] - stationIndex[station]) +
        Math.abs(stationIndex["Qizhang"] - stationIndex[currentStation]);
    } else {
      distance = Math.abs(stationIndex[currentStation] - stationIndex[station]);
    }

    if (minDistance === null || distance < minDistance) {
      minDistance = distance;
      closestPerson = member;
    }
  }
  console.log(closestPerson);
}

const messages = {
  Leslie: "I'm at home near Xiaobitan station.",
  Bob: "I'm at Ximen MRT station.",
  Mary: "I have a drink near Jingmei MRT station.",
  Copper: "I just saw a concert at Taipei Arena.",
  Vivian: "I'm at Xindian station waiting for you.",
};
findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian
// *********************************************************************************************************************************
// Tesk 2
// *********************************************************************************************************************************
function book(consultants, hour, duration, criteria) {
  // 確認每個顧問字典中是否含有 "schedule"，如果"沒有"則添加上去
  //使用 forEach 方法來迭代陣列
  if (!("schedule" in consultants[0])) {
    consultants.forEach((consultant) => {
      consultant.schedule = [];
    });
  }

  const start_time = hour;
  const end_time = hour + duration;

  // 找出有空的顧問
  let available_consultants = [];
  consultants.forEach((consultant) => {
    let overlap = false;
    consultant.schedule.forEach(([s, e]) => {
      if (s < end_time && start_time < e) {
        overlap = true;
      }
    });
    if (!overlap) {
      available_consultants.push(consultant);
    }
  });

  if (available_consultants.length === 0) {
    console.log("No Service");
    return;
  }

  // 根據 criteria 選擇顧問
  let chosen_consultant = null;
  if (criteria === "price") {
    let lowest_price = null;
    available_consultants.forEach((consultant) => {
      if (lowest_price === null || consultant.price < lowest_price) {
        lowest_price = consultant.price;
        chosen_consultant = consultant;
      }
    });
  } else if (criteria === "rate") {
    let highest_rate = null;
    available_consultants.forEach((consultant) => {
      if (highest_rate === null || consultant.rate > highest_rate) {
        highest_rate = consultant.rate;
        chosen_consultant = consultant;
      }
    });
  }

  // 更新選定顧問的預約時間
  chosen_consultant.schedule.push([start_time, end_time]);
  console.log(chosen_consultant.name);
}

const consultants = [
  { name: "John", rate: 4.5, price: 1000 },
  { name: "Bob", rate: 3, price: 1200 },
  { name: "Jenny", rate: 3.8, price: 800 },
];

book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob (overlap with Jenny's booking)
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John (overlap with Jenny's booking)
// *********************************************************************************************************************************
