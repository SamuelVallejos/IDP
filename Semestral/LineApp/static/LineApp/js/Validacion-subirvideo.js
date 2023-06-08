$(document).ready(function () {
    const formulario = document.getElementById("formsubirvideo");
    const inputs = document.querySelectorAll('#formsubirvideo input');
    const seles = document.querySelectorAll('#formsubirvideo select');

    const expresiones = {
        titulo: /^[a-zA-Z0-9^\s\_\-]{3,30}$/,
        descripcion: /^[a-zA-Z0-9^\s]{1,200}$/,
        incorporacion: /^https:\/\/www.youtube.com\/embed\/[a-zA-Z0-9\_\-]+$/ //  tiene que empezar con la direccion https://www.youtube.com/embed/....................... del video
    }

    const campos = {
        titul: false,
        agente: false,
        mapa: false,
        bando: false,
        descripcion: false,
        incorporacion: false
    }

    const validacion = (e) => {
        switch (e.target.name) {
            case "titulo":
                validarCampo(expresiones.titulo, e.target, "titul");
                break;
            case "descripcion":
                validarCampo(expresiones.descripcion, e.target, "descripcion");
                break;
            case "incorporacion":
                validarCampo(expresiones.incorporacion, e.target, "incorporacion");
                break;
        }
    }

    const validarCampo = (expre, input, campo) => {
        if (expre.test(input.value)) {
            $("#" + campo).removeClass("is-invalid");
            $("#" + campo).addClass("is-valid");
            $("#msj-" + campo).removeClass("d-block");
            $("#msj-" + campo).addClass("d-none");
            campos[campo] = true;
        } else {
            $("#" + campo).removeClass("is-valid");
            $("#" + campo).addClass("is-invalid");
            $("#msj-" + campo).removeClass("d-none");
            $("#msj-" + campo).addClass("d-block");
            campos[campo] = false;

        }
    }

    const vselect = (e) => {
        switch (e.target.name) {
            case "agente":
                validarSelect("agente");
                break;
            case "mapa":
                validarSelect("mapa");
                break;
            case "bando":
                validarSelect("bando");
                break;
        }
    }

    const validarSelect = (campo) => {
        var sele = $("#" + campo).val();
        if (sele != -1) {
            $("#msj-" + campo).removeClass("d-block");
            $("#msj-" + campo).addClass("d-none");
            campos[campo] = true;
        } else {
            $("#msj-" + campo).removeClass("d-none");
            $("#msj-" + campo).addClass("d-block");
            campos[campo] = false;
        }
    }

    seles.forEach((select) => {
        select.addEventListener('blur', vselect);
    });


    inputs.forEach((input) => {
        input.addEventListener('keyup', validacion);
        input.addEventListener('blur', validacion);
    });
    $("#formsubirvideo").submit(function () {
        event.preventDefault();
        if(campos.titul && campos.agente && campos.mapa && campos.bando && campos.descripcion && campos.incorporacion){
            formulario.submit();
        }else{
            $("#mensaj-error").removeClass("d-none");
            $("#mensaj-error").addClass("d-block");
            $("#mensaj-envio").addClass("d-none");
            $("#mensaj-envio").removeClass("d-block");
        }
    })
});