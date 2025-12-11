const no_viajes = document.getElementById("no_viajes");
const precio_form = document.getElementById("precio_maximo");
const cards_viajes = document.querySelectorAll(".viaje-card");

const form = document.getElementById("range-form");
form.addEventListener("submit", function(event) {
    event.preventDefault();
    
    const precio_max = parseFloat(precio_form.value);
    let any = false;

    cards_viajes.forEach(card => {
        const precio_viaje = parseFloat(card.dataset.precio);

        if (precio_viaje <= precio_max) {
            card.style.display = "block";
            any = true;
        } else {
            card.style.display = "none";
        }

        if (any) {
            no_viajes.style.display = "none";
        } else {
            no_viajes.style.display = "block";
        }
    });
});