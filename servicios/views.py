from django.shortcuts import render
from .models import Servicio
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def servicios(request):

	servicios = Servicio.objects.all()
	return render(request, 'servicios.html', {'servicios': servicios})