/* About2/about2.js */

window.debug("[about2.js] loaded.");

/*This jS is to control content collapse and expand. */
document.addEventListener("DOMContentLoaded", () => {
    window.debug("[about2.js] DOM ready, collapsibles initialized");

    const collapsibles = document.querySelectorAll(".collapsible");

    collapsibles.forEach((section) => {
        const header = section.querySelector(".collapsible-header");
        const content = section.querySelector(".collapsible-content");

        header.addEventListener("click", () => {
            window.debug("[about2.js] clicked");
            section.classList.toggle("is-active");

            if (section.classList.contains("is-active")) {
                content.style.display = "block";
            } else {
                content.style.display = "none";
            }
        });
    });
});
