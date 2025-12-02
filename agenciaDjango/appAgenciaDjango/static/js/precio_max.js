document.getElementById("range-form").addEventListener("submit", function(event) {
    event.preventDefault();
    let precio_maximo = document.getElementById("precio_maximo").value;
    console.log(precio_maximo);
    destino = window.location.pathname.split("/")[2]; // destino para re-construir el pathname
    window.location.href = `/viajes/${destino}/${precio_maximo}`; // funciona tanto desde /destino como desde /destino/precio
});