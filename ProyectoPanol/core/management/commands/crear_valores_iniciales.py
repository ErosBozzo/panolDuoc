from django.core.management.base import BaseCommand
from core.models import Departamento, RolUsuario, EstadoUsuario, EstadoProducto, Producto

class Command(BaseCommand):
    help = 'Agrega valores iniciales a los modelos'

    def handle(self, *args, **options):
        self.crear_valores_iniciales()

    def crear_valores_iniciales(self):
        # Departamento
        Departamento.objects.get_or_create(idDepartamento=1, depto="Informatica")
        Departamento.objects.get_or_create(idDepartamento=2, depto="Diseño")

        # RolUsuario
        RolUsuario.objects.get_or_create(idRol=1, rol="Profesor")
        RolUsuario.objects.get_or_create(idRol=2, rol="Alumno")
        RolUsuario.objects.get_or_create(idRol=3, rol="Encargado")

        # EstadoUsuario
        EstadoUsuario.objects.get_or_create(idEstadoUsuario=1, estadoUsuario="Normal")
        EstadoUsuario.objects.get_or_create(idEstadoUsuario=2, estadoUsuario="Bloqueado")

        # EstadoProducto
        EstadoProducto.objects.get_or_create(idEstadoProducto=1, estadoProducto="Disponible")
        EstadoProducto.objects.get_or_create(idEstadoProducto=2, estadoProducto="Dado de baja")

        # Producto
        Producto.objects.get_or_create(nombreProducto='Bobina de lanzamiento 500m', esFungible=False, estadoProducto=EstadoProducto.objects.get(idEstadoProducto=1), marca='BX616', modelo='MMPC 500M', stock="2", stockMinimo="1", descripcion='Herramienta que se utiliza para analizar los posibles problemas y averías en una línea de fibra óptica.', imagen="images/bobina500.jpeg", departamento=Departamento.objects.get(idDepartamento=1), ubicacionRack="2")
        Producto.objects.get_or_create(nombreProducto='Bobina de lanzamiento 1km', esFungible=False, estadoProducto=EstadoProducto.objects.get(idEstadoProducto=1), marca='BX616', modelo='MMPC 1K', stock="1", stockMinimo="1", descripcion='Herramienta que se utiliza para analizar los posibles problemas y averías en una línea de fibra óptica.', imagen="images/bobina1000.jpeg", departamento=Departamento.objects.get(idDepartamento=1), ubicacionRack="2")
        Producto.objects.get_or_create(nombreProducto='Bobina de lanzamiento 2km', esFungible=False, estadoProducto=EstadoProducto.objects.get(idEstadoProducto=1), marca='BX616', modelo='MMPC 2K', stock="4", stockMinimo="1", descripcion='Herramienta que se utiliza para analizar los posibles problemas y averías en una línea de fibra óptica.', imagen="images/bobina2000.jpeg", departamento=Departamento.objects.get(idDepartamento=1), ubicacionRack="2")
        Producto.objects.get_or_create(nombreProducto='Detector de gas', esFungible=False, estadoProducto=EstadoProducto.objects.get(idEstadoProducto=1), marca='Hanwei Electronics', modelo='BX616', stock="2", stockMinimo="1", descripcion='Dispositivos de seguridad que se utilizan para detectar gases tóxicos o explosivos en el aire.', imagen="images/detector_gas.jpeg", departamento=Departamento.objects.get(idDepartamento=1), ubicacionRack="2")
        Producto.objects.get_or_create(nombreProducto='Conversor de media', esFungible=False, estadoProducto=EstadoProducto.objects.get(idEstadoProducto=1), marca='OPNET', modelo='SM-20 SC', stock="2", stockMinimo="1", descripcion='Dispositivo que se utiliza para conectar diferentes tipos de medios de red, como cobre y fibra óptica.', imagen="images/conv_media.jpeg", departamento=Departamento.objects.get(idDepartamento=1), ubicacionRack="2")
        Producto.objects.get_or_create(nombreProducto='Microscopio de fibra Leviton', esFungible=False, estadoProducto=EstadoProducto.objects.get(idEstadoProducto=1), marca='Leviton', modelo='Regular', stock="5", stockMinimo="2", descripcion='Microscopio diseñado para inspeccionar equipos de fibra óptica.', imagen="images/microsc_leviton.jpeg", departamento=Departamento.objects.get(idDepartamento=1), ubicacionRack="2")
        Producto.objects.get_or_create(nombreProducto='Microscopio de fibra Komshine', esFungible=False, estadoProducto=EstadoProducto.objects.get(idEstadoProducto=1), marca='Konshine', modelo='Regular', stock="3", stockMinimo="1", descripcion='Microscopio diseñado para inspeccionar equipos de fibra óptica.', imagen="images/microsc_komshine.jpeg", departamento=Departamento.objects.get(idDepartamento=1), ubicacionRack="2")
        Producto.objects.get_or_create(nombreProducto='Modem', esFungible=False, estadoProducto=EstadoProducto.objects.get(idEstadoProducto=1), marca='G/epon onu', modelo='WK3802W', stock="3", stockMinimo="2", descripcion='Dispositivo que se utiliza para conectar una computadora a Internet.', imagen="images/modem.jpeg", departamento=Departamento.objects.get(idDepartamento=1), ubicacionRack="2")
        Producto.objects.get_or_create(nombreProducto='Amplificador Optico Nodo', esFungible=False, estadoProducto=EstadoProducto.objects.get(idEstadoProducto=1), marca='IP01', modelo='2600', stock="9", stockMinimo="3", descripcion='Dispositivo que se usa en las redes de cable y fibra óptica para aumentar la potencia de la señal.', imagen="images/amp_optico_2600.jpeg", departamento=Departamento.objects.get(idDepartamento=1), ubicacionRack="3")
        Producto.objects.get_or_create(nombreProducto='Amplificador BTD Troncal', esFungible=False, estadoProducto=EstadoProducto.objects.get(idEstadoProducto=1), marca='LH', modelo='la8630t-SIII', stock="3", stockMinimo="1", descripcion='Dispositivo de banda ancha que se utiliza en las redes de cable y fibra óptica para amplificar la señal de RF.', imagen="images/amp_btd_troncal.jpeg", departamento=Departamento.objects.get(idDepartamento=1), ubicacionRack="3")
        Producto.objects.get_or_create(nombreProducto='Taladro', esFungible=False, estadoProducto=EstadoProducto.objects.get(idEstadoProducto=1), marca='Bauker', modelo='e0220159603', stock="2", stockMinimo="1", descripcion='Herramienta giratoria que se utiliza para perforar agujeros en diferentes materiales.', imagen="images/taladro_bauker.jpeg", departamento=Departamento.objects.get(idDepartamento=1), ubicacionRack="3")

        self.stdout.write(self.style.SUCCESS('Valores por defecto agregados con éxito.'))
