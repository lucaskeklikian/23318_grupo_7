
var form_paciente = document.getElementById("form_paciente")

form_paciente.addEventListener("submit",validar);

function validar(){
    
    if (validarNombre()){
        form_paciente.nombre.focus()
        return 0
    }

    if (validarApellido()){
        form_paciente.apellido.focus()
        return 0
    }

    if (validarEmail()){
        form_paciente.email.focus()
        return 0
    }

    
 }

 
function validarNombre() {
     const pattern = new RegExp('^[A-Z]+$', 'i');
     if(!pattern.test(form_paciente.nombre.value)){
        alert("Nombre invalido")
     }
    return form_paciente.nombre.value.length  == 0
}

function validarApellido() {
    const pattern = new RegExp('^[A-Z]+$', 'i');
    if(!pattern.test(form_paciente.apellido.value)){
        alert("Apellido invalido")
     }
    return form_paciente.apellido.value.length  == 0
}


function validarEmail() { 
    console.log("HOLAAAAAAAAAAAAAAAA")
    const pattern = new RegExp('[a-z0-9]+@[a-z]+\.[a-z]{2,3}', 'i');
    if(!pattern.test(form_paciente.email.value)){
        alert("Email invalido")
     }
    return form_paciente.email.value.length  == 0
}
