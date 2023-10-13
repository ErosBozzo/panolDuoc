function mostrarContraseña(){
    var tipo = document.getElementById("contraseña");
    if(tipo.type == "password"){
    tipo.type = "text";
    }else{
    tipo.type = "password";
    }
}

function mostrarRecontraseña(){
    var tipo = document.getElementById("recontraseña");
    if(tipo.type == "password"){
    tipo.type = "text";
    }else{
    tipo.type = "password";
    }
}
