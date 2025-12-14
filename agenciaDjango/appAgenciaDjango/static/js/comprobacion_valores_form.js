const emailForm = document.getElementById("email");
const passwordForm = document.getElementById("password");
const confirmationForm = document.getElementById("password2");
const nombreForm = document.getElementById("nombre");

// nuevos divs
let emailError = document.createElement("div");
emailError.className = "error";

let passwordError = document.createElement("div");
passwordError.className = "error";

let confirmationError = document.createElement("div");
confirmationError.className = "error";

let nombreError = document.createElement("div");
nombreError.className = "error";



emailForm.insertAdjacentElement("afterend", emailError);
passwordForm.insertAdjacentElement("afterend", passwordError);
confirmationForm.insertAdjacentElement("afterend", confirmationError);
nombreForm.insertAdjacentElement("afterend", nombreError);


const form = document.querySelector("form");
form.addEventListener("submit", function(event) {

    const email = emailForm.value;
    const password = passwordForm.value;
    const confirmation = confirmationForm.value;
    const nombre = nombreForm.value;

    // método de validación del email, tiene que ser "algo@algo.algo" : solo 1 @ obligatorio, después del @ solo 1 punto obligatorio, sin separaciones
    const emailFormato = /^[^\s@]+@[^\s@.]+\.[^\s@.]+$/;
    if(!emailFormato.test(email)) { // si el email es incorrecto respecto a dicho formato
        event.preventDefault();
        emailError.textContent = `El email insertado no es válido (${email})`;
        emailError.classList.add("visible");
    } else {
        emailError.style.display = "none";
    }

    if(password.length < 8) { // si la contraseña tiene menos de 8 carácteres
        event.preventDefault();
        passwordError.textContent = `La contraseña indicada no es válida, tiene menos de 8 carácteres`;
        passwordError.classList.add("visible");
    } else {
        passwordError.style.display = "none";
    }

    if(confirmation != password) {
        event.preventDefault();
        confirmationError.textContent = `La confirmación no coincide con la contraseña primeramente indicada`;
        confirmationError.classList.add("visible")
    } else {
        confirmationError.style.display = "none";
    }

    // Exactamente 1 nombre y 1 apellido como nombre y apellido
    const nombreFormato = /^[^\s]+\s[^\s]+$/;
    if(!nombreFormato.test(nombre)) {
        event.preventDefault();
        nombreError.textContent = `Inserte exactamente 1 nombre y 1 apellido. El nombre insertado no es válido (${nombre})`;
        nombreError.classList.add("visible");
    } else {
        nombreError.style.display = "none";
    }
});