$(document).ready(function () {

    $("#btnEnviar").click(function () {
        var contra = "";
        contra = $("#contraseña").val();

        var recontra = "";
        recontra = $("#recontraseña").val();

        if (contra.length < 5) {
            document.getElementById("mensajeContra").classList.remove('desactive')
            document.getElementById("mensajeContra").classList.add('activate')
            return false; //impide que el formulario se envie de forma erronea
        } else {
            document.getElementById("mensajeContra").classList.add('desactive')

        }

        if (contra !== recontra) {
            document.getElementById("mensajeRecontra").classList.remove('desactive') //Removemos una clase 
            document.getElementById("mensajeRecontra").classList.add('activate') //Agregamos una clase 

        } else {
            document.getElementById("mensajeRecontra").classList.add('desactive')
        }
    })
});


