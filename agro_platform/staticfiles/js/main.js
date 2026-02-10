// Navbar scroll effect
window.addEventListener("scroll", () => {
    const nav = document.querySelector(".navbar");
    nav.style.boxShadow = window.scrollY > 50
        ? "0 4px 12px rgba(0,0,0,0.2)"
        : "none";
});
