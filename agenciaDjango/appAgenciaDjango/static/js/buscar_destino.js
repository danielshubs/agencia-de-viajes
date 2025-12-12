const no_destinos = document.getElementById("no_destinos");
const cards_destinos = document.querySelectorAll(".destino-card");

const barra = document.getElementById("barra-busqueda");
barra.addEventListener("input", function(event) {
    const busqueda = barra.value;
    let any = false;

    cards_destinos.forEach(card => {
        nombre = card.dataset.nombre;

        // si la busqueda no se pasa de largo Y si la busqueda coincide con el inicio del nombre (mayúsculas/minúsculas dan igual)
        if(busqueda.length <= nombre.length && nombre.toLowerCase().slice(0, busqueda.length) == busqueda.toLowerCase()) {
            card.style.display = "block";
            any = true;
        } else {
            card.style.display = "none";
        }

        if (any) {
            no_destinos.style.display = "none";
        } else {
            no_destinos.style.display = "block";
        }
    });

});