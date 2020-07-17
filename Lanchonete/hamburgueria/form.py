from django.forms import ModelForm
from .models import Pedido, Lanche, Acompanhamento, Bebida, Cliente


class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['num_pedido', 'data', 'horario', 'cliente', 'lanches', 'bebidas', 'acompanhamentos']


class LancheForm(ModelForm):
    class Meta:
        model = Lanche
        fields = ['nome_lanche','valor_lanche', 'descricao']


class AcompanhamentoForm(ModelForm):
    class Meta:
        model = Acompanhamento
        fields = ['nome_acompanhamento','valor_acompanhamento', 'descricao']


class BebidaForm(ModelForm):
    class Meta:
        model = Bebida
        fields = ['nome','tipo','marca','valor_bebida', 'descricao']


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['cpf_cliente',
                  'nome_cliente',
                  'email_cliente',
                  'telefone_cliente',
                  'logradouro',
                  'numero',
                  'complemento',
                  'bairro',
                  'cidade',
                  'uf',
                  'cep'
        ]
