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

      //創建新的區塊替代promotion1
      let targetElement1 = document.querySelector(".promotion.promotion1");
      let newPromotion1 = document.createElement("div");
      newPromotion1.className = "js_promotion js_promotion1";

      let newImageDiv1 = document.createElement("div");
      newImageDiv1.className = "js_image";
      let newImage1 = document.createElement("img");
      newImage1.src = spots[0].imageUrl; //從JSON數據(data)獲得第一個景點圖片的URL
      newImage1.alt = "Taiwan";
      newImageDiv1.appendChild(newImage1);

      let newTextDiv1 = document.createElement("div");
      newTextDiv1.className = "js_text";
      newTextDiv1.textContent = spots[0].title; //從JSON數據(data)獲得第一個景點的名稱
      newPromotion1.appendChild(newImageDiv1);
      newPromotion1.appendChild(newTextDiv1);

      container.replaceChild(newPromotion1, targetElement1); //直接用替換原本的promotion1

      //創建新的區塊替代promotion2
      let targetElement2 = document.querySelector(".promotion.promotion2");
      let newPromotion2 = document.createElement("div");
      newPromotion2.className = "js_promotion js_promotion2";

      let newImageDiv2 = document.createElement("div");
      newImageDiv2.className = "js_image";
      let newImage2 = document.createElement("img");
      newImage2.src = spots[1].imageUrl;
      newImage2.alt = "Taiwan";
      newImageDiv2.appendChild(newImage2);

      let newTextDiv2 = document.createElement("div");
      newTextDiv2.className = "js_text";
      newTextDiv2.textContent = spots[1].title;
      newPromotion2.appendChild(newImageDiv2);
      newPromotion2.appendChild(newTextDiv2);

      container.replaceChild(newPromotion2, targetElement2);

      //創建新的區塊替代promotion3
      let targetElement3 = document.querySelector(".promotion.promotion3");
      let newPromotion3 = document.createElement("div");
      newPromotion3.className = "js_promotion js_promotion3";

      let newImageDiv3 = document.createElement("div");
      newImageDiv3.className = "js_image";
      let newImage3 = document.createElement("img");
      newImage3.src = spots[2].imageUrl;
      newImage3.alt = "Taiwan";
      newImageDiv3.appendChild(newImage3);

      let newTextDiv3 = document.createElement("div");
      newTextDiv3.className = "js_text";
      newTextDiv3.textContent = spots[2].title;
      newPromotion3.appendChild(newImageDiv3);
      newPromotion3.appendChild(newTextDiv3);

      container.replaceChild(newPromotion3, targetElement3);

      // 創建並更新 title1
      let targetTitleElement1 = document.querySelector(".title.title1");
      let newTitle1 = document.createElement("div");
      newTitle1.className = "js_title js_title1";

      let newImage1Div1 = document.createElement("div");
      newImage1Div1.className = "js_image1";
      let newImage1_1 = document.createElement("img");
      newImage1_1.src = spots[3].imageUrl; // 獲取第四個景點的圖片 URL
      newImage1_1.alt = "Taiwan";
      newImage1Div1.appendChild(newImage1_1);

      let newImage2Div1 = document.createElement("div");
      newImage2Div1.className = "js_image2";
      let newImage2_1 = document.createElement("img");
      newImage2_1.src = "./images/541415.png"; // 假設第二張圖片不變
      newImage2_1.alt = "Star";
      newImage2Div1.appendChild(newImage2_1);

      let newTextDiv1_title1 = document.createElement("div");
      newTextDiv1_title1.className = "js_text";
      newTextDiv1_title1.textContent = spots[3].title; // 獲取第四個景點的名稱
      newTitle1.appendChild(newImage1Div1);
      newTitle1.appendChild(newImage2Div1);
      newTitle1.appendChild(newTextDiv1_title1);

      container.replaceChild(newTitle1, targetTitleElement1); // 替換原來的 title1

      // 創建並更新 title2
      let targetTitleElement2 = document.querySelector(".title.title2");
      let newTitle2 = document.createElement("div");
      newTitle2.className = "js_title js_title2";

      let newImage1Div2 = document.createElement("div");
      newImage1Div2.className = "js_image1";
      let newImage1_2 = document.createElement("img");
      newImage1_2.src = spots[4].imageUrl;
      newImage1_2.alt = "Taiwan";
      newImage1Div2.appendChild(newImage1_2);

      let newImage2Div2 = document.createElement("div");
      newImage2Div2.className = "js_image2";
      let newImage2_2 = document.createElement("img");
      newImage2_2.src = "./images/541415.png";
      newImage2_2.alt = "Star";
      newImage2Div2.appendChild(newImage2_2);

      let newTextDiv2_title2 = document.createElement("div");
      newTextDiv2_title2.className = "js_text";
      newTextDiv2_title2.textContent = spots[4].title;
      newTitle2.appendChild(newImage1Div2);
      newTitle2.appendChild(newImage2Div2);
      newTitle2.appendChild(newTextDiv2_title2);

      container.replaceChild(newTitle2, targetTitleElement2);

      // 創建並更新 title3
      let targetTitleElement3 = document.querySelector(".title.title3");
      let newTitle3 = document.createElement("div");
      newTitle3.className = "js_title js_title3";

      let newImage1Div3 = document.createElement("div");
      newImage1Div3.className = "js_image1";
      let newImage1_3 = document.createElement("img");
      newImage1_3.src = spots[5].imageUrl;
      newImage1_3.alt = "Taiwan";
      newImage1Div3.appendChild(newImage1_3);

      let newImage2Div3 = document.createElement("div");
      newImage2Div3.className = "js_image2";
      let newImage2_3 = document.createElement("img");
      newImage2_3.src = "./images/541415.png";
      newImage2_3.alt = "Star";
      newImage2Div3.appendChild(newImage2_3);

      let newTextDiv3_title3 = document.createElement("div");
      newTextDiv3_title3.className = "js_text";
      newTextDiv3_title3.textContent = spots[5].title;
      newTitle3.appendChild(newImage1Div3);
      newTitle3.appendChild(newImage2Div3);
      newTitle3.appendChild(newTextDiv3_title3);

      container.replaceChild(newTitle3, targetTitleElement3);

      // 創建並更新 title4
      let targetTitleElement4 = document.querySelector(".title.title4");
      let newTitle4 = document.createElement("div");
      newTitle4.className = "js_title js_title4";

      let newImage1Div4 = document.createElement("div");
      newImage1Div4.className = "js_image1";
      let newImage1_4 = document.createElement("img");
      newImage1_4.src = spots[6].imageUrl;
      newImage1_4.alt = "Taiwan";
      newImage1Div4.appendChild(newImage1_4);

      let newImage2Div4 = document.createElement("div");
      newImage2Div4.className = "js_image2";
      let newImage2_4 = document.createElement("img");
      newImage2_4.src = "./images/541415.png";
      newImage2_4.alt = "Star";
      newImage2Div4.appendChild(newImage2_4);

      let newTextDiv4_title4 = document.createElement("div");
      newTextDiv4_title4.className = "js_text";
      newTextDiv4_title4.textContent = spots[6].title;
      newTitle4.appendChild(newImage1Div4);
      newTitle4.appendChild(newImage2Div4);
      newTitle4.appendChild(newTextDiv4_title4);

      container.replaceChild(newTitle4, targetTitleElement4);

      // 創建並更新 title5
      let targetTitleElement5 = document.querySelector(".title.title5");
      let newTitle5 = document.createElement("div");
      newTitle5.className = "js_title js_title5";

      let newImage1Div5 = document.createElement("div");
      newImage1Div5.className = "js_image1";
      let newImage1_5 = document.createElement("img");
      newImage1_5.src = spots[4].imageUrl;
      newImage1_5.alt = "Taiwan";
      newImage1Div5.appendChild(newImage1_5);

      let newImage2Div5 = document.createElement("div");
      newImage2Div5.className = "js_image2";
      let newImage2_5 = document.createElement("img");
      newImage2_5.src = "./images/541415.png";
      newImage2_5.alt = "Star";
      newImage2Div5.appendChild(newImage2_5);

      let newTextDiv5 = document.createElement("div");
      newTextDiv5.className = "js_text";
      newTextDiv5.textContent = spots[4].title;
      newTitle5.appendChild(newImage1Div5);
      newTitle5.appendChild(newImage2Div5);
      newTitle5.appendChild(newTextDiv5);

      container.replaceChild(newTitle5, targetTitleElement5);

      // 創建並更新 title6
      let targetTitleElement6 = document.querySelector(".title.title6");
      let newTitle6 = document.createElement("div");
      newTitle6.className = "js_title js_title6";

      let newImage1Div6 = document.createElement("div");
      newImage1Div6.className = "js_image1";
      let newImage1_6 = document.createElement("img");
      newImage1_6.src = spots[5].imageUrl;
      newImage1_6.alt = "Taiwan";
      newImage1Div6.appendChild(newImage1_6);

      let newImage2Div6 = document.createElement("div");
      newImage2Div6.className = "js_image2";
      let newImage2_6 = document.createElement("img");
      newImage2_6.src = "./images/541415.png";
      newImage2_6.alt = "Star";
      newImage2Div6.appendChild(newImage2_6);

      let newTextDiv6 = document.createElement("div");
      newTextDiv6.className = "js_text";
      newTextDiv6.textContent = spots[5].title;
      newTitle6.appendChild(newImage1Div6);
      newTitle6.appendChild(newImage2Div6);
      newTitle6.appendChild(newTextDiv6);

      container.replaceChild(newTitle6, targetTitleElement6);

      // 創建並更新 title7
      let targetTitleElement7 = document.querySelector(".title.title7");
      let newTitle7 = document.createElement("div");
      newTitle7.className = "js_title js_title7";

      let newImage1Div7 = document.createElement("div");
      newImage1Div7.className = "js_image1";
      let newImage1_7 = document.createElement("img");
      newImage1_7.src = spots[6].imageUrl;
      newImage1_7.alt = "Taiwan";
      newImage1Div7.appendChild(newImage1_7);

      let newImage2Div7 = document.createElement("div");
      newImage2Div7.className = "js_image2";
      let newImage2_7 = document.createElement("img");
      newImage2_7.src = "./images/541415.png";
      newImage2_7.alt = "Star";
      newImage2Div7.appendChild(newImage2_7);

      let newTextDiv7 = document.createElement("div");
      newTextDiv7.className = "js_text";
      newTextDiv7.textContent = spots[6].title;
      newTitle7.appendChild(newImage1Div7);
      newTitle7.appendChild(newImage2Div7);
      newTitle7.appendChild(newTextDiv7);

      container.replaceChild(newTitle7, targetTitleElement7);

      // 創建並更新 title8
      let targetTitleElement8 = document.querySelector(".title.title8");
      let newTitle8 = document.createElement("div");
      newTitle8.className = "js_title js_title8";

      let newImage1Div8 = document.createElement("div");
      newImage1Div8.className = "js_image1";
      let newImage1_8 = document.createElement("img");
      newImage1_8.src = spots[7].imageUrl;
      newImage1_8.alt = "Taiwan";
      newImage1Div8.appendChild(newImage1_8);

      let newImage2Div8 = document.createElement("div");
      newImage2Div8.className = "js_image2";
      let newImage2_8 = document.createElement("img");
      newImage2_8.src = "./images/541415.png";
      newImage2_8.alt = "Star";
      newImage2Div8.appendChild(newImage2_8);

      let newTextDiv8 = document.createElement("div");
      newTextDiv8.className = "js_text";
      newTextDiv8.textContent = spots[7].title;
      newTitle8.appendChild(newImage1Div8);
      newTitle8.appendChild(newImage2Div8);
      newTitle8.appendChild(newTextDiv8);

      container.replaceChild(newTitle8, targetTitleElement8);

      // 創建並更新 title9
      let targetTitleElement9 = document.querySelector(".title.title9");
      let newTitle9 = document.createElement("div");
      newTitle9.className = "js_title js_title9";

      let newImage1Div9 = document.createElement("div");
      newImage1Div9.className = "js_image1";
      let newImage1_9 = document.createElement("img");
      newImage1_9.src = spots[8].imageUrl;
      newImage1_9.alt = "Taiwan";
      newImage1Div9.appendChild(newImage1_9);

      let newImage2Div9 = document.createElement("div");
      newImage2Div9.className = "js_image2";
      let newImage2_9 = document.createElement("img");
      newImage2_9.src = "./images/541415.png";
      newImage2_9.alt = "Star";
      newImage2Div9.appendChild(newImage2_9);

      let newTextDiv9 = document.createElement("div");
      newTextDiv9.className = "js_text";
      newTextDiv9.textContent = spots[8].title;
      newTitle9.appendChild(newImage1Div9);
      newTitle9.appendChild(newImage2Div9);
      newTitle9.appendChild(newTextDiv9);

      container.replaceChild(newTitle9, targetTitleElement9);

      // 創建並更新 title10
      let targetTitleElement10 = document.querySelector(".title.title10");
      let newTitle10 = document.createElement("div");
      newTitle10.className = "js_title js_title10";

      let newImage1Div10 = document.createElement("div");
      newImage1Div10.className = "js_image1";
      let newImage1_10 = document.createElement("img");
      newImage1_10.src = spots[9].imageUrl;
      newImage1_10.alt = "Taiwan";
      newImage1Div10.appendChild(newImage1_10);

      let newImage2Div10 = document.createElement("div");
      newImage2Div10.className = "js_image2";
      let newImage2_10 = document.createElement("img");
      newImage2_10.src = "./images/541415.png";
      newImage2_10.alt = "Star";
      newImage2Div10.appendChild(newImage2_10);

      let newTextDiv10 = document.createElement("div");
      newTextDiv10.className = "js_text";
      newTextDiv10.textContent = spots[9].title;
      newTitle10.appendChild(newImage1Div10);
      newTitle10.appendChild(newImage2Div10);
      newTitle10.appendChild(newTextDiv10);

      container.replaceChild(newTitle10, targetTitleElement10);
    });
});
