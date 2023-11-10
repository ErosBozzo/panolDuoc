from django import forms
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm, fields
from .models import Producto, CustomUser, RolUsuario, EstadoUsuario, EstadoProducto, Departamento, Solicitud, ProductosSolicitud


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto', 'nombreProducto', 'esFungible', 'estadoProducto', 'marca', 'modelo', 'stock', 'stockMinimo', 'descripcion', 'imagen', 'departamento', 'ubicacionRack']

class CustomUserForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña (RUT sin digito verificador)', widget=forms.PasswordInput)
    EstadoUsuario = forms.HiddenInput(attrs={'value': 1})

    class Meta:
        model = CustomUser
        fields = ('username', 'correo', 'sede', 'rol', 'departamento', 'password1')

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        if not password1.isdigit() or len(password1) != 8:
            raise ValidationError("La contraseña debe ser un número de 8 dígitos sin letras.")
        
        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden. Por favor, inténtalo de nuevo.")




class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['fecha_solicitud', 'fecha_retiro', 'fecha_devolucion_efectiva', 'estaAprobado']
        widgets = {
            'fecha_solicitud': forms.DateInput(attrs={'readonly': 'readonly'}),
            'fecha_retiro': forms.DateInput(attrs={'type': 'date'}),
            'fecha_devolucion_efectiva': forms.HiddenInput(),
            'estaAprobado': forms.HiddenInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_retiro = cleaned_data.get('fecha_retiro')

        # Calcula la fecha de devolución como 7 días después de la fecha de retiro
        if fecha_retiro:
            cleaned_data['fecha_devolucion_efectiva'] = fecha_retiro + timezone.timedelta(days=7)

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(SolicitudForm, self).__init__(*args, **kwargs)
        self.fields['fecha_solicitud'].widget.attrs['value'] = timezone.now().strftime('%Y-%m-%d')
        self.fields['fecha_devolucion_efectiva'].initial = None
        self.fields['estaAprobado'].initial = False

class EditarSolicitudForm(forms.ModelForm):
    OPCIONES_APROBADO = (
        (True, 'Aprobado'),
        (False, 'No Aprobado'),
    )

    estaAprobado = forms.ChoiceField(
        choices=OPCIONES_APROBADO,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    comentarios = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )

    class Meta:
        model = Solicitud
        fields = ['fecha_solicitud', 'fecha_retiro', 'fecha_devolucion_efectiva', 'estaAprobado', 'comentarios']

    def __init__(self, *args, **kwargs):
        super(EditarSolicitudForm, self).__init__(*args, **kwargs)
        self.fields['fecha_solicitud'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['fecha_retiro'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['fecha_devolucion_efectiva'].widget = forms.DateInput(attrs={'type': 'date'})

class ProductosSolicitudForm(forms.ModelForm):
    class Meta:
        model = ProductosSolicitud
        fields = ['producto', 'cantidad']