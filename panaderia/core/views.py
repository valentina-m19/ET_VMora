from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def QuienesSomos(request):
    return render(request, 'Quienes somos.html')

def Galería(request):
    return render(request, 'Galería.html')

def contacto(request):
    return render(request, 'contacto.html')

def pasteleria(request):
    return render(request, 'pasteleria.html')

def panaderia(request):
    return render(request, 'panaderia.html')

def bebidas(request):
    return render(request, 'bebidas.html')

def api(request):
    return render(request, 'API.html')

def registro(request):
    return render(request, 'registro.html')

def mostrar(request):
    clientes = Cliente.objects.all()
    datos={
        'usuario': clientes
    }
    return render(request, 'mostrar.html', datos)
    
def eliminar(request, id):
    cliente = Clientes.objects.get(Nombre=id)
    cliente.delete()
    return redirect('mostrar')


def crearCliente(request):
    if request.method=='POST': 
        clienteform = ClienteForm(request.POST)
        if clienteform.is_valid():
            clienteform.save()     #similar al insert
            return redirect('mostrar')
    else:
        clienteform=ClienteForm()
    return render(request, 'crearCliente.html', {'clienteform': clienteform})

def modificar(request, id):
    cliente = Clientes.objects.get(Nombre=id)
    datos={
        'form': ClienteForm(instance=cliente)
    }

    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar')
    
    return render(request, 'modificar.html', datos)

def producto(request):
    if request.method=='POST': 
        productoform = productoForm(request.POST)
        if productoform.is_valid():
            productoform.save()     #similar al insert
            return redirect('mostrarProducto')
    else:
        productoform=productoForm()
    return render(request, 'producto.html', {'productoform': productoform})

def mostrarProducto(request):
    productos = producto.objects.all()
    datos={
        'ingreso': productos
    }
    return render(request, 'mostrarProducto.html', datos)
    
def eliminar(request, id):
    producto = producto.objects.get(Nombre=id)
    producto.delete()
    return redirect('mostrarProducto')

def modificarproducto(request, id):
    producto = producto.objects.get(Nombre=id)
    datos={
        'form': productoForm(instance=producto)
    }

    if request.method=='POST':
        formulario = productoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrarProducto')
    
    return render(request, 'modificarproducto.html', datos)