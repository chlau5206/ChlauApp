// main / layout.js

const DEBUG = false;

function log(msg) {
    if (DEBUG) console.log(msg);
}

log("layout.js loaded")
document.addEventListener('DOMContentLoaded', () => {
    const burger = document.getElementById('mainBurger');
    const menu = document.getElementById(burger.dataset.target);
    const dropdowns = document.querySelectorAll('.has-dropdown');

    // Toggle navbar menu
    burger.addEventListener('click', () => {
        log("layout.js navbar menu: burger clicked")
        burger.classList.toggle('is-active');
        menu.classList.toggle('is-active');
    });

    // Reset menu state on resize
    window.addEventListener('resize', () => {
        if (window.innerWidth > 768) {
            burger.classList.remove('is-active');
            menu.classList.remove('is-active');
        }
    });

    // Toggle dropdown menus on click
    dropdowns.forEach((dropdown) => {
        const link = dropdown.querySelector('.navbar-link');
        if (link) {
            link.addEventListener('click', () => {
                log("layout.js navbar-dropdown: burger clicked")
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

// Detect system theme
const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

// Apply theme based on system preference
if (prefersDark) {
    document.documentElement.className = "dark-mode";   // High-Contrast Dark
    //document.documentElement.className = "soft-dark"; // soft dark
    //document.documentElement.className = "oled";      // OLED
} else {
    document.documentElement.className = "";            // Light
}


//window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", e => {
//    document.documentElement.className = e.matches ? "dark-mode" : "";
//});

// To test
// window.matchMedia("(prefers-color-scheme: dark)").matches