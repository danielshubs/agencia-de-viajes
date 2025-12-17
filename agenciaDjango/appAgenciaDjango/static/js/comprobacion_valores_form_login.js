const emailForm = document.getElementById("email");
const passwordForm = document.getElementById("password");

// nuevos divs
let emailError = document.createElement("div");
emailError.className = "errorDiv";

let passwordError = document.createElement("div");
passwordError.className = "errorDiv";

emailForm.insertAdjacentElement("afterend", emailError);
passwordForm.insertAdjacentElement("afterend", passwordError);


const form = document.querySelector("form");
form.addEventListener("submit", function(event) {

    const email = emailForm.value;
    const password = passwordForm.value;

    // método de validación del email, tiene que ser "algo@algo.algo" : solo 1 @ obligatorio, después del @ solo 1 punto obligatorio, sin separaciones
    const emailFormato = /^[^\s@]+@[^\s@.]+\.[^\s@.]+$/;
    if(!emailFormato.test(email)) { // si el email es incorrecto respecto a dicho formato
        event.preventDefault();
        emailError.textContent = `El email insertado no es válido (${email})`;
        emailError.style.display = "block";
    } else {
        emailError.style.display = "none";
    }

    if(password.length < 8) { // si la contraseña tiene menos de 8 carácteres
        event.preventDefault();
        passwordError.textContent = `La contraseña indicada no es válida, tiene menos de 8 carácteres`;
        passwordError.style.display = "block";
    } else {
        passwordError.style.display = "none";
    }
});