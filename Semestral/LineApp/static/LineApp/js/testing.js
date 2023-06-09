var carrito = [];

function agregarAlCarrito(nombre, precio) {
    var producto = {
        nombre: nombre,
        precio: precio
    };

    carrito.push(producto);
    actualizarCarrito();
}

function actualizarCarrito() {
    var cartItems = document.getElementById('cart-items');
    var total = 0;

    cartItems.innerHTML = '';

    carrito.forEach(function (producto) {
        var item = document.createElement('div');
        item.classList.add('item');

        var nombre = document.createElement('span');
        nombre.classList.add('name');
        nombre.textContent = producto.nombre;

        var precio = document.createElement('span');
        precio.classList.add('price');
        precio.textContent = '$' + producto.precio;

        item.appendChild(nombre);
        item.appendChild(precio);

        cartItems.appendChild(item);

        total += producto.precio;
    });

    var totalElement = document.getElementById('total');
    totalElement.textContent = 'Total: $' + total;
}

function realizarPago() {
    // Obtiene la URL base de la API de Flow
    var baseUrl = 'https://sandbox.flow.cl/api';

    // Agrega el servicio a consumir a la URL
    var url = baseUrl + '/payment/create';

    // Crea un arreglo con los productos del carrito
    var items = carrito.map(function (producto) {
        return {
            name: producto.nombre,
            price: producto.precio,
            quantity: 1
        };
    });

    // Agrega la firma y los productos al objeto params
    var params = {
        s: '5269228904d151863511068deee92b722f6a82cc', // Reemplaza 'signature' con tu firma de Flow
        items: items
    };

    // Realiza la solicitud POST a la API de Flow   

    console.log('Parámetros de la solicitud:', params);
    console.log(url)

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