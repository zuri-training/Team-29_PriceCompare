//Show or Hide Nav Menu
const menu = document.querySelector(".nav2");
const openBtn = document.querySelector(".menu-open");
const closeBtn = document.querySelector(".menu-closed");

//To open
openBtn.addEventListener("click", () => {
  menu.style.display = "flex";
  closeBtn.style.display = "inline-block";
  openBtn.style.display = "none";
});

//To close

closeBtn.addEventListener("click", () => {
  menu.style.display = "none";
  openBtn.style.display = "inline-block";
  closeBtn.style.display = "none";
});
