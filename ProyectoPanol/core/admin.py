from django.contrib import admin
from .models import Departamento, Producto, CustomUser, RolUsuario, EstadoUsuario, EstadoProducto, Solicitud, Notificacion


# Register your models here.


admin.site.register(Departamento)
admin.site.register(Producto)
admin.site.register(CustomUser)
admin.site.register(RolUsuario)
admin.site.register(EstadoUsuario)
admin.site.register(EstadoProducto)
admin.site.register(Solicitud)

class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'usuario', 'fecha_notificacion', 'leido')  # Asegúrate de incluir 'fecha_notificacion'
    list_filter = ('tipo', 'leido', 'usuario')
    search_fields = ('tipo', 'usuario__username', 'fecha_notificacion')

admin.site.register(Notificacion, NotificacionAdmin)