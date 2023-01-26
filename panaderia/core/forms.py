from django import forms
from django.forms import ModelForm 
from django.forms import widgets #permite definir la configuración de los datos de entrada del form
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Cliente
from .models import producto

class ClienteForm(forms.ModelForm):
    
    class Meta: #permite configurar el form 
        model = Cliente 
        fields = ['id', 'Nombre', 'Apellido', 'Telefono']
        labels = {
            'id': 'id',
            'Nombre': 'Nombre',
            'Apellido': 'Apellido',
            'Telefono': 'Telefono',
        }
        widgets={
            'id': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite una ID',
                    'id': 'id'
                }
            ),
            'Nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite un Nombre',
                    'id': 'Nombre'
                }
            ),
            'Apellido': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite un Apellido',
                    'id': 'Apellido'
                }
            ),
            'Telefono':forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite un Telefono',
                    'id': 'categoria'
                }
            ),
        }

class productoForm(forms.ModelForm):
    
    class Meta: #permite configurar el form 
        model = producto
        fields = ['id', 'NombreProducto', 'precio', 'imagen']
        labels = {
            'id': 'id',
            'NombreProducto': 'NombreProducto',
            'precio': 'precio',
            'imagen': 'imagen',
        }
        widgets={
            'id': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite una ID',
                    'id': 'id'
                }
            ),
            'NombreProducto': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite nombre de producto',
                    'id': 'NombreProducto'
                }
            ),
            'precio': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite precio de producto',
                    'id': 'precio'
                }
            ),
            'Imagen':forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'Imagen',
                }
            )
        }