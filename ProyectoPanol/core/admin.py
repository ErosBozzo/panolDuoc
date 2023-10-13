from django.contrib import admin
from .models import Departamento, Producto, CustomUser, RolUsuario, Estado


# Register your models here.


admin.site.register(Departamento)
admin.site.register(Producto)
admin.site.register(CustomUser)
admin.site.register(RolUsuario)
admin.site.register(Estado)