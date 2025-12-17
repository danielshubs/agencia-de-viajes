const no_destinos = document.getElementById("no_destinos");
const cards_reserva = document.querySelectorAll(".reserva-card");
const barra = document.getElementById("barra-busqueda");

barra.addEventListener("input", function () {
    const busqueda = barra.value.toLowerCase();
    let any = false;

    cards_reserva.forEach(card => {
        const nombre = card.dataset.nombre.toLowerCase();

        if (nombre.startsWith(busqueda)) {
            card.style.display = "grid";
            any = true;
        } else {
            card.style.display = "none";
        }
    });
    if (any) {
        no_destinos.style.display = "none";
    } else {
        no_destinos.style.display = "block";
    }
});

