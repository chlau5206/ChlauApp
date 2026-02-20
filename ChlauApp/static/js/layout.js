// layout.js

document.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('.navbar-burger');
    const menu = document.querySelector('.navbar-menu');
    const dropdowns = document.querySelectorAll('.has-dropdown');

    // Toggle navbar menu
    if (burger && menu) {
        burger.addEventListener('click', () => {
            burger.classList.toggle('is-active');
            menu.classList.toggle('is-active');
        });
    }

    // Toggle dropdown menus on click
    dropdowns.forEach((dropdown) => {
        const link = dropdown.querySelector('.navbar-link');
        if (link) {
            link.addEventListener('click', () => {
                dropdown.classList.toggle('is-active');
            });
        }
    });
});
window.addEventListener("scroll", () => {
    const navbar = document.querySelector(".navbar");
    if (window.scrollY > 10) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }
});
