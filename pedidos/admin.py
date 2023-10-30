from django.contrib import admin
from .models import Pedido
from .models import LineaPedido

# Register your models here.

admin.site.register([Pedido, LineaPedido])