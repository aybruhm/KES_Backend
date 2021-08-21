// Summit 
const togBtn = document.getElementById("toggle-button");
const navTabs = document.getElementById("nav-tabs");

togBtn.addEventListener("click", toggleNavTabs);

function toggleNavTabs(e) {
    e.preventDefault();

    navTabs.classList.toggle("d-none");
}