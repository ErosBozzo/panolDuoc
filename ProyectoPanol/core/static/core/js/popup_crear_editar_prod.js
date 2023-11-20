$(document).ready(function () {
    const btnEditar = $('.btn-editar');
    const popupFormContainer = $('#popup-form-container');

    btnEditar.on('click', function (event) {
        event.preventDefault();

        const productoId = $(this).data('producto-id');

        // Realiza una solicitud AJAX para obtener los datos del producto
        $.ajax({
            url: "{% url 'producto' 'get' 0 %}".replace('0', productoId),
            type: 'GET',
            success: function (data) {
                // Llena el formulario emergente con los datos recibidos
                popupFormContainer.html(data);

                // Muestra el formulario emergente
                popupFormContainer.show();
            },
            error: function () {
                Swal.fire({
                    icon: 'error',
                    title: 'Error al obtener datos del producto',
                    showConfirmButton: false,
                    timer: 1500
                });
            }
        });
    });

    // Puedes agregar un evento para cerrar el formulario emergente si es necesario
    // ...
});
