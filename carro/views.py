from django.shortcuts import render
from .carro import Carro
from tienda.models import Producto
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def agregar_producto(request, producto_id):

	carro = Carro(request)

	producto = Producto.objects.get(id=producto_id)

	carro.agregar(producto=producto)

	return redirect('Tienda')

@login_required
def eliminar_producto(request, producto_id):

	carro = Carro(request)

	producto = Producto.objects.get(id=producto_id)

	carro.eliminar(producto=producto)

	return redirect('Tienda')

@login_required
def restar_producto(request, producto_id):

	carro = Carro(request)

	producto = Producto.objects.get(id=producto_id)

	carro.restar_producto(producto=producto)

	return redirect('Tienda')

@login_required
def limpiar_carro(request, producto_id):

	carro = Carro(request)

	carro.limpiar_carro()

	return redirect('Tienda')