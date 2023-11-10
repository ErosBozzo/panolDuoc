// Cuando el documento esté listo
$(document).ready(function() {

  // Ocultar el elemento que muestra el mensaje de cargando
  $(".ajaxRes").hide(); 

  // Cada 5 segundos (5000ms)
  setInterval(function() {
    // Obtener la URL de los datos del elemento HTML
    var url = $("#notificaciones").data('url');

    $.ajax({
      url: url,
      dataType: 'json',

      // Antes de enviar la petición
      beforeSend: function() {
        // Mostrar elemento de cargando
        $(".ajaxRes").show();
        // Escribir mensaje
        $(".ajaxRes").text('Loading...');
      },

      // Si la petición es exitosa
      success: function(res) {
        // Parsear JSON a objeto
        let _json = $.parseJSON(res.data);
    
        // Inicializar variable para HTML
        let _html = '';
    
        // Recorrer objetos de notificaciones
        $.each(_json, function(index, d) {
            var verButton = '';
            // Agregar elemento <li> para cada notificación  
            if (d.fields.tipo === 'envio_solicitud') {
                verButton = '<a data-notificacion-id="' + d.pk + '" data-tipo="' + d.fields.tipo + '" class="btn btn-sm btn-secondary float-end">Ver</a>';
            } else if (d.fields.tipo === 'aprobacion' || d.fields.tipo === 'rechazo') {
                verButton = '<a data-notificacion-id="' + d.pk + '" data-tipo="' + d.fields.tipo + '" class="btn btn-sm btn-secondary float-end">Ver</a>';
            }
    
            _html += '<li class="list-group-item' +
                // Agregar clase 'leido' si la notificación está marcada como leída
                (d.fields.leido ? ' leido' : '') +
                '">' +
                '<div class="notif-content">' +
                '<span class="notif-text">' + d.fields.detalle + '</span>' +
                '<div class="notif-button">' + verButton + '</div>' +
                '</div>' +
                '</li>';
        });
    
        // Actualizar HTML con las notificaciones
        $(".notif-list").html(_html);
    
        // Actualizar contador de notificaciones no leídas
        $(".badgebg-primary").text(res.count_no_leidas);
    
        // Ocultar mensaje de cargando
        $(".ajaxRes").hide();
    }

    });

  }, 5000);

  // Manejar clic en el botón "Ver" fuera de la función setInterval
  $(".notif-list").on("click", "a.btn-secondary", function() {
    // Obtener el ID de la notificación desde el botón
    var notificacionId = $(this).data('notificacion-id');
    // Obtener el tipo de notificación desde el botón
    var tipoNotificacion = $(this).data('tipo');

    // Llamar a la vista para marcar la notificación como leída
    $.ajax({
      url: `/marcar_notificacion_leida/${notificacionId}/`,
      method: 'GET',
      dataType: 'json',
      success: function(response) {
        console.log(response.message);
        // Redirigir a la página correspondiente después de marcar como leída
        if (response.success) {
          // Determinar la redirección según el tipo de notificación
          if (tipoNotificacion === 'envio_solicitud') {
            window.location.href = '/solicitudes';
          } else if (tipoNotificacion === 'aprobacion' || tipoNotificacion === 'rechazo') {
            window.location.href = '/mis_solicitudes';
          } else {
            window.location.reload(); // Otra acción por defecto si es necesario
          }
        } else {
          console.error('Error al marcar la notificación como leída');
        }
      },
      error: function(error) {
        console.log(error.status); // status HTTP
        console.log(error.responseText); // texto de respuesta
      }
    });
  });
});