from django.shortcuts import render, redirect
from .models import Pedido, Cliente, Lanche, Acompanhamento, Bebida
from .form import PedidoForm, LancheForm, AcompanhamentoForm, BebidaForm, ClienteForm


# Views de atualizaçãp de registro
def up_pedido(request, pk):
    data = {}
    uppedido = Pedido.objects.get(pk=pk)
    form = PedidoForm(request.POST or None, instance=uppedido)
    if form.is_valid():
        form.save()
        return redirect('url_lista_pedido')
    data['form'] = form
    return render(request, "hamburgueria/cadastros.html", data)


def up_lanche(request, pk):
    data = {}
    uplanche = Lanche.objects.get(pk=pk)
    form = LancheForm(request.POST or None, instance=uplanche)
    if form.is_valid():
        form.save()
        return redirect('url_cardapio')
    data['form'] = form
    return render(request, "hamburgueria/cadastros.html", data)


def up_acompanhamento(request, pk):
    data = {}
    upacompanhamento = Acompanhamento.objects.get(pk=pk)
    form = AcompanhamentoForm(request.POST or None, instance=upacompanhamento)
    if form.is_valid():
        form.save()
        return redirect('url_cardapio')
    data['form'] = form
    return render(request, "hamburgueria/cadastros.html", data)


def up_bebida(request, pk):
    data = {}
    upbebida = Bebida.objects.get(pk=pk)
    form = BebidaForm(request.POST or None, instance=upbebida)
    if form.is_valid():
        form.save()
        return redirect('url_cardapio')
    data['form'] = form
    return render(request, "hamburgueria/cadastros.html", data)


def up_cliente(request, pk):
    data = {}
    upcliente = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=upcliente)
    if form.is_valid():
        form.save()
        return redirect('url_buscar_cliente')
    data['form'] = form
    return render(request, "hamburgueria/cadastros.html", data)


# Views de pesquisa de registros
def busca_cliente(request):
    nome = request.POST.get("nome")
    if nome:
        data = {"clientes": Cliente.objects.filter(nome_cliente__contains=nome)}
    else:
        data = {"clientes": ""}
    return render(request, "hamburgueria/cliente.html", data)


# Views de listagem de td tabela
def pedido(request):
    data = {"pedidos": Pedido.objects.all().order_by('-num_pedido')}
    return render(request, "hamburgueria/pedidos.html", data)


def cardapio(request):
    data = {"lanches": Lanche.objects.all().order_by('-valor_lanche'),
            "acompanhamentos": Acompanhamento.objects.all().order_by('-valor_acompanhamento'),
            "bebidas": Bebida.objects.all().order_by('-valor_bebida')}
    return render(request, "hamburgueria/cardapio.html", data)


def clicardapio(request):
    data = {"lanches": Lanche.objects.all().order_by('-valor_lanche'),
            "acompanhamentos": Acompanhamento.objects.all().order_by('-valor_acompanhamento'),
            "bebidas": Bebida.objects.all().order_by('-valor_bebida')}
    return render(request, "hamburgueria/cliCardapio.html", data)


def clientes(request):
    data = {"clientes": Cliente.objects.all()}
    return render(request, "hamburgueria/clientes.html", data)


# Views de cadastro de registros
def cli_cad_pedido(request):
    data = {}
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("url_home")
    data["form"] = form
    return render(request, "hamburgueria/cliCadastros.html", data)


def cad_pedido(request):
    data = {}
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("url_lista_pedido")
    data["form"] = form
    return render(request, "hamburgueria/cadastros.html", data)


def cad_lanche(request):
    data = {}
    form = LancheForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("url_cardapio")
    data["form"] = form
    return render(request, "hamburgueria/cadastros.html", data)


def cad_acompanhamento(request):
    data = {}
    form = AcompanhamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("url_cardapio")
    data["form"] = form
    return render(request, "hamburgueria/cadastros.html", data)


def cad_bebida(request):
    data = {}
    form = BebidaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("url_cardapio")
    data["form"] = form
    return render(request, "hamburgueria/cadastros.html", data)


def cad_cliente(request):
    data = {}
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("url_buscar_cliente")
    data["form"] = form
    return render(request, "hamburgueria/cadastros.html", data)


def cli_cad_cliente(request):
    data = {}
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("url_home")
    data["form"] = form
    return render(request, "hamburgueria/cliCadastros.html", data)


# Views de exclusão de registros
def del_pedido(request, pk):
    delpedido = Pedido.objects.get(pk=pk)
    delpedido.delete()
    return redirect('url_lista_pedido')


def del_lanche(request, pk):
    dellanche = Lanche.objects.get(pk=pk)
    dellanche.delete()
    return redirect('url_cardapio')


def del_acompanhamento(request, pk):
    delacompanhamento = Acompanhamento.objects.get(pk=pk)
    delacompanhamento.delete()
    return redirect('url_cardapio')


def del_bebida(request, pk):
    delbebida = Bebida.objects.get(pk=pk)
    delbebida.delete()
    return redirect('url_cardapio')


def del_cliente(request, pk):
    delcliente = Cliente.objects.get(pk=pk)
    delcliente.delete()
    return redirect('url_buscar_cliente')


# Views simples
def sobre(request):
    return render(request, "hamburgueria/sobre.html")


def home(request):
    return render(request, "hamburgueria/index.html")

