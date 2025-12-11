const form = document.querySelector("form");
const emailForm = document.getElementById("email");
const passwordForm = document.getElementById("password"); // por ahora no se si validar algo en la password pero por si aca lo paso ya

// div debajo del input de email
let emailError = document.createElement("div");
emailError.className = "error";
// no he conseguido que funcionara desde el css, posible cambio
emailError.style.display = "none"; emailError.style.color = "red"; emailError.style.fontSize = "15px"; emailError.style.marginTop = "10px"; emailError.style.border = "1px solid red"
emailForm.insertAdjacentElement("afterend", emailError);

form.addEventListener("submit", function(event) {

    const email = emailForm.value;
    const password = passwordForm.value;

    // método de validación del email, tiene que ser "algo@algo.algo" : solo 1 @ obligatorio, después del @ solo 1 punto obligatorio, sin separaciones
    const emailFormato = /^[^\s@]+@[^\s@.]+\.[^\s@.]+$/;
    if(!emailFormato.test(email)) { // si falla
        event.preventDefault();
        emailError.textContent = `El Email insertado no es valido (${email})`;
        emailError.style.display = "block";   
    }
});