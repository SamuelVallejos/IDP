//GET
// Obtiene la URL base de la API de Flow
function verificarEstadoPago() {
    var baseUrl = 'https://sandbox.flow.cl/api/';

    // Agrega el servicio a consumir a la URL
    var url = baseUrl + '/payment/getStatus';

    // Agrega la firma a los parámetros
    var params = {};
    params.s = '26FC7924-EE7C-46C5-8852-84F7B988L590'; // Reemplazar 'signature' con tu firma de Flow

    // Codifica los parámetros en formato URL y los agrega a la URL
    url += '?' + new URLSearchParams(params);

    // Realiza la solicitud GET a la API de Flow
    fetch(url)
        .then(function (response) {
            if (!response.ok) {
                throw new Error('Unexpected error occurred. HTTP_CODE: ' + response.status);
            }
            return response.json();
        })
        .then(function (data) {
            // Procesa la respuesta de la API de Flow
            console.log(data);
            // Aquí puedes mostrar o utilizar la información del estado de pago
        })
        .catch(function (error) {
            // Maneja los errores de la solicitud
            console.error('Error: ' + error.message);
        });
}

// -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
// POST
// Obtiene la URL base de la API de Flow
function crearOrdenPago() {
    // Obtiene la URL base de la API de Flow
    var baseUrl = 'https://sandbox.flow.cl/api';

    // Agrega el servicio a consumir a la URL
    var url = baseUrl + '/payment/create';

    // Agrega la firma a los parámetros
    var params = {
        s: '5269228904d151863511068deee92b722f6a82cc',// Reemplazar 'signature' con tu firma de Flow
        currency: "CLP",
        monto: '100'
    };

    console.log('Parámetros de la solicitud:', params);
    console.log(url)

    // Realiza la solicitud POST a la API de Flow
    fetch(url, {
        method: 'POST',
        mode: 'no-cors',
        body: JSON.stringify(params),
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(function (response) {
            if (!response.ok) {
                throw new Error('Unexpected error occurred. HTTP_CODE: ' + response.status);
            }
            return response.text();
        })
        .then(function (data) {
            // Procesa la respuesta de la API de Flow
            console.log(data);
            // Aquí puedes mostrar o utilizar la respuesta de la creación de la orden de pago
        })
        .catch(function (error) {
            // Maneja los errores de la solicitud
            console.error('Error: ' + error.message);
        });
}
function calcularTotal() {
    // Calcula el monto total sumando los precios de los productos seleccionados
    var productos = document.querySelectorAll('ul li');
    var total = 0; // Inicializar total en 0

    productos.forEach(function (producto) {
        var precio = parseFloat(producto.textContent.match(/\d+/)[0]);
        total += precio;
    });

    return total;
}