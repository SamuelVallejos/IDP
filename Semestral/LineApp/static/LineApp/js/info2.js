$(document).ready(function () {
    $.get("https://valorant-api.com/v1/agents?language=es-ES", function (data) {
        $.each(data.data, function (i, item) {
            $("#agente").append('<option value=' + item.displayName + '>' + item.displayName + '</option>');
        });
    });
    $.get("https://valorant-api.com/v1/maps?language=es-ES", function (data) {
        $.each(data.data, function (i, item) {
            if (item.displayName != "Campo de tiro"){
                $("#mapa").append('<option value=' + item.displayName + '>' + item.displayName + '</option>');
            }
        });
    });
});



