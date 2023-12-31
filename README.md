
# **Pañol Digital DUOC**

![](https://github.com/ErosBozzo/panolDuoc/blob/master/ProyectoPanol/core/static/core/icons/iconopag.png?raw=true)


### Sobre nuestro proyecto

El proyecto "Pañol Digital DUOC" tiene como objetivo diseñar e implementar una solución informática que digitalice el proceso de préstamo de herramientas y bienes fungibles del pañol en DUOC. Esta solución consiste en un software que funcionará a través del navegador, donde los usuarios podrán crear solicitudes de préstamo que serán controladas por un encargado, quien además podrá gestionar el inventario. La implementación de esta solución supondrá una mejora significativa en la eficiencia del pañol, ya que agilizará los procesos que se hacen de manera manual actualmente, reduciendo los tiempos de espera para los usuarios y así dando un paso hacia la era digital.

### Características

- Gestión de usuarios y roles (Profesor, Alumno y Encargado)
- Gestión de inventario (Control de stock minimo, identificación y ubicación de los productos)
- Gestión de solicitudes de préstamo (Fechas de prestamo, fecha de devolución)
- Control de atrasos en la devolución.
- Notificaciones sobre solicitudes nuevas solicitudes (encargado), solicitudes aprobadas y solicitudes rechazadas (profesor y alumno)
- Exportar reportes del listado de productos a excel según departamento y disponibilidad.

### Requisitos para el entorno de desarollo

- asgiref==3.7.2
- Django==4.2.5
- djangorestframework==3.14.0
- et-xmlfile==1.1.0
- mysqlclient==2.2.0
- openpyxl==3.1.2
- Pillow==10.0.1
- pytz==2023.3.post1
- sqlparse==0.4.4
- tzdata==2023.3

### Instalación del ambiente de desarrollo:


	python -m pip install --upgrade pip
	pip install --upgrade virtualenv
	python -m venv "C:\test\ProyectoPanol_venv"
	call cd "C:\test"
	call ProyectoPanol_venv\Scripts\activate.bat
	python -m pip install --upgrade pip
	pip install asgiref==3.7.2
	pip install Django==4.2.5
	pip install et-xmlfile==1.1.0
	pip install mysqlclient==2.2.0
	pip install openpyxl==3.1.2
	pip install Pillow==10.0.1
	pip install djangorestframework==3.14.0
	pip install pytz==2023.3.post1
	pip install sqlparse==0.4.4
	pip install tzdata==2023.3
	cd "C:\test"
	django-admin startproject ProyectoPanol
	cd ProyectoPanol
	python manage.py startapp core
	python manage.py startapp apirest
	pip freeze > requirements.txt
 	python manage.py makemigrations core
	python manage.py migrate
	python manage.py crear_valores_iniciales
    
