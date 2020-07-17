"""Lanchonete URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hamburgueria import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('pedido', views.pedido, name="url_lista_pedido"),
    path('cardapio', views.cardapio, name="url_cardapio"),
    path('cli_cardapio', views.clicardapio, name="url_cli_cardapio"),

    path('cadastro_pedido/', views.cad_pedido, name="url_cadastro_pedido"),
    path('cli_cadastro_pedido/', views.cli_cad_pedido, name="url_cli_cadastro_pedido"),
    path('cadastro_lanche/', views.cad_lanche, name="url_cadastro_lanche"),
    path('cadastro_acompanhamento/', views.cad_acompanhamento, name="url_cadastro_acompanhamento"),
    path('cadastro_bebida/', views.cad_bebida, name="url_cadastro_bebida"),
    path('cadastro_cliente/', views.cad_cliente, name="url_cadastro_cliente"),
    path('cli_cadastro_cliente/', views.cli_cad_cliente, name="url_cli_cadastro_cliente"),

    path('busca_cliente/', views.busca_cliente, name="url_buscar_cliente"),

    path('up_pedido/<int:pk>', views.up_pedido, name="url_up_pedido"),
    path('up_lanche/<int:pk>', views.up_lanche, name="url_up_lanche"),
    path('up_acompanhamento/<int:pk>', views.up_acompanhamento, name="url_up_acompanhamento"),
    path('up_bebida/<int:pk>', views.up_bebida, name="url_up_bebida"),
    path('up_cliente/<int:pk>', views.up_cliente, name="url_up_cliente"),

    path('del_pedido/<int:pk>', views.del_pedido, name="url_del_pedido"),
    path('del_lanche/<int:pk>', views.del_lanche, name="url_del_lanche"),
    path('del_acompanhamento/<int:pk>', views.del_acompanhamento, name="url_del_acompanhamento"),
    path('del_bebida/<int:pk>', views.del_bebida, name="url_del_bebida"),
    path('del_cliente/<int:pk>', views.del_cliente, name="url_del_cliente"),

    path('sobre/', views.sobre, name="url_sobre"),
    path('', views.home, name="url_home"),
]
