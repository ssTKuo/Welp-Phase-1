// document 是 JavaScript 中的一个全局对象，它代表整个 HTML 文档
// "DOMContentLoaded"是一种特殊的事件，当 HTML 的全部内容完全被加载和解析完成后，就会触发这个事件，但不需要等待样式表、图像和子框架的完成加载。
// addEventListener 是 HTML 元素的一个方法，用于在该元素上绑定一个事件监听器。它接收两个参数：事件名称("submit")和当事件发生时要调用的函数。
// (event) => {...} 是一个箭头函数，它在 "DOMContentLoaded" 事件被触发时执行。
// getElementById 是 document 对象的一个方法，用于获取具有指定 ID 的元素。在这个例子中，它用来获取 ID 为 "signinForm" 的表单元素。
// "submit" 是要监听的事件类型，表示当表单尝试提交时触发。
//  function (event) {...} 是一个匿名函数，它定义了当 submit 事件发生时应执行的操作。这个函数接收一个参数 event，它是一个包含事件相关信息的对象。
//  document.getElementById("agree") 同样是一个获取 ID 为 "agree" 的 HTML 元素的方法调用，此处用来获取复选框元素。
//  checkbox.checked 是一个属性，它表示复选框是否被勾选。如果复选框被勾选，checked 属性返回 true；否则返回 false。
//  preventDefault 是事件对象 event 的一个方法。它用来取消事件的默认动作。对于提交事件，其默认动作是提交表单。调用 event.preventDefault() 方法会阻止表单提交，这在复选框未被勾选时非常有用。

document.addEventListener("DOMContentLoaded", (event) => {
  let form = document.getElementById("signinForm");
  if (form) {
    form.addEventListener("submit", function (event) {
      let checkbox = document.getElementById("agree");
      // 清除之前的自定义验证消息
      checkbox.setCustomValidity("");
      if (!checkbox.checked) {
        // 如果复选框未勾选，设置自定义验证消息
        checkbox.setCustomValidity("Please check the checkbox first");
        // 显示自定义验证消息
        checkbox.reportValidity();
        // 阻止表单提交
        event.preventDefault();
      }
      // 如果复选框被勾选，表单将正常提交
    });
  } else {
    console.error("signinForm not found");
  }
});

// fetch語法(Promise寫法)，這邊處理查詢會員的功能
function fetchMemberData() {
  const username = document.getElementById("username").value;
  fetch(`/api/member?username=${username}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      const resultDiv = document.getElementById("result");
      if (data.data) {
        resultDiv.textContent = `${data.data.name} (${data.data.username})`;
      } else {
        resultDiv.textContent = "No Data";
      }
    })
    .catch((error) => {
      console.error(
        "There has been a problem with your fetch operation:",
        error
      );
    });
}
// fetch語法(Promise寫法)，這邊處理會員姓名修改的功能
function updateMemberName() {
  const newName = document.getElementById("newName").value;
  fetch(`/api/member`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name: newName }),
  })
    .then((response) => response.json())
    .then((data) => {
      const updateResultDiv = document.getElementById("updateResult");
      if (data.ok) {
        updateResultDiv.textContent = "更新成功";
      } else {
        updateResultDiv.textContent = "更新失敗";
      }
    })
    .catch((error) => {
      console.error(
        "There has been a problem with your fetch operation:",
        error
      );
    });
}
