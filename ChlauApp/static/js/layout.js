// layout.js

document.addEventListener('DOMContentLoaded', () => {
    const burger = document.getElementById('mainBurger');
    const menu = document.getElementById(burger.dataset.target);
    const dropdowns = document.querySelectorAll('.has-dropdown');

    // Toggle navbar menu
    burger.addEventListener('click', () => {
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
