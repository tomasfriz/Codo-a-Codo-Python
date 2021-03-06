// Esta función valida todos los campos del form.
// Si alguno no cumple con los requisitos, se aborta
// con return. Caso contrario, al final se realiza 
// efectivamente el envio de los datos.

function valida_envia() {
    //valido el nombre
    if (document.formulario.firstname.value.length == 0) {
        alert("Tiene que escribir su nombre")
        document.formulario.firstname.focus()
        return 0;
    } else {
        firstname = document.formulario.firstname.value;
        firstname = validarLetras(firstname);
        document.formulario.firstname.value = firstname;
        if (firstname == "") {
            alert("Tiene que introducir letras en su nombre.")
            document.formulario.firstname.focus()
            return 0;
        }
    }

    //valido el apellido
    if (document.formulario.lastname.value.length == 0) {
        alert("Tiene que escribir su apellido")
        document.formulario.lastname.focus()
        return 0;
    } else {
        lastname = document.formulario.lastname.value;
        lastname = validarLetras(lastname);
        document.formulario.lastname.value = lastname;
        if (lastname == "") {
            alert("Tiene que introducir letras en su apellido.")
            document.formulario.firstname.focus()
            return 0;
        }
    }

    //valido el email
    if (document.formulario.email.value.length == 0) {
        alert("Tiene que escribir su email")
        document.formulario.email.focus()
        return 0;
    }

    //valido el telefono.
    phone = document.formulario.phone.value;
    phone = validarEntero(phone);
    document.formulario.phone.value = phone;
    if (phone == "") {
        alert("Tiene que introducir números enteros en su telefono.")
        document.formulario.phone.focus()
        return 0;
    }
}

function validarEntero(valor) {
    //intento convertir a entero.
    //si era un entero no le afecta, si no lo era lo intenta convertir.
    valor = parseInt(valor);
    //Compruebo si es un valor numérico.
    if (isNaN(valor)) {
        //entonces (no es numero) devuelvo el valor cadena vacia.
        return "";
    } else {
        //En caso contrario (Si era un número) devuelvo el valor.
        return valor;
    }
}

function validarLetras(valor) {
    //Compruebo si es una cadena de caracteres.
    if (valor.length == "0" || valor.length == "1" || valor.length == "2" || valor.length == "3" || valor.length == "4" || valor.length == "5" || valor.length == "6" || valor.length == "7" || valor.length == "8" || valor.length == "9") {
        //entonces (es numero) devuelvo el valor cadena vacia.
        return "";
    } else {
        //En caso contrario (Si era una cadena) devuelvo el valor.
        return valor;
    }
}

