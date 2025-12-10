
seguro = document.querySelector('#seguro');
total = document.querySelector("#total");
const base_price = parseFloat(total.textContent);
console.log(seguro.checked);

seguro.addEventListener('change', function() {
    if (seguro.checked) {
    total.textContent = (base_price+ 50).toFixed(2); // .toFixed(2) para mostrar dos decimales
} else {
    total.textContent = (base_price).toFixed(2);
    }

});




