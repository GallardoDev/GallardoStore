from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.

# Vista para la página de inicio (home)

def principal(request):
	return render(request, 'principal.html')

# Vista para la página de registro (signup)
def signup(request):

	# Cuando se solicita el acceso a la página, se accede al formulario de registro

	if request.method == 'GET':
		return render(request, 'signup.html', {
		'form': UserCreationForm
		})
	else:
		# Cuando se envían los datos en el formulario, se comprueba que las claves sean iguales

		if request.POST['password1'] == request.POST['password2']:
			# Se registra el usuario
			try:
				# Del objeto User de Django, se ejecuta el método create_user
				# Se le asigna el valor de 'username' ingresado en el formulario, a la variable username

				user = User.objects.create_user(username=request.POST['username'], password=request.POST['password2'], email=request.POST['email'])

				# Se guarda el nuevo user en la BBDD

				user.save()

				# Al objeto login de Django, se le pasa el request y el user creado

				login(request, user)

				# Se redirecciona a la página tasks

				return redirect('principal')

			except IntegrityError:

				# En caso de que el usuario ya exista, se renderiza la página signup con un mensaje de error

				return render(request, 'signup.html', {
		'form': UserCreationForm,
		'error': 'User already exist'
		})
		
		# Si las claves no son iguales, se renderiza la misma página con un mensaje de error

		return render(request, 'signup.html', {
		'form': UserCreationForm,
		'error': 'Passwords do not match'
		})
		print('Obteniendo datos')
		print(request.POST)
	

@login_required
def signout(request):
	logout(request)
	return redirect('principal')

def signin(request):
	if request.method == 'GET':
		print(request.GET)
		return render(request, 'signin.html', {
			'form': AuthenticationForm
			})
	else:
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		
		if user is None:
			print(request.POST)
			return render(request, 'signin.html', {
				'form': AuthenticationForm,
				'error': 'username or passwords is icorrect'
				})
		else:
			print(request.POST)
			login(request, user)
			return redirect('principal')
			
		