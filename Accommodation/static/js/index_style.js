const bodyEl = document.querySelector("body");
const toggleEl = document.querySelector(".fa-moon");

toggleEl.addEventListener("click", () => {
  bodyEl.classList.toggle("dark");

  if (bodyEl.classList.contains("dark")) {
    toggleEl.classList.replace("fa-moon", "fa-sun");
  } else {
    toggleEl.classList.replace("fa-sun", "fa-moon");
  }
});