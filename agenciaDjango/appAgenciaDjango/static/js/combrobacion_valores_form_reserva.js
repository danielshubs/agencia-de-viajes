// Campos
const nombreForm = document.getElementById("nombre");
const apellidoForm = document.getElementById("apellido");
const emailForm = document.getElementById("email");
const telefonoForm = document.getElementById("telefono");
const tarjetaForm = document.getElementById("cc_numero");
const expiracionForm = document.getElementById("cc_expiracion");
const cvvForm = document.getElementById("cc_cvv");


let nombreError = document.createElement("div");
nombreError.className = "errorDiv";

let apellidoError = document.createElement("div");
apellidoError.className = "errorDiv";

let emailError = document.createElement("div");
emailError.className = "errorDiv";

let telefonoError = document.createElement("div");
telefonoError.className = "errorDiv";

let tarjetaError = document.createElement("div");
tarjetaError.className = "errorDiv";

let expiracionError = document.createElement("div");
expiracionError.className = "errorDiv";

let cvvError = document.createElement("div");
cvvError.className = "errorDiv";

// Insertar errores
nombreForm.insertAdjacentElement("afterend", nombreError);
apellidoForm.insertAdjacentElement("afterend", apellidoError);
emailForm.insertAdjacentElement("afterend", emailError);
telefonoForm.insertAdjacentElement("afterend", telefonoError);
tarjetaForm.insertAdjacentElement("afterend", tarjetaError);
expiracionForm.insertAdjacentElement("afterend", expiracionError);
cvvForm.insertAdjacentElement("afterend", cvvError);

const form = document.querySelector("form");

form.addEventListener("submit", function (event) {

    // NOMBRE
    if (nombreForm.value.trim() === "") {
         event.preventDefault();
        nombreError.textContent = "El nombre es obligatorio";
        nombreError.classList.add("visible");

    } else {
        nombreError.classList.remove("visible");
    }

    // APELLIDO
    if (apellidoForm.value.trim() === "") {
         event.preventDefault();
        apellidoError.textContent = "El apellido es obligatorio";
        apellidoError.classList.add("visible");

    } else {
       apellidoError.classList.remove("visible");
    }

    // EMAIL
    const emailFormato = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailFormato.test(emailForm.value)) {
         event.preventDefault();
        emailError.textContent = "El email no es válido";
        emailError.classList.add("visible");

    } else {
        emailError.classList.remove("visible");
    }

    // TELÉFONO (mínimo 9 números)
    if (telefonoForm.value.length < 9 ) {
         event.preventDefault();
        telefonoError.textContent = "El teléfono debe tener al menos 9 números";
        telefonoError.classList.add("visible");

    } else {
       telefonoError.classList.remove("visible");
    }

    // TARJETA (16 dígitos)
    if (tarjetaForm.value.replace(/\s/g, "").length !== 16) {
         event.preventDefault();
        tarjetaError.textContent = "La tarjeta debe tener 16 dígitos";
        tarjetaError.classList.add("visible");

    } else {
        tarjetaError.classList.remove("visible");
    }

    // EXPIRACIÓN MM/AA
    const expFormato = /^(0[1-9]|1[0-2])\/\d{2}$/;
    if (!expFormato.test(expiracionForm.value)) {
         event.preventDefault();
        expiracionError.textContent = "Formato inválido (MM/AA)";
        expiracionError.classList.add("visible");

    } else {
       expiracionError.classList.remove("visible");
    }

    // CVV
    if (cvvForm.value.length !== 3) {
         event.preventDefault();
        cvvError.textContent = "El CVV debe tener 3 dígitos";
        cvvError.classList.add("visible");

    } else {
        cvvError.classList.remove("visible");
    }

});
