from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, poblar_bd, producto, producto_ficha, registro, carrito_compra, add_to_cart, remove_from_cart,clear_cart,buscar_productos, user_login

urlpatterns = [
    path('', home, name="home"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('producto/<action>/<id>', producto, name="Producto"),
    path('producto_ficha/<id>', producto_ficha, name="producto_ficha"),
    path('registro/', registro, name='registro'),
    path('login/', user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('carrito_compra', carrito_compra, name="carrito_compra"),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('clear_cart/', clear_cart, name='clear_cart'),
    path('buscar/', buscar_productos, name='buscar_productos'),

]
    