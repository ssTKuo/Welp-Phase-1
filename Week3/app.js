// 製作popup視窗
function pupup() {
  let showMenu = document.querySelector("#menuOverlay");
  if (showMenu.style.display === "block") {
    showMenu.style.display = "none";
  } else {
    showMenu.style.display = "block";
  }
}

function closepupup() {
  let closeMenu = document.querySelector("#menuOverlay");
  closeMenu.style.display = "none";
}

// 導入JSON(fetch)
function loadData() {
  return fetch(
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
  )
    .then(function (response) {
      return response.json(); //因為是json檔案所以 return response.json 來處理檔案
    })
    .then(function (data) {
      console.log(data);
      return data; // 儲存成data ,return返回數據，以便後面處理
    });
}

function processSpotsData(data) {
  return data.data.results.map(function (spot) {
    // 從 filelist 擷取第一個URL
    let firstImageUrl = "https://" + spot.filelist.split("https://")[1];

    // 返回一個物件，物件包含景點名稱與第一個URL
    let spotData = {
      title: spot.stitle, // 景點的標題
      imageUrl: firstImageUrl, // 第一張圖片的URL
    };
    // console.log(spotData); // 檢查一下
    return spotData;
  });
}

document.addEventListener("DOMContentLoaded", function () {
  loadData()
    .then(processSpotsData)
    .then(function (spots) {
      let container = document.querySelector(".container"); // DOM回.container

      // 用for迴圈創建並更新promotion區塊 (我有3塊，所以寫i<3)
      for (let i = 0; i < 3; i++) {
        let targetElement = document.querySelector(
          `.promotion.promotion${i + 1}` //`.promotion.promotion${i + 1}`:這段程式碼使用模板字符串語法，用反引號框起來，表示要在字串符內插入遍量i值，並加1上去，這邊用來動態生成promotion1-3
        ); // 一次抓三個promotion

        //創建3個新的promotion區塊(寫在foe回圈內)
        let newPromotion = document.createElement("div");
        newPromotion.className = `js_promotion js_promotion${i + 1}`;

        let newImageDiv = document.createElement("div");
        newImageDiv.className = "js_image";
        let newImage = document.createElement("img");
        newImage.src = spots[i].imageUrl;
        newImage.alt = "Taiwan";
        newImageDiv.appendChild(newImage);

        let newTextDiv = document.createElement("div");
        newTextDiv.className = "js_text";
        newTextDiv.textContent = spots[i].title;
        newPromotion.appendChild(newImageDiv);
        newPromotion.appendChild(newTextDiv);

        // 使用.replaceChild替換原來的 promotion 區塊
        container.replaceChild(newPromotion, targetElement);
      }

      // 用for迴圈創建並更新title區塊 (我有10塊，所以寫i<10)
      for (let i = 1; i <= 10; i++) {
        let targetTitleElement = document.querySelector(`.title.title${i}`);

        // 创建新的 title 区块
        let newTitle = document.createElement("div");
        newTitle.className = `js_title js_title${i}`;

        let newImage1Div = document.createElement("div");
        newImage1Div.className = "js_image1";
        let newImage1 = document.createElement("img");
        newImage1.src = spots[i + 2].imageUrl; // 第 3 到 12 個景點圖片URL
        newImage1.alt = "Taiwan";
        newImage1Div.appendChild(newImage1);

        let newImage2Div = document.createElement("div");
        newImage2Div.className = "js_image2";
        let newImage2 = document.createElement("img");
        newImage2.src = "./images/541415.png"; // 維持原本的圖片
        newImage2.alt = "Star";
        newImage2Div.appendChild(newImage2);

        let newTextDiv = document.createElement("div");
        newTextDiv.className = "js_text";
        newTextDiv.textContent = spots[i + 2].title; // 第 3 到 12 個景點迷稱
        newTitle.appendChild(newImage1Div);
        newTitle.appendChild(newImage2Div);
        newTitle.appendChild(newTextDiv);

        // 替換原來的 title區塊
        container.replaceChild(newTitle, targetTitleElement);
      }
    });
});
