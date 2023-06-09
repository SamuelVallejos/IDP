$(document).ready(function (e) {
    const formulario = document.getElementById("car");
    const inputs = document.querySelectorAll('#car input');

    const carrito = document.getElementById('carrito');
    const total = document.getElementById('total');

    // Función para añadir un producto al carrito
    function agregarProducto(producto) {
        const li = document.createElement('li');
        li.innerText = producto;
        carrito.appendChild(li);

        // Actualizar el total
        const precio = parseFloat(producto.dataset.precio);
        total.innerText = `$${parseFloat(total.innerText.substr(1)) + precio}.00`;
    }

    // Función para vaciar el carrito
    function vaciarCarrito() {
        carrito.innerHTML = '';
        total.innerText = '$0.00';
    }
});