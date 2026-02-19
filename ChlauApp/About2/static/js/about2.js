/* About2/about2.js */
<script>
document.addEventListener("DOMContentLoaded", () => {
    const sections = document.querySelectorAll(".collapsible-section");

    sections.forEach(section => {
        const title = section.querySelector(".collapsible-title");
        const full = section.querySelector(".collapsible-full");
        const chevron = section.querySelector(".chevron");

        title.addEventListener("click", () => {
            full.classList.toggle("is-hidden");
            chevron.classList.toggle("rotated");
        });
    });
});
</script>

