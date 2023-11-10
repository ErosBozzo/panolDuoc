from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
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
    
class EstadoUsuario(models.Model):
    idEstadoUsuario = models.IntegerField(primary_key=True, verbose_name="Id Estado")
    estadoUsuario = models.CharField(max_length=10, blank=False, null=False, verbose_name="Estado Usuario")

    def __str__(self):
        return self.estadoUsuario

class EstadoProducto(models.Model):
    idEstadoProducto = models.IntegerField(primary_key=True, verbose_name="Id Estado Producto")
    estadoProducto = models.CharField(max_length=20, blank=False, null=False, verbose_name="Estado Producto")

    def __str__(self):
        return self.estadoProducto

# Create Modelo para Productos

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name="Id de Producto")
    nombreProducto = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre del producto")
    esFungible = models.BooleanField(max_length=80, blank=False, null=False, verbose_name="Es fungible")
    estadoProducto = models.ForeignKey(EstadoProducto, on_delete=models.DO_NOTHING, verbose_name="Estado del producto")
    marca = models.CharField(max_length=40, blank=False, null=False, verbose_name="Marca")
    modelo = models.CharField(max_length=20, blank=False, null=False, verbose_name="Modelo")
    stock = models.IntegerField(null=False, blank=False, verbose_name="Stock")
    stockMinimo = models.IntegerField(null=False, blank=False, verbose_name="Stock Minimo")
    descripcion = models.CharField(max_length=200, blank=False, null=False, verbose_name="Descripcion del producto")
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")
    departamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING, verbose_name="Departamento")
    ubicacionRack = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(1), MaxValueValidator(12)], verbose_name="Rack")

    def __str__(self):
        return str(self.idProducto)
    
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
    estadoUsuario = models.ForeignKey(EstadoUsuario, on_delete=models.DO_NOTHING, default=1)
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
            estado = EstadoUsuario.objects.get(idEstadoUsuario=1)
            self.estado = estado
        super().save(*args, **kwargs)



class Solicitud(models.Model):
    idSolicitud = models.AutoField(primary_key=True, verbose_name="Id de Solicitud")
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='solicitudes', verbose_name="Usuario")
    fecha_solicitud = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Solicitud")
    fecha_retiro = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de Retiro")
    fecha_devolucion = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de Devolución")
    fecha_devolucion_efectiva = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de Devolución Efectiva")
    estaAprobado = models.BooleanField(default=False, verbose_name="Está Aprobado")
    productos = models.ManyToManyField(Producto, through='ProductosSolicitud', related_name='solicitudes', verbose_name="Productos")
    comentarios = models.TextField(blank=True, verbose_name="Comentarios")
    

    def save(self, *args, **kwargs):
        # Si la fecha de retiro se establece, calcula automáticamente la fecha de devolución
        if self.fecha_retiro:
            self.fecha_devolucion = self.fecha_retiro + timezone.timedelta(days=7)
        super().save(*args, **kwargs)


class ProductosSolicitud(models.Model):
    idProductosSolicitud = models.AutoField(primary_key=True, verbose_name="Id de ProductosSolicitud")
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, verbose_name="Solicitud")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    cantidad = models.PositiveIntegerField(default=1, verbose_name="Cantidad")

class Notificacion(models.Model):
    TIPO_CHOICES = (
        ('envio_solicitud', 'Usuario ha enviado una solicitud'),
        ('aprobacion', 'Tu solicitud fue aprobada'),
        ('rechazo', 'Tu solicitud fue rechazada'),
        # Puedes agregar más tipos de notificaciones según tus necesidades
    )

    detalle = models.TextField()
    leido = models.BooleanField(default=False)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='nombre_notificaciones')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    fecha_notificacion = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.usuario.username}"