from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, poblar_bd, producto, producto_ficha, registro, carrito_compra, add_to_cart, remove_from_cart,clear_cart,buscar_productos, user_login, reponedor_depdiseño,reponedor_depinformatica, reponedor_depproductosdisponibles, reponedor_depproductosdadosdebaja, exportar_productos_a_excel_mantenedor,exportar_productos_a_excel_departamentoinformatica,exportar_productos_a_excel_departamentodiseño,exportar_productos_a_excel_productosdisponibles, exportar_productos_a_excel_productosdadosdebaja, todos_los_productos, determine_home_page, custom_logout, cambiar_contraseña, solicitud_exitosa, solicitud_prestamo,solicitudes, mis_solicitudes, editar_solicitud, notificaciones, obtener_notificaciones, marcar_leida

urlpatterns = [
    path('', determine_home_page, name='determine_home_page'),
    path('home/', home, name="home"),
    path('todos_los_productos', todos_los_productos, name="todos_los_productos"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('producto/<action>/<id>', producto, name="Producto"),
    path('solicitud_prestamo/<int:producto_id>/', solicitud_prestamo, name='solicitud_prestamo'),
    path('producto_ficha/<id>', producto_ficha, name="producto_ficha"),
    path('registro/', registro, name='registro'),
    path('login/', user_login, name='login'),
    path('cambiar_contraseña/', cambiar_contraseña, name='cambiar_contraseña'),
    path('logout/', custom_logout, name='logout'),
    path('carrito_compra', carrito_compra, name="carrito_compra"),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('clear_cart/', clear_cart, name='clear_cart'),
    path('buscar/', buscar_productos, name='buscar_productos'),
    path('reponedor_depdiseño/', reponedor_depdiseño, name='reponedor_depdiseño'),
    path('reponedor_depinformatica/', reponedor_depinformatica, name='reponedor_depinformatica'),
    path('reponedor_depproductosdisponibles/', reponedor_depproductosdisponibles, name='reponedor_depproductosdisponibles'),
    path('reponedor_depproductosdadosdebaja/', reponedor_depproductosdadosdebaja, name='reponedor_depproductosdadosdebaja'),
    path('exportar_productos_a_excel_mantenedor/', exportar_productos_a_excel_mantenedor, name='exportar_productos_a_excel_mantenedor'),
    path('exportar_productos_a_excel_departamentoinformatica/', exportar_productos_a_excel_departamentoinformatica, name='exportar_productos_a_excel_departamentoinformatica'),
    path('exportar_productos_a_excel_departamentodiseño/', exportar_productos_a_excel_departamentodiseño, name='exportar_productos_a_excel_departamentodiseño'),
    path('exportar_productos_a_excel_productosdisponibles/', exportar_productos_a_excel_productosdisponibles, name='exportar_productos_a_excel_productosdisponibles'),
    path('exportar_productos_a_excel_productosdadosdebaja/', exportar_productos_a_excel_productosdadosdebaja, name='exportar_productos_a_excel_productosdadosdebaja'),
    path('solicitud/', solicitud_prestamo, name='solicitud_prestamo'),
    path('solicitud_exitosa/', solicitud_exitosa, name='solicitud_exitosa'),
    path('mis_solicitudes/', mis_solicitudes, name='mis_solicitudes'),
    path('solicitudes/', solicitudes, name='solicitudes'),
    path('editar_solicitud/<int:solicitud_id>/', editar_solicitud, name='editar_solicitud'),
    path('notificaciones/', notificaciones, name='notificaciones'),
    path('obtener-notificaciones/', obtener_notificaciones, name='obtener_notificaciones'),
    path('marcar_notificacion_leida/<int:notificacion_id>/', marcar_leida, name='marcar_leida'),
    
]


    