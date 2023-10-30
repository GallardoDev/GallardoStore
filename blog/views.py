from django.shortcuts import render
from .models import Post, Categoria
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def blog(request):

	posts = Post.objects.all()
	return render(request, 'blog.html', {'posts': posts})

def leer_blog(request):

	return render(request, 'leer_blog.html')

@login_required
def categoria(request, categoria_id):

	categoria = Categoria.objects.get(id=categoria_id)
	posts = Post.objects.filter(categorias=categoria)
	return render(request, 'categorias.html', {'categoria': categoria, 'posts': posts})