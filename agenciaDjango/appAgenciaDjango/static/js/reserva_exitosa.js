
const button = document.querySelector(".btn");
const icon = document.querySelector(".success-icon");

// Evento hover en  el botón
button.addEventListener("mouseover", function () {
    button.style.backgroundColor = "#2ecc71";
});

// Evento mouseout en el botón
button.addEventListener("mouseout", function () {
    button.style.backgroundColor = "";
});

