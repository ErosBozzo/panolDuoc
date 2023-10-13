from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.


# Create Modelo para Categoria


class Departamento(models.Model):
    idDepartamento = models.IntegerField(primary_key=True, verbose_name="Id de Departamento")
    depto = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre del departamento")

    def __str__(self):
        return self.depto
    
class RolUsuario(models.Model):
    idRol = models.IntegerField(primary_key=True, verbose_name="Id Rol")
    rol = models.CharField(max_length=12, blank=False, null=False, verbose_name="Rol")

    def __str__(self):
        return self.rol
    
class Estado(models.Model):
    idEstado = models.IntegerField(primary_key=True, verbose_name="Id Estado")
    estado = models.CharField(max_length=10, blank=False, null=False, verbose_name="Estado")

    def __str__(self):
        return self.estado



# Create Modelo para vehículo


class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="Id de Producto")
    nombreProducto = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre del producto")
    esFungible = models.BooleanField(max_length=80, blank=False, null=False, verbose_name="Es fungible")
    stock = models.IntegerField(null=False, blank=False, verbose_name="Stock")
    stockMinimo = models.IntegerField(null=False, blank=False, verbose_name="Stock Minimo")
    descripcion = models.CharField(max_length=200, blank=False, null=False, verbose_name="Descripcion del producto")
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")
    departamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.idProducto
    
    class Meta:
        permissions = [
            ("can_view_producto", "Puede ver la página de productos"),
        ]
    
    
class Cart(models.Model):
    user = models.ForeignKey('core.CustomUser', on_delete=models.CASCADE)
    products = models.ManyToManyField('Producto', through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('Producto', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)



class CustomUser(AbstractUser):
    idUsuario = models.AutoField(primary_key=True)
    correo = models.EmailField(unique=True, max_length=60)
    sede = models.CharField(max_length=45)
    rol = models.ForeignKey(RolUsuario, on_delete=models.DO_NOTHING, default=1)
    estado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING, default=1)
    departamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING, default=1)

    # Agregar related_name para evitar el conflicto de nombres
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='custom_user_groups'  # Cambia el nombre como prefieras
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_user_permissions'  # Cambia el nombre como prefieras
    )

    def __str__(self):
        return self.username
    def save(self, *args, **kwargs):
        # Asigna automáticamente el valor 1 a 'estado' al crear un nuevo usuario
        if not self.idUsuario:
            estado = Estado.objects.get(idEstado=1)
            self.estado = estado
        super().save(*args, **kwargs)
