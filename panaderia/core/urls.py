from django.urls import path
from .views import inicio
from .views import QuienesSomos
from .views import Galería
from .views import contacto
from .views import pasteleria
from .views import panaderia
from .views import bebidas
from .views import api
from .views import registro
from .views import mostrar, eliminar, crearCliente, modificar
from .views import producto, modificarproducto, mostrarProducto

urlpatterns=[
    path("", inicio, name="inicio"),
    path('QuienesSomos/', QuienesSomos, name="QuienesSomos"),
    path('Galería/', Galería, name="Galería"),
    path('contacto/', contacto, name="contacto"),
    path('pasteleria/', pasteleria, name="pasteleria"),
    path('panaderia/', panaderia, name="panaderia"),
    path('bebidas/', bebidas, name="bebidas"),
    path('api/', api, name="api"),
    path('registro/', registro, name="registro"),
    path('mostrar/', mostrar, name="mostrar"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('crearCliente/', crearCliente, name="crearCliente"),
    path('modificar/', modificar, name="modificar"),
    path('producto/', producto, name="producto"),
    path('modificarproducto/', modificarproducto, name="modificarproducto"),
    path('mostrarProducto/', mostrarProducto, name="mostrarProducto"),
]