const inputs = document.querySelectorAll(".input");

function focusFunc() {
  let parent = this.parentNode;
  parent.classList.add("focus");
}

function blurFunc() {
  let parent = this.parentNode;
  if (this.value == "") {
    parent.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", focusFunc);
  input.addEventListener("blur", blurFunc);
});

function hidePlaceholder(inputId) { const input = document.getElementById(inputId); input.placeholder = ""; }

function showPlaceholder(inputId) { const input = document.getElementById(inputId); const placeholders = { fullname: "Fullname*", email: "Email*", phone: "Phone Number*", message: "Message*" }; if (input.value === "") { input.placeholder = placeholders[inputId]; } }
