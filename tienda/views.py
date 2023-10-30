from django.shortcuts import render
from .models import Producto
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def tienda(request):

	productos = Producto.objects.all()
	return render(request, 'tienda/tienda.html', {'productos': productos})
