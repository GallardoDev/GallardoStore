from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def contacto(request):

	formulario_contacto = FormularioContacto()

	if request.method == 'POST':

		formulario_contacto = FormularioContacto(data=request.POST)

		if formulario_contacto.is_valid():

			nombre = request.POST.get('nombre')
			email = request.POST.get('email')
			contenido = request.POST.get('contenido')

			try:
				email = EmailMessage('Mensaje de contacto',
				 'El usuario de nombre {}, con email {}, te escribe: \n\n {}'.format(nombre, email, contenido), '', 
				 ['gallardosapp@gmail.com'], reply_to=[email])

				email.send()

				return redirect('/contacto/?valido')

			except:
			
				return redirect('/contacto/?NOvalido')
			

	return render(request, 'contacto.html', {'miFormulario': formulario_contacto})
	

