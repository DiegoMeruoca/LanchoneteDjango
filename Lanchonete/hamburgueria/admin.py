from django.contrib import admin
from .models import Acompanhamento, Bebida, Cliente, Lanche, Pedido
# Register your models here.

admin.site.register(Acompanhamento)
admin.site.register(Bebida)
admin.site.register(Cliente)
admin.site.register(Lanche)
admin.site.register(Pedido)
