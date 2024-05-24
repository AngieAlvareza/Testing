from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Proveedor, Producto

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PedidoForm(forms.Form):
    proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all())
    productos = forms.ModelMultipleChoiceField(queryset=Producto.objects.all(), widget=forms.CheckboxSelectMultiple)
    cantidades = forms.CharField(widget=forms.Textarea)

    def clean_cantidades(self):
        cantidades = self.cleaned_data['cantidades']
        cantidades_list = cantidades.split(',')
        if any(int(cantidad) < 1 or int(cantidad) > 100 for cantidad in cantidades_list):
            raise forms.ValidationError("Cada cantidad debe ser un número entre 1 y 100.")
        return cantidades_list
    