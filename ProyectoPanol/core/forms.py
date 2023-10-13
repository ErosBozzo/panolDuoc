from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, fields
from .models import Producto, CustomUser, RolUsuario, Estado, Departamento


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto', 'nombreProducto', 'esFungible', 'stock', 'stockMinimo', 'descripcion', 'imagen', 'departamento']

class CustomUserForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    estado = forms.HiddenInput(attrs={'value': 1})

    class Meta:
        model = CustomUser
        fields = ('username', 'correo', 'sede', 'rol', 'departamento', 'password1', 'password2')
