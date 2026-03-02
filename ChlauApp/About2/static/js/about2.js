/* About2/about2.js */

/*This jS is to control content collapse and expand. */
document.addEventListener("DOMContentLoaded", () => {
    const collapsibles = document.querySelectorAll(".collapsible");

    collapsibles.forEach((section) => {
        const header = section.querySelector(".collapsible-header");
        const content = section.querySelector(".collapsible-content");

        header.addEventListener("click", () => {
            section.classList.toggle("is-active");

            if (section.classList.contains("is-active")) {
                content.style.display = "block";
            } else {
                content.style.display = "none";
            }
        });
    });
});