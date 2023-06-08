$(document).ready(function () {
    $.get("https://valorant-api.com/v1/maps?language=es-ES", function(data){
            $.each(data.data ,function(i, item){
                $("."+item.displayName).css("background-image", "url("+item.listViewIcon+")");
            });
        });
});