function openSidebar() {
            document.getElementById("mySidebar").classList.add("open");
        }
        function closeSidebar() {
            document.getElementById("mySidebar").classList.remove("open");
        }

const images = [
            "static/images/pollen-bg1.jpg","static/images/pollen-bg2.jpg","static/images/pollengrain.jpg"
        ];
let current = 0;
function showSlide(idx) {
    current = idx;
    document.getElementById('carousel-img').src = images[current];
    document.querySelectorAll('.carousel-dot').forEach((dot, i) => {
        dot.classList.toggle('active', i === current);
    });
}
function prevSlide() {
    current = (current - 1 + images.length) % images.length;
    showSlide(current);
}
function nextSlide() {
    current = (current + 1) % images.length;
    showSlide(current);
}
// Optional: auto-slide
setInterval(() => { nextSlide(); }, 5000);        
