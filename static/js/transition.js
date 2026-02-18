document.addEventListener("DOMContentLoaded", () => {
    document.body.style.opacity = "1";
});

document.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", function(e) {

        if (this.hostname === window.location.hostname) {
            e.preventDefault();
            document.body.classList.remove("loaded");

            setTimeout(() => {
                window.location = this.href;
            }, 400);
        }
    });
});
