from django.contrib.auth import login, authenticate
from functools import partial
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import Producto, Departamento, Cart, CartItem, CustomUser, Estado
from .forms import ProductoForm, CustomUserForm
from django.db import models
from django.db.models import Sum
from django.urls import reverse
from django.contrib import messages
# Create your views here.


def home(request):
    data = {"list": Producto.objects.all().order_by('idProducto')}
    return render(request, "core/home.html", data)


def registro(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                custom_user = form.save()
                Cart.objects.create(user=custom_user)

                messages.success(request, 'Registro exitoso. ¡Inicia sesión!')
                return redirect('home')
            else:
                messages.error(request, 'Las contraseñas no coinciden. Por favor, inténtalo de nuevo.')
        else:
            messages.error(request, 'Error en el formulario. Por favor, verifica los campos.')

    else:
        form = CustomUserForm()

    return render(request, 'core/registro.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                # Redirige al usuario a la página 'home' tras el inicio de sesión exitoso

                # Verifica si el usuario tiene un carrito, y créalo si no lo tiene
                if not Cart.objects.filter(user=user).exists():
                    Cart.objects.create(user=user)

                return redirect('home')
            else:
                # El inicio de sesión falló, muestra un mensaje de error
                error_message = 'Nombre de usuario o contraseña incorrectos.'
                return render(request, 'core/login.html', {'form': form, 'error_message': error_message})
        else:
            # El formulario no es válido, muestra un mensaje de error
            error_message = 'Error en el formulario. Por favor, verifica los campos.'
            return render(request, 'core/login.html', {'form': form, 'error_message': error_message})
    
    else:
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})

@login_required
def carrito_compra(request):
    return render(request, "core/carrito_compra.html")

def producto_ficha(request, id):
    producto = Producto.objects.get(idProducto=id)
    print(f"idProducto: {id}")  # Agrega esta línea para imprimir el valor de idProducto
    data = {"producto": producto}
    return render(request, "core/producto_ficha.html", data)


def es_encargado(user, idRol):
    return user.rol.idRol == idRol

# Validador para encargados
es_encargado_encargado = partial(es_encargado, idRol=3)  # Reemplaza "1" con el ID correcto de "encargado"

@user_passes_test(es_encargado_encargado)
def producto(request, action, id):
    data = {"mesg": "", "form": ProductoForm, "action": action, "id": id}


    if action == 'ins':
        if request.method == "POST":
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El producto fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos producto con la misma id!"


    elif action == 'upd':
        objeto = Producto.objects.get(idProducto=id)
        if request.method == "POST":
            form = ProductoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El producto fue actualizado correctamente!"
        data["form"] = ProductoForm(instance=objeto)


    elif action == 'del':
        try:
            Producto.objects.get(idProducto=id).delete()
            data["mesg"] = "¡El producto fue eliminado correctamente!"
            return redirect(producto, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El producto ya estaba eliminado!"


    data["list"] = Producto.objects.all().order_by('idProducto')
    return render(request, "core/producto.html", data)



def add_to_cart(request, product_id):
    if request.method == 'POST':
        quantity_str = request.POST.get('quantity', '1')
        
        if not quantity_str.isdigit():
            messages.error(request, 'La cantidad ingresada no es válida.')
            return redirect(reverse('producto_ficha', args=[product_id]))
        
        quantity = int(quantity_str)
        
        product = Producto.objects.get(pk=product_id)
        user_cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)

        # Obtener el valor de stock y stock mínimo del producto
        stock = product.stock
        stock_minimo = product.stockMinimo
        stock_disponible = stock - stock_minimo - cart_item.quantity  # Restar lo que ya está en el carrito

        # Calcular la cantidad máxima que se puede solicitar
        cantidad_maxima = min(stock_disponible, stock - stock_minimo)

        if quantity > cantidad_maxima:
            messages.error(request, f'No puedes solicitar más de {cantidad_maxima} unidades de {product.nombreProducto}.')
        elif quantity < 1:
            messages.error(request, 'La cantidad ingresada no es válida.')
        else:
            cart_item.quantity += quantity
            cart_item.save()
            messages.success(request, f'Se agregaron {quantity} {product.nombreProducto} al carrito.')

    return redirect(reverse('producto_ficha', args=[product_id]))




def remove_from_cart(request, product_id):
    if request.user.is_authenticated:
        try:
            product = Producto.objects.get(idProducto=product_id)
            cart = Cart.objects.get(user=request.user)
            cart_item = CartItem.objects.get(cart=cart, product=product)
            cart_item.delete()
        except (Producto.DoesNotExist, Cart.DoesNotExist, CartItem.DoesNotExist):
            pass  # Puedes manejar errores de la manera que prefieras

    return redirect('carrito_compra')




def clear_cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
        cart.cartitem_set.all().delete()  # Elimina todos los elementos del carrito
    return redirect('carrito_compra')


def buscar_productos(request):
    query = request.GET.get('q')

    # Realiza la búsqueda en la base de datos
    productos = Producto.objects.filter(
        models.Q(idProducto__icontains=query) | models.Q(nombreProducto__icontains=query)
    )

    return render(request, 'core/home.html', {'list': productos})

    
def carrito_compra(request):
    # Obtener el carrito del usuario actual (esto puede variar dependiendo de tu implementación de autenticación)
    user_cart = Cart.objects.get(user=request.user)
    # Obtener los elementos del carrito para ese carrito
    cart_items = CartItem.objects.filter(cart=user_cart)

    data = {
        "cart_items": cart_items
    }
    return render(request, "core/carrito_compra.html", data)


def producto_ficha(request, id, error_message=None):
    producto = Producto.objects.get(idProducto=id)
    data = {"producto":  producto, "error_message": error_message}
    return render(request, "core/producto_ficha.html", data)


def poblar_bd(request):
    Producto.objects.all().delete()
    Producto.objects.create(idProducto="001", nombreProducto='Taladro', esFungible=False, stock="9", stockMinimo="6", descripcion='Ta ladrando', imagen="images/taladro.png", departamento=Departamento.objects.get(idDepartamento=1))
    Producto.objects.create(idProducto="002", nombreProducto='Martillo', esFungible=False, stock="10", stockMinimo="5", descripcion='El de thor', imagen="images/martillo.png", departamento=Departamento.objects.get(idDepartamento=1))
    Producto.objects.create(idProducto="003", nombreProducto='Pintura', esFungible=False, stock="40", stockMinimo="30", descripcion='Pinta', imagen="images/pintura.png", departamento=Departamento.objects.get(idDepartamento=2))
    Producto.objects.create(idProducto="004", nombreProducto='Cable USB', esFungible=False, stock="50", stockMinimo="20", descripcion='Conecta USB', imagen="images/usb.png", departamento=Departamento.objects.get(idDepartamento=1))
    Producto.objects.create(idProducto="005", nombreProducto='Cable HDMI', esFungible=False, stock="50", stockMinimo="25", descripcion='Conecta HDMI', imagen="images/sinfoto.jpg", departamento=Departamento.objects.get(idDepartamento=1))
    Producto.objects.create(idProducto="006", nombreProducto='Adaptador HDMI', esFungible=True, stock="40", stockMinimo="50", descripcion='Adapta HDMI', imagen="images/sinfoto.jpg", departamento=Departamento.objects.get(idDepartamento=1))
    Producto.objects.create(idProducto="007", nombreProducto='Televisor', esFungible=False, stock="10", stockMinimo="5", descripcion='Para ver tele', imagen="images/sinfoto.jpg", departamento=Departamento.objects.get(idDepartamento=1))
    Producto.objects.create(idProducto="008", nombreProducto='Pincel', esFungible=True, stock="60", stockMinimo="20", descripcion='Para pintar', imagen="images/sinfoto.jpg", departamento=Departamento.objects.get(idDepartamento=2))
    return redirect(producto, action='ins', id = '-1')