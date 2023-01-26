from django.db import models

# Create your models here.

class Cliente(models.Model):
    id=models.CharField(max_length=6, primary_key=True, verbose_name='id')
    Nombre=models.CharField(max_length=20, verbose_name='Nombre')
    Apellido=models.CharField(max_length=20, verbose_name='Apellido')
    Telefono=models.CharField(max_length=9, verbose_name='Telefono')

    def __str__(self):
        return self.Nombre

class producto(models.Model):
    id=models.CharField(max_length=6, primary_key=True, verbose_name='id')
    NombreProducto=models.CharField(max_length=20, verbose_name='NombreProducto')
    precio=models.CharField(max_length=20, verbose_name='precio')
    Imagen=models.ImageField(upload_to="productos", null=True)
    

    def __str__(self):
        return self.NombreProducto